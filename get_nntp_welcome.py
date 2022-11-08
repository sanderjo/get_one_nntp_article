#!/usr/bin/env python3


# Get Welcom message from a NNTP / NNTPS server

import nntplib
import sys

try:
        mynntpserver = sys.argv[1]
except:
        print("Usage:", sys.argv[0], " nntpserver")
        sys.exit(-1)


print(mynntpserver, end=': ' )

try:
        s = nntplib.NNTP_SSL(mynntpserver, port=563)
        print(s.getwelcome())
except:
        print("error")

try:
        s.quit()
except:
        pass
