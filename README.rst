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
compromised.

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


Change Log
-------------

========== ======= =============================
2016-10-29 0.1.1   published to PyPi
2016-09-16 0.0.1   init
========== ======= =============================
