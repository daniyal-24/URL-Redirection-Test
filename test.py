#!/usr/bin/env python
import requests
import sys
import time
import os
import argparse
heading = """
 #################################################
 #    Tool:   URL Redirection Testing  
 #    By:     Daniyal Nasir
 #################################################
    """
def main():
    os.system('clear')
    print(heading)
    parser = argparse.ArgumentParser()
    parser.add_argument('-dl', help='domains file path', nargs=1, dest='domainlist', required=True)
    parser.add_argument('-pl', help='redirections payloads path', nargs=1, dest='payloadlist', required=True)
    args = parser.parse_args()
    # first argument - file with subdomains
    file = args.domainlist[0]
    # second argument - payload string
    payloads = args.payloadlist[0]
    #open file with subdomains and iterates
    with open(file) as f:
		print ""
		print "Finding the URL redirections on the Target..."
		print ""
		time.sleep(4)

                for line in f:
		    with open(payloads) as p:
			for payload in p:
                    	    try:
                        	line2 = line.strip()
                        	line3 = '\nhttp://' + line2 + payload
                        	print line3
                        	response = requests.get(line3, verify=True)  
                        	print response

                        	try:
                            	    if response.history:
                                	print "\n\n\n\n\n\nRequest was redirected"
                                	for resp in response.history:
                                    	    print "|"
                                    	    print resp.status_code, resp.url
                                	print "********Final destination:*********"
                                	print "+"
                                	print response.status_code, response.url
                                        print "\n\n\n\n\n"


                           	    else:
                                	print "Request was not redirected"

                        	except :
                            	    print "connection error :("

                   	    except:
                        	print "quitting.."
try:
	main()
except IndexError:
	print(" Usage: python "+sys.argv[0]+" [domain.file] [redirection.payload]\n")
        print(" Example python "+sys.argv[0]+" payload.list '//google.com/%2F..'\n")







