# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from vizhash import __version__


setup(
	name="VizHash.py",
	version=__version__,
	author="Marien Fressinaud",
	author_email="dev@marienfressinaud.fr",
	description="A generator of string visual hashes.",
	license="zlib/libpng",
	url="https://github.com/marienfressinaud/vizhash.py",
	packages=find_packages('.'),
	long_description=open('README.md').read(),
	classifiers=[
		"Programming Language :: Python",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
		"Intended Audience :: Information Technology",
		"License :: OSI Approved :: zlib/libpng License",
		"Natural Language :: English",
	],
)
