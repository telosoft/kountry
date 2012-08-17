===========================================
 kountry - Country data library for Python
===========================================

*kountry* is a Python library which provides country data to
applications. The data used in the library is obtained from various
resources including `GeoNames <http://www.geonames.org>`_ and
`Wikipedia <http://www.wikipedia.org>`_.

Installation
============

You can install the latest version of *kountry* from the GitHub
repository::

    $ pip install git+https://github.com/telosoft/kountry.git

Example Usage
=============

Import the canonical *Country* class::

    >>> from kountry import Country

Retrieve a *Country* object for a given identifier::

    >>> turkey = Country.get("TR")
    >>> turkey
    Turkey
    >>> turkey.code_2
    'TR'
    >>> turkey.code_3
    'TUR'
    >>> turkey.enum
    '792'
    >>> turkey.name
    'Turkey'
    >>> turkey.currency
    'TRY'

The identifier can be any of ``code_2``, ``code_3``, ``enum`` or
``name`` attributes of a *Country* object::

    >>> Country.get("TR") == Country.get("TUR")
    True
    >>> Country.get("TUR") == Country.get("792")
    True
    >>> Country.get("792") == Country.get("Turkey")
    True

Quick API Reference
===================

.. todo:: Provide the FULL API reference.

*kountry* has a single Python class and the entire functionality is
built around it: ``Country``.

Class Attributes:
-----------------

- ``DB``: Provides the country database with four indices (for
  ``code_2``, ``code_3``, ``enum`` and ``name``).

Object Attributes:
------------------

- ``code_2``
- ``code_3``
- ``enum``
- ``code_fips``
- ``continent``
- ``currency``
- ``tld``
- ``name``
- ``capital``
- ``postal_code_format``
- ``postal_code_regex``
- ``phone_prefixes``

Class Methods:
--------------

- ``get(identifier)``: Queries the country database for the identifier
  provided and returns the country object if found, ``None``
  otherwise.
- ``put(country)``: Inserts or overrides a country in the DB.
