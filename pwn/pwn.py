#!/usr/bin/env python
#
# created 2016-09-16
# see https://haveibeenpwned.com/API/v2 for more details
#

from __future__ import print_function
import requests
try:
	import simplejson as json
except:
	import json
from time import sleep

# API https address
APIURL = "https://haveibeenpwned.com/api/v2/breachedAccount/"
truncate = '?truncateResponse=false'

# standard HTTP response codes used
ACCOUNT_IS_BAD   = 200
BAD_REQUEST      = 400
FORBIDDEN        = 403
ACCOUNT_IS_GOOD  = 404
RATE_LIMIT_ERROR = 429

"""
[{u'PwnCount': 152445165, u'Domain': u'adobe.com', u'IsSensitive': False,
u'Name': u'Adobe', u'Title': u'Adobe', u'DataClasses': [u'Email addresses',
u'Password hints', u'Passwords', u'Usernames'], u'IsRetired': False,
u'LogoType': u'svg', u'BreachDate': u'2013-10-04', u'IsActive': True,
u'AddedDate': u'2013-12-04T00:00:00Z', u'IsVerified': True, u'Description':
u'In October 2013, 153 million Adobe accounts were breached with each
containing an internal ID, username, email, encrypted password and a password
hint in plain text. The password cryptography was poorly done and many were
quickly resolved back to plain text. The unencrypted hints also disclosed much
about the passwords adding further to the risk that hundreds of millions of
Adobe customers already faced.'}, {u'PwnCount': 68648009, u'Domain':
u'dropbox.com', u'IsSensitive': False, u'Name': u'Dropbox', u'Title':
u'Dropbox', u'DataClasses': [u'Email addresses', u'Passwords'], u'IsRetired':
False, u'LogoType': u'svg', u'BreachDate': u'2012-07-01', u'IsActive': True,
u'AddedDate': u'2016-08-31T00:19:19Z', u'IsVerified': True, u'Description':
u'In mid-2012, Dropbox suffered a data breach which exposed the stored
credentials of tens of millions of their customers. In August 2016, they forced
password resets for customers they believed may be at risk. A large volume of
data totalling over 68 million records was subsequently traded online and
included email addresses and salted hashes of passwords (half of them SHA1,
half of them bcrypt).'}]
"""

def readJson(fname):
	"""
	Reads a Json file
	in: file name
	out: length of file, dictionary
	"""
	try:
		with open(fname, 'r') as f:
			data = json.load(f)

		return data
	except IOError:
		raise Exception('Could not open {0!s} for reading'.format((fname)))

def writeJson(fname, data):
	"""
	Writes a Json file
	"""
	try:
		with open(fname, 'w') as f:
			json.dump(data, f)

	except IOError:
		raise Exception('Could not open {0!s} for writing'.format((fname)))


def isBreach(email):
	"""
	Given an email, this checks the database for a compromised account

	in: email/account
	out: http status code, 200 bad, 404 good
	"""
	url = APIURL+email
	resp = requests.get(url, verify=True)

	if resp.status_code == ACCOUNT_IS_GOOD:
		return False, None
	elif resp.status_code == ACCOUNT_IS_BAD:
		return True, resp.json()
	else:
		return 'error', resp.status_code


if __name__ == '__main__':
	print('hello')
