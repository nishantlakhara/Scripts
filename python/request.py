#!/usr/bin/python

import json
import requests

api_url = "http://google.com"

def main():
	url = "{}{}" . format(api_url, '/app')
	data = {
# 		"appname" : "App1",
# 		"operation" : "start",
 		"port" : 1212,
		"hostName" : "host1"
	}
	result = requests.get(url, params=data, headers=None)
	print result.url
	print result.status_code
	print result.text
	#print result.json()
	
if __name__ == '__main__':
	main()
