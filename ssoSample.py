from claroSSO import SSOApp
from optparse import OptionParser
from ConfigParser import ConfigParser
import json
import os
import webbrowser

if __name__ == "__main__":
	configPaths = os.getcwd() + os.sep + "sso.cfg";
	parser = OptionParser()
	parser.add_option("-a", "--app", dest="app_id", help="The application's id")
	parser.add_option("-k", "--auth", dest="auth_key", help="The application's authorization key")
	parser.add_option("-e", "--email", dest="email", help="The email address of the user to sign-in")
	parser.add_option("-r", "--role", dest="role", help="The role of the user to sign in")
	parser.add_option("-u", "--url", dest="url", help="The URL of the Claro instance")
	parser.add_option(
		"-c", "--config", dest="config", help="""A configuration file to load.  Any options specified
		on the command line will override the config file""")
	(options, args) = parser.parse_args()
	if (options.config) != None:
		configPaths.appen(options.config)

	# Attempt to read default config file from current directory, along with file specfied in
	# command line options, if any
	config = ConfigParser()
	readPaths = config.read(configPaths)
	# Grap any config file options found, for which nothing was specified on the command line
	if config.has_option("options", "app_id") and options.app_id == None:
		options.app_id = config.get("options", "app_id")

	if config.has_option("options", "auth_key") and options.auth_key == None:
		options.auth_key = config.get("options", "auth_key")

	if config.has_option("options", "email") and options.email == None:
		options.email = config.get("options", "email")

	if config.has_option("options", "role") and options.role == None:
		options.role = config.get("options", "role")

	if config.has_option("options", "url") and options.url == None:
		options.url = config.get("options", "url")

	if options.app_id == None:
		print "An application ID is required"
		exit(0)

	if options.auth_key == None:
		print "An authentication key is required"
		exit(0)

	if options.email == None:
		print "An email address is required"
		exit(0)

	if options.role == None:
		print "A role is required"
		exit(0)

	if options.url == None:
		print "A url is required"
		exit(0)

	user = {'email' : options.email, 'role': options.role}
	ssoApp = SSOApp(options.app_id, options.auth_key, options.url)
	ssoResponse = ssoApp.request(user)

	if ssoResponse: 
		webbrowser.open(ssoApp.loginURL, 2, True)
	else:
		print ssoApp.lastStatus
		print json.dumps(ssoApp.headers, indent=4, sort_keys=True)
