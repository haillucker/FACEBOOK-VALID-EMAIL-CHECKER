#!/usr/bin/python
# -*- coding: utf-8 -*-

# ( -- IMPORTS -- ) #
import requests
import time
import json
import sys
from colorama import Fore
from colorama import Style
from pprint import pprint
from colorama import init
init(autoreset=True)

# ( -- COLORAMA COLORS -- ) #
rd = Fore.RED
cy = Fore.CYAN
wh = Fore.WHITE
gr = Fore.GREEN
yl = Fore.YELLOW
mg = Fore.MAGENTA
bl = Fore.BLACK

# ( -- LOGO * INFO -- ) #
bugs = '''{} {}
    ____  ____  _   _  ____ ____         ____ _   _ _____ ____ _  _______ ____  ____  
   / __ \| __ )| | | |/ ___/ ___|       / ___| | | | ____/ ___| |/ / ____|  _ \/ ___| 
  / / _` |  _ \| | | | |  _\___ \ _____| |   | |_| |  _|| |   | ' /|  _| | |_) \___ \ 
 | | (_| | |_) | |_| | |_| |___) |_____| |___|  _  | |__| |___| . \| |___|  _ < ___) |
  \ \__,_|____/ \___/ \____|____/       \____|_| |_|_____\____|_|\_\_____|_| \_\____/ 
   \____/                                                                             
\n [$] BUGS FACEBOOK VALID EMAIL CHECKER.
 [$] URL = ('https://www.Brazzers.com/').
 [$] SCRIPT PROGRAMMED BY BUGS WITH PYTHON2.
'''.format(mg, mg)
#################################
# ( -- PROGRAMMED BY @BUGS -- ) #
#################################

# ( -- FULL API SCRIPT -- ) #

print bugs
print '\n{} {}[+] FACEBOOK VALID EMAIL CHECKER [+]'.format(cy, cy)
print ''
# ----------------------------------- ## ----------------------------------- #
list = raw_input('{} {}[X] ENTER YOUR LIST PATH NAME X> '.format(cy, cy))
print ''
# ----------------------------------- ## ----------------------------------- #
req_headers = {
	'Origin': 'https://m.facebook.com',
	'Upgrade-Insecure-Requests': '1',
	'Content-Type': 'application/x-www-form-urlencoded',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Referer': 'https://m.facebook.com/login/identify/?ctx=recover&c&multiple_results=0&_rdr',
	'Cookie': 'sb=cYoyW3nsXPVkGd1ScoizOZey; datr=cYoyW9tC71TOh4siRRrD1wkv; reg_fb_gate=https%3A%2F%2Fwww.facebook.com%2F; m_pixel_ratio=1; wd=1280x656; reg_fb_ref=https%3A%2F%2Fm.facebook.com%2Ffavicon.ico; fr=04ZmanersrttG9YVA..BbMopx.lo.AAA.0.0.BbMo96.AWWm5QHA'
}
# ----------------------------------- ## ----------------------------------- #
try:
	file = open(list,'r').readlines()
	list_len = str(len(file))
	print '{} {}[+] '.format(yl, yl) + 'YOUR LIST EMAILS NUM IS X> '.format(yl, yl) + list_len + '\n'
	count = 0
	for mail in file:
		count+=1
		mail = mail.strip()
		fb_url = 'https://m.facebook.com/login/identify/?ctx=recover&search_attempts=1'
		req_data = 'lsd=AVqNg7vZ&email='+mail+'&did_submit=Search'
		request = requests.post(fb_url, data=req_data, headers=req_headers)
		src = request.content
		# //print src
		if 'https://scontent-cai1-1.xx.fbcdn.net' in src:
			print '{} {}[+] '.format(gr, gr) + '(' + str(count) + ') ' + mail + ' => [ + VALID + ]'.format(gr, gr)
			valid = open('VALID_FB.txt', 'a+')
			valid.write('[+] [ ' + mail + ' ] => [ + VALID + ] \n')
			valid.close()
		else:
			mail = mail.format(rd, rd)
			print '{} {}[+] '.format(rd, rd) + '(' + str(count) + ') ' + mail + ' => [ + INVALID + ]'.format(rd, rd)
except (IOError, TypeError) as e:
	print '[X]'
