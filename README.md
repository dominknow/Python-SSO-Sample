# Claro SSO API client sample

This package includes a module for interacting with the Claro Single Sign-on API (claroSSO.py), as well
as a sample command line application (ssoSampley.py).

The [requests](http://docs.python-requests.org/en/latest/) module is a dependency of claroSSO.py. The command line 
client will take either a config file (see the .template) in the current working directory, or as specified on the command line.

Command line options will override any config file options.

Options can be viewed by running python ssoSample.py -h
