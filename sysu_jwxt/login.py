# -------------------------------------------------------
#  post request to check security and get the JSESSIONID
# -------------------------------------------------------

import urllib
import urllib2
import data_module

def get_jsessionid(username, password, opener):

    header = data_module.header

    postdata = urllib.urlencode ({
        'j_username': username,
        'j_password': password
    })

    req = urllib2.Request(
        url = 'http://uems.sysu.edu.cn/jwxt/j_unieap_security_check.do',
        data = postdata,
        headers = header
    )

    result = opener.open(req)
    resulturl = result.geturl()

    key = False
    jsessionid = ""

    if "jsessionid" in resulturl:
        key = True
        jsessionid = resulturl[resulturl.find('=')+1:resulturl.find('?')]

    return key, jsessionid
