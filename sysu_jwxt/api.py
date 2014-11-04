#-*- coding: utf-8 -*-
import urllib2
import data_module
import data_re

# ---------------------------------------------------------------------
#  API list
#    
#    1.Student & Login Info
#       get_hostIP(opener)           - login host IP address
#       get_student_info(opener)     - student detail information
# 
#    2.Course & Credit
#       get_zxf_req(opener)                       - request credits in all
#       get_zxf_earned(year, term, opener)        - earned credits of certain year and term
#       get_zjd_average(year, term, opener)       - average credits of certain year and term
#       get_kcjd(year, term, opener)              - course credits of certain year and term
#       get_score_detail(cjlcId)                  - detail of course score
#       get_selected_courses(year, term)          - selected courses of certain year and term
#       get_course_table_html(year, term, opener) - html data of course table from jwxt
#   3.Todo:
#       get_course_table(year, term, opener)      - result form table[第几节课][第几周] = 
#                                                   [几节课, 课名, 课室, 第几节到第几节, 第几周到第几周]
#    
#    For detail data of api, please view file data_re.py
# ---------------------------------------------------------------------

def get_hostIP(opener):

    req = data_module.req_get_hostIP
    result = opener.open(req)

    return data_re.find_hostIP(result.read())


def get_student_info(opener):

    req = data_module.req_get_major
    result = opener.open(req)

    return data_re.find_student_info(result.read())


def get_zxf_req(opener):

    stuInfo = get_student_info(opener)
    nj = "'" + stuInfo["nj"] + "'"   # can without '
    zyh = "'" + stuInfo["zyh"] + "'" # must be surrounded by '
    result = opener.open(data_module.req_zxf_req(nj, zyh))

    return data_re.find_zxf_req(result.read())


def get_zxf_earned(year, term, opener):

    sid = get_student_info(opener)["xh"]
    result = opener.open(data_module.req_zxf_earned(sid, year, term))

    return data_re.find_zxf_earned(result.read())


def get_zjd_average(year, term, opener):

    sid = get_student_info(opener)["xh"]
    result = opener.open(data_module.req_zjd_average(sid, year, term))

    return data_re.find_zjd_average(result.read())


def get_kcjd(year, term, opener):

    year = "'" + year + "'" # must be surrounded by '
    term = "'" + term + "'" # can without '
    result = opener.open(data_module.req_kcjd(year, term))

    return data_re.find_kcjd(result.read(), opener)


def get_score_detail(cjlcId, opener):

    result = opener.open(data_module.req_score_detail(cjlcId))

    return data_re.find_score_detail(result.read())


def get_selected_courses(year, term, opener):

    year = "'" + year + "'"
    term = "'" + term + "'"
    result = opener.open(data_module.req_selected_courses(year, term))
    
    return data_re.find_selected_courses(result.read())


def get_course_table_html(year, term, opener):

    result = opener.open(data_module.req_course_table(year, term))

    return data_re.find_course_table_html(result.read())
