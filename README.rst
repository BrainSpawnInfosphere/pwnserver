pwnserver
============================

.. image:: https://img.shields.io/pypi/v/pwnserver.svg
	:target: https://pypi.python.org/pypi/pwnserver/
	:alt: Latest Version
.. image:: https://img.shields.io/pypi/l/pwnserver.svg
	:target: https://pypi.python.org/pypi/pwnserver/
	:alt: License


.. image:: https://github.com/walchko/pwnserver/blob/master/pics/screenshot.png
	:align: center
	:alt: Screenshot

Runs a simple web server that shows if your account information has been
compromised. This polls `haveibeenpwned <https://haveibeenpwned.com>`_ and
returns any compromised accounts found.

Install
-----------

pip
~~~~~

::

	pip install pwnserver

Development
~~~~~~~~~~~~~

::

	git clone https://github.com/walchko/pwnserver
	cd pwnserver
	pip install -e .

Usage
---------

To run the server:

::

	pwnserver --email emails.json --port 9000

You need a config file with names and emails:

.. code-block:: json

	{
		"bob":
			[
				"bob.tom@google.com",
				"bob.tom@yahoo.com"
			],
		"tom":
			[
				"tom.jones@google.com",
				"tom.jones@snuggle.org"
			]
	}

Raw Output
------------

A sample of the raw output from ``haveibeenpwned.com``:

.. code-block:: json

	[{"PwnCount": 152445165, "Domain": "adobe.com", "IsSensitive": false,
	"Name": "Adobe", "Title": "Adobe", "DataClasses": ["Email addresses",
	"Password hints", "Passwords", "Usernames"], "IsRetired": false,
	"LogoType": "svg", "BreachDate": "2013-10-04", "IsActive": true,
	"AddedDate": "2013-12-04T00:00:00Z", "IsVerified": true, "Description":
	"In October 2013, 153 million Adobe accounts were breached with each
	containing an internal ID, username, email, encrypted password and a password
	hint in plain text. The password cryptography was poorly done and many were
	quickly resolved back to plain text. The unencrypted hints also disclosed much
	about the passwords adding further to the risk that hundreds of millions of
	Adobe customers already faced."}, {"PwnCount": 68648009, "Domain":
	"dropbox.com", "IsSensitive": false, "Name": "Dropbox", "Title":
	"Dropbox", "DataClasses": ["Email addresses", "Passwords"], "IsRetired":
	false, "LogoType": "svg", "BreachDate": "2012-07-01", "IsActive": true,
	"AddedDate": "2016-08-31T00:19:19Z", "IsVerified": true, "Description":
	"In mid-2012, Dropbox suffered a data breach which exposed the stored
	credentials of tens of millions of their customers. In August 2016, they forced
	password resets for customers they believed may be at risk. A large volume of
	data totalling over 68 million records was subsequently traded online and
	included email addresses and salted hashes of passwords (half of them SHA1,
	half of them bcrypt)."}]

Change Log
-------------

========== ======= =============================
2016-10-29 0.1.1   published to PyPi
2016-09-16 0.0.1   init
========== ======= =============================
