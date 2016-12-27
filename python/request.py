#!/usr/bin/python

import json
import requests

api_url = "http://rno-store-tools-svc.apple.com:9604/service/fleetdomain"

def main():
	url = "{}{}" . format(api_url, '/app')
	data = {
# 		"appname" : "App1",
# 		"operation" : "start",
 		"port" : 8213
		"hostName" : "rn2-rosp-pr01-lsvc01.rno.apple.com"
	}
	result = requests.get(url, params=data, headers=None)
	print result.url
	print result.status_code
	print result.text
	#print result.json()
	
if __name__ == '__main__':
	main()
