#!/usr/bin/python

import json
import urllib2
import urllib

api_url = "http://localhost:8080"

def main():
	url = "{}{}" . format(api_url, '/app')
	data = {'port': 9991, 'appname': 'App1', 'operation': 'start'}
	request = urllib2.Request(url, data = urllib.urlencode(data))
	response = urllib2.urlopen(request)
	print response.getcode()
	response_json = json.loads(response.read())
	print response_json
	print response_json["operationStatus"]
	#print result.json()
	
if __name__ == '__main__':
	main()
