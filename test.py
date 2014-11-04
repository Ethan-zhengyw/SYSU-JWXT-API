# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib
import json
import sysu_jwxt.login as login
import sysu_jwxt.data_module as data_module
import sysu_jwxt.api as api

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

print " Login\n#-----------------------------"
sid = raw_input(" sid: ")
pwd = raw_input(" pwd: ")
print

key, jsessionid = login.get_jsessionid(sid, pwd, opener)

years = ["2012-2013", "2013-2014"]
terms = ["1", "2", "3"]
year = "2013-2014"
term = "2"

print " Student information\n#-----------------------------"
print " Host IP: " + "\t" + api.get_hostIP(opener)
stuInfo = api.get_student_info(opener)
for attr in stuInfo:
    print " " + attr + ": " + "\t" + stuInfo[attr]
print

print " All Credits Request\n#-----------------------------"
print "", api.get_zxf_req(opener), "\n"

print " All Credits Earned\n#-----------------------------"
print "", api.get_zxf_earned("", "", opener), "\n"

print " Average GPA of All courses \n#-----------------------------"
print "", api.get_zjd_average("", "", opener), "\n"

print " Earned Creadits and GPA Per Term\n#-----------------------------"
for year in years:
    for term in terms:
        print " [" + year + " " + term + "]", "\t",
        earned = api.get_zxf_earned(year, term, opener)
        gpa = api.get_zjd_average(year, term, opener)
        print earned, "\t", gpa
        for a in api.get_kcjd(year, term, opener):
            for b in a:
                if b == "score_detail":
                    print b, ":"
                    for l in a[b]:
                        print "[",
                        for x in l:
                            print x,
                        print "]"
                else:
                    print b + ": \t", a[b]
            print

for course in api.get_selected_courses(year, term, opener):
    for attr in course:
        print attr + ": \t", course[attr]

table = api.get_course_table_html(year, term, opener)
