import urllib2
import json

# -------------------------------------------------------
#  This file contains following object for api url request
#
#       - header
#       - post data
#       - request 
#
# -------------------------------------------------------

# Request header
header = {
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3; .NET4.0E; Shuame)",
}

# request header for json type data
header_jsonreq = {
    "render": "unieap",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3; .NET4.0E; Shuame)",
}


# get_hostIP
req_get_hostIP = urllib2.Request(
    url = 'http://uems.sysu.edu.cn/jwxt/edp/menu/RootMenu.jsp',
    headers = header
)


# get_student_info
postdata_student_info = json.dumps({"header":{"code": -100, "message": {"title": "", "detail": ""}},"body":{"dataStores":{"xsxxStore":{"rowSet":{"primary":[],"filter":[],"delete":[]},"name":"xsxxStore","pageNumber":1,"pageSize":10,"recordCount":0,"rowSetName":"pojo_com.neusoft.education.sysu.xj.grwh.model.Xsgrwhxx"}},"parameters":{"args": [""]}}})

req_get_major = urllib2.Request(
    url = 'http://uems.sysu.edu.cn/jwxt/WhzdAction/WhzdAction.action?method=getGrwhxxList',
    data = postdata_student_info,
    headers = header_jsonreq
)


# get_zxf_req
def postdata_zxf_req(nj, zyh):
    """
     - nj: grade
     - zyh: a integer string response by request:
        http://uems.sysu.edu.cn/jwxt/xscjcxAction/xscjcxAction.action?method=judgeStu
    """
    data = json.dumps({ "header": { "code": -100, "message": { "title": "", "detail": "" } }, "body": { "dataStores": { "zxzyxfStore": { "rowSet": {"primary":[], "filter":[], "delete":[]}, "name": "zxzyxfStore", "pageNumber": 1, "pageSize": 2147483647, "recordCount": 0, "rowSetName": "pojo_com.neusoft.education.sysu.djks.ksgl.model.TwoColumnModel" } }, "parameters": { "zxzyxfStore-params": [ {"name": "pylbm", "type": "String", "value": "'01'", "condition": " = ", "property": "x.pylbm"}, {"name": "nj", "type": "String", "value": nj, "condition": " = ", "property": "x.nj"}, {"name": "zyh", "type": "String", "value": zyh, "condition": " = ", "property": "x.zyh"} ], "args": [] } } })
    return data

def req_zxf_req(nj, zyh):
    req = urllib2.Request(
        url = 'http://uems.sysu.edu.cn/jwxt/xscjcxAction/xscjcxAction.action?method=getZyxf',
        data = postdata_zxf_req(nj, zyh),
        headers = header_jsonreq
    )
    return req


# get_zxf_earned
def postdata_zxf_earned(sid, year, term):
    """
     - year: "2012-2013"
     - term: "1"
     - empty string represent for all years or terms
    """
    data = json.dumps( { "body": { "dataStores": { "xfStore": { "rowSet": { "primary": [], "filter": [], "delete": [] }, "name": "xfStore", "pageNumber": 1, "pageSize": 2147483647, "recordCount": 0, "rowSetName": "pojo_com.neusoft.education.sysu.djks.ksgl.model.TwoColumnModel" } }, "parameters": { "args": [ sid, year, term, "01" ] } } })
    return data

def req_zxf_earned(sid, year, term):
    req = urllib2.Request(
        url = 'http://uems.sysu.edu.cn/jwxt/xscjcxAction/xscjcxAction.action?method=getAllXf',
        data = postdata_zxf_earned(sid, year, term),
        headers = header_jsonreq
    )
    return req


# get_zjd_average
def postdata_zjd_average(sid, year, term):
    data = json.dumps({"header":{"code": -100, "message": {"title": "", "detail": ""}},"body":{"dataStores":{"allJdStore":{"rowSet":{"primary":[],"filter":[],"delete":[]},"name":"allJdStore","pageNumber":1,"pageSize":2147483647,"recordCount":0,"rowSetName":"pojo_com.neusoft.education.sysu.djks.ksgl.model.TwoColumnModel"}},"parameters":{"args": [sid, year, term, ""]}}})
    return data

