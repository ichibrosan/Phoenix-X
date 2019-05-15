#!/usr/local/bin/python3.7
import cgi
import cgitb
cgitb.enable()

#cgi.test()

print("Content-type:\ttext/html\n\n")

from globals import *

if __name__ == "__main__":
    print("<p>APPBASE is "+APPBASE)
    print("<p>APPCGI is "+APPCGI)
    print("<p>APPDATA_DIRSPEC is "+APPDATA_DIRSPEC)
    print("<p>AUDITAPP_DIRSPEC is "+AUDITAPP_DIRSPEC)
    print("<p>AUDITUSER_DIRSPEC is"+AUDITUSER_DIRSPEC)
    print("<p>SQLSCRIPT_FILEPATH is "+SQLSCRIPT_FILEPATH)
    print("<p>USERTAR_ARCPATH is "+USERTAR_ARCPATH)
    print("<p>USERFORM_SCHPATH is "+USERFORM_SCHPATH)
    print("<p>USERDATA_DIRSPATH is "+USERDATA_DIRSPATH)
    print("<p>USERHTML_FILEPATH is"+USERHTML_FILEPATH)
    print("<p>USERLOG_FILEPATH is "+USERLOG_FILEPATH)
    print("<p>USERTEXT_NLSPATH is "+USERTEXT_NLSPATH)
    print("<p>USERHTML_IMGURL is "+USERHTML_IMGURL)
    print("<p>USERHTML_PAGEURL is "+USERHTML_PAGEURL)

