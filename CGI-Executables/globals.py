#!/usr/bin/python
"""
# globals.py 5/15/2019 dwg - begin Phoenix-X
# globals.py 10/22/2018 dwg - reorganize Phoenix code and data
# globals.py 10/18/2018 dwg - added WHEELIP for license handling
# globals.py 10/9/2018 dwg - adjust audit dirs
# globals.py 10/8/2018 dwg - added AUDITDATA_DIRSPEC
# globals.py 9/6/2018 dwg - switch to ichibrosan.com domain
# globals.py 9/2/2018 dwg - phoenix global variables (site level)
#######################################################################
### Copyright (C) 2014-2019 Douglas W Goodall. All Rights Reserved. ###
#######################################################################
"""

import datetime

month = str(datetime.datetime.today().month)
day = str(datetime.datetime.today().day)
year  = str(datetime.datetime.today().year)
hour = str(datetime.datetime.today().hour)

RMJ = year
RMN = month
RUP = day
RTP = hour
VER = str(RMJ)+"."+str(RMN)+"."+str(RUP)+"."+str(RTP)
VERSION = VER

LANGUAGE = "english"

HOST_USER = "doug"

HSTNAME    = "localhost"
SMTPHOST   = HSTNAME
APPDOMAIN  = HSTNAME
VPAHOST    = HSTNAME
WEBHOST    = HSTNAME
WHEELIP    = HSTNAME

STANDARD = "http://"
SECURE   = "https://"

VPA_WKPN = "5164"

EXIT_SUCCESS = True
EXIT_FAILURE = False

APPBASE = "/Library/WebServer/"
APPCGI  = APPBASE + "CGI-Executables/"
APPDATA_DIRSPEC = APPBASE + "AppData/"
AUDITAPP_DIRSPEC = APPBASE + "Audit/Apps/"
AUDITUSER_DIRSPEC = APPBASE + "Audit/Users/"
SQLSCRIPT_FILEPATH = APPBASE + "SQL/"
USERTAR_ARCPATH = APPBASE + "Archives/"
USERFORM_SCHPATH = APPBASE + "Schemas/"
USERDATA_DIRSPATH = APPBASE + "Users/"
USERHTML_FILEPATH = APPBASE + "Documents/"
USERLOG_FILEPATH = APPBASE + "Log/"
USERTEXT_NLSPATH = APPBASE + "NLS/"
USERHTML_IMGURL = STANDARD + WEBHOST + "/images/"
USERHTML_PAGEURL = STANDARD + WEBHOST + "/cgi-bin/"

# These macros are passed to intro and alert routines instead of quoated literals
UNKNOWNUSER = "unkuser"

####################
# eof - globals.py #
####################