def req_zjd_average(sid, year, term):
    req = urllib2.Request(
        url = 'http://uems.sysu.edu.cn/jwxt/xscjcxAction/xscjcxAction.action?method=getAllJd',
        data = postdata_zjd_average(sid, year, term),
        headers = header_jsonreq
    )
    return req


# get_kcjd
def postdata_kcjd(year, term):
    data = json.dumps({ "header":{ "code": -100, "message": { "title": "", "detail": "" } }, "body":{ "dataStores":{ "kccjStore":{ "rowSet":{ "primary":[],"filter":[],"delete":[] }, "name":"kccjStore", "pageNumber":1, "pageSize":10, "recordCount":0, "rowSetName":"pojo_com.neusoft.education.sysu.xscj.xscjcx.model.KccjModel", "order":"t.xn, t.xq, t.kch, t.bzw" } }, "parameters":{ "kccjStore-params": [ { "name": "Filter_t.pylbm_0.5692540288519818", "type": "String", "value": "'01'", "condition": " = ", "property": "t.pylbm" }, { "name": "Filter_t.xn_0.6301131875580945", "type": "String", "value": year, "condition": " = ", "property": "t.xn"}, { "name": "Filter_t.xq_0.6804709813288836", "type": "String", "value": term, "condition": " = ", "property": "t.xq" } ], "args": ["student"]}}})
    return data
def req_kcjd(year, term):
    req = urllib2.Request(
        url = 'http://uems.sysu.edu.cn/jwxt/xscjcxAction/xscjcxAction.action?method=getKccjList',
        data = postdata_kcjd(year, term),
        headers = header_jsonreq
    )
    return req


# get_score_detail
def postdata_score_detail(cjlcId):
    data = json.dumps({"header":{"code": -100, "message": {"title": "", "detail": ""}},"body":{"dataStores":{"fxcjStore":{"rowSet":{"primary":[],"filter":[],"delete":[]},"name":"fxcjStore","pageNumber":1,"pageSize":2147483647,"recordCount":0,"rowSetName":"pojo_com.neusoft.education.sysu.xscj.cj.entity.FxcjEntity"}},"parameters":{"args": [cjlcId]}}})
    return data
def req_score_detail(cjlcId):
    req = urllib2.Request(
        url = 'http://uems.sysu.edu.cn/jwxt/xscjcxAction/xscjcxAction.action?method=getFxcj',
        data = postdata_score_detail(cjlcId),
        headers = header_jsonreq
    )
    return req


# get_selected_courses
def postdata_selected_courses(year, term):
    data = json.dumps({"header":{"code": -100, "message": {"title": "", "detail": ""}},"body":{"dataStores":{"xsxkjgStore":{"rowSet":{"primary":[],"filter":[],"delete":[]},"name":"xsxkjgStore","pageNumber":1,"pageSize":20,"recordCount":0,"rowSetName":"pojo_com.neusoft.education.sysu.xk.xkjg.entity.XkjgxxEntity","order":"xkjg.xnd desc,xkjg.xq desc, xkjg.jxbh"}},"parameters":{"xsxkjgStore-params": [{"name": "xnd", "type": "String", "value": year, "condition": " = ", "property": "xkjg.xnd"}, {"name": "xq", "type": "String", "value": term, "condition": " = ", "property": "xkjg.xq"}], "args": []}}})
    return data
def req_selected_courses(year, term):
    req = urllib2.Request(
        url = 'http://uems.sysu.edu.cn/jwxt/xstk/xstk.action?method=getXsxkjgxxlistByxh',
        data = postdata_selected_courses(year, term),
        headers = header_jsonreq
    )
    return req


# get_course_table
def postdata_course_table(year, term):
    data = json.dumps({"header":{"code": -100, "message": {"title": "", "detail": ""}},"body":{"dataStores":{},"parameters":{"args": [term, year], "responseParam": "rs"}}})
    return data
def req_course_table(year, term):
    req = urllib2.Request(
        url = 'http://uems.sysu.edu.cn/jwxt/KcbcxAction/KcbcxAction.action?method=getList',
        data = postdata_course_table(year, term),
        headers = header_jsonreq
    )
    return req
