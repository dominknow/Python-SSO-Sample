"This module provides methods/classes for interacting with the Claro Single-Sign On API"
import json
import requests
import hashlib

class SSOApp:
	"This class represents an authorized SSO app"

	def __init__(self,app_id, auth_key, url):
		"The public constructor"
		self.app_id = app_id
		self.auth_key = auth_key
		self.url = url
		self.tokenURL = url + "/sso.cfm/" + app_id + "/token"
		self.loginURL = ""
		self.lastStatus = 0
		self.headers = {}

	def request(self, user):
		"Makes a request for a user, represented by the 'user' dictionary"
		userJSON = json.dumps(user)
		loginHash = hashlib.sha1(userJSON + self.auth_key).hexdigest()
		response = requests.post(self.tokenURL, data={'userJSON' : userJSON, 'loginHash' : loginHash})
		self.lastStatus = int(response.status_code)
		self.headers = response.headers
		if self.headers["Location"] != None:
			self.loginURL = self.headers["Location"]

		if (self.lastStatus == 200 or self.lastStatus == 201) :
			return True
		else :
			return False

