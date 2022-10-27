#!/usr/bin/env python3


# Get one article from a NNTP / NNTPS server

import nntplib
import sys

try:
	mynntpserver = sys.argv[1]
	myname = sys.argv[2]
	mypassword = sys.argv[3]
	articleid = sys.argv[4]
except:
	print("Usage:", sys.argv[0], " nntpserver username password articleid")
	sys.exit(-1)
	

# We want articleid to begin with "<" and end with ">", so add if not there	
if articleid[0] != "<" and articleid[-1] != ">":
	articleid = "<" + articleid + ">"

s = nntplib.NNTP_SSL(mynntpserver, port=563, user = myname, password = mypassword)

article_body = s.body(articleid, file = "mybody-" + mynntpserver + "-" + articleid + ".bin")

blabla = s.article(articleid, file = "myarticle-" + mynntpserver + "-" + articleid + ".bin")
print(article_body[:20])

s.quit()

