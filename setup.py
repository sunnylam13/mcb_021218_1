try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Madlibs program that replaces ADJECTIVE, VERB, NOUN, etc with a word of your choosing.',
	'author': 'Sunny Lam',
	'url': 'https://github.com/sunnylam13/mcb_021218_1',
	'download_url': 'https://github.com/sunnylam13/mcb_021218_1',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['shelve, pyperclip, sys'],
	'scripts': [],
	'name': 'Multiple Clipboard'
}

setup(**config)