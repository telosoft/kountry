from setuptools import find_packages
from setuptools import setup
import os
import sys

# The absolute directory path:
here = os.path.abspath(os.path.dirname(__file__))

# The README file contents:
README = open(os.path.join(here, "README.rst")).read()

# The LICENSE file contents:
LICENSE = open(os.path.join(here, "LICENSE")).read()

# Requirements for installation:
install_requires = []

# Requirements for setup:
setup_requires = [
    "versiontools >= 1.8",
    ],

# Requirements for tests:
tests_require = []

# Requirements for documentation:
docs_extras = [
    "Sphinx",
    "docutils",
    ]

# Extra requirements for testing:
testing_extras = tests_require + [
    "nose",
    "coverage",
    "virtualenv",
    ]

# Setup now:
setup(
    name="kountry",
    version=":versiontools:kountry",
    description=("A Python library which provides country data"),
    long_description=README,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        ],
    keywords="country iso-3166",
    author="Vehbi Sinan Tunalioglu",
    author_email="vst@vsthost.com",
    url="http://github.com/telosoft/kountry",
    license=LICENSE,
    py_modules=["kountry"],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    setup_requires=setup_requires,
    extras_require={
        "testing": testing_extras,
        "docs": docs_extras,
        },
    tests_require=tests_require,
    test_suite="tests",
)
