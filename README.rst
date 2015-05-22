|status| |version| |downloads| |license| |issues| |forks| |stars| |ages| |works| |badges|

Introduction
------------

Connery is a simple, lightweight, open source, easy-to-use IRC Utility bot,
written in Python. It's designed to be easy to use, run and extend.

Installation
------------

Latest stable release
=====================
If you're on Fedora or Arch, the easiest way to install is through your package
manager. The package is named ``connery`` in both Fedora and the AUR. On other
distros, and pretty much any operating system you can run Python on, you can
install `pip <https://pypi.python.org/pypi/pip/>`_, and do ``pip install
connery``. Failing all that, you can download the latest tarball from
http://connery.dftba.net and follow the steps for installing from the latest
source below.

Latest source
=============
First, either clone the repository with ``git clone
git://github.com/embolalia/connery.git`` or download a tarball from GitHub.

Note: connery requires Python 2.7 or Python 3.3 to run. On Python 2.7,
connery requires ``backports.ssl_match_hostname`` to be installed. Use
``pip install backports.ssl_match_hostname`` or ``yum install python-backports.ssl_match_hostname`` to install it,
or download and install it manually `from PyPi <https://pypi.python.org/pypi/backports.ssl_match_hostname>`.

In the source directory (whether cloned or from the tarball) run
``setup.py install``. You can then run ``connery`` to configure and start the
bot. Alternately, you can just run the ``connery.py`` file in the source
directory.

Adding modules
--------------
The easiest place to put new modules is in ``~/.connery/modules``. You will need
to add a a line to the ``[core]`` section of your config file saying
``extra = /home/yourname/.connery/modules``.

Some extra modules are available in the
`connery-extras <https://github.com/embolalia/connery-extras>`_ repository, but of
course you can also write new modules. A `tutorial <https://github.com/embolalia/connery/wiki//Connery-tutorial,-Part-2>`_
for creating new modules is available on the wiki.
API documentation can be found online at http://connery.dftba.net/docs, or
you can create a local version by running ``make html`` in the ``doc``
directory.

Further documentation
---------------------

In addition to the `official website <http://connery.dftba.net>`_, there is also a
`wiki <http://github.com/embolalia/connery/wiki>`_ which includes valuable
information including a full listing of
`commands <https://github.com/embolalia/connery/wiki/Commands>`_.

Questions?
----------

Join us in `#connery <irc://irc.freenode.net/#connery>`_ on Freenode.

.. |status| image:: https://travis-ci.org/embolalia/connery.svg
   :target: https://travis-ci.org/embolalia/connery
.. |coverage-status| image:: https://coveralls.io/repos/embolalia/connery/badge.png
   :target: https://coveralls.io/r/embolalia/connery
.. |version| image:: https://img.shields.io/pypi/v/connery.svg
   :target: https://pypi.python.org/pypi/connery
.. |downloads| image:: https://img.shields.io/pypi/dm/connery.svg
   :target: https://pypi.python.org/pypi/connery
.. |license| image:: https://img.shields.io/pypi/l/connery.svg
   :target: https://github.com/embolalia/connery/blob/master/COPYING
.. |issues| image:: https://img.shields.io/github/issues/embolalia/connery.svg
   :target: https://github.com/embolalia/connery/issues
.. |forks| image:: https://img.shields.io/github/forks/embolalia/connery.svg
   :target: https://github.com/embolalia/connery/network
.. |stars| image:: https://img.shields.io/github/stars/embolalia/connery.svg
   :target: https://github.com/embolalia/connery/stargazers
.. |ages| image:: https://img.shields.io/badge/ages-12%2B-green.svg
.. |works| image:: https://img.shields.io/badge/works-usually-yellow.svg
.. |badges| image:: https://img.shields.io/badge/badges-10-green.svg
