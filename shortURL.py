from __future__ import with_statement
import contextlib
#exception handling for the URL
try:
	from urllib.parse import urlencode
except ImportError:
	from urllib import urlencode
try:
	from urllib.request import urlopen
except ImportError:
	from urllib2 import urlopen
import sys

#if the code is not working, then use the command - python3 filename.py url

def make_tiny(url):
	request_url = ('http://tinyurl.com/api-create.php?' + 
	urlencode({'url':url}))
	with contextlib.closing(urlopen(request_url)) as response:
		return response.read().decode('utf-8')

def main():
	for tinyurl in map(make_tiny, sys.argv[1:]):
		print(tinyurl)

if __name__ == '__main__':
	main()