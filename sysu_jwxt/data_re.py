# -*- coding: UTF-8 -*-   
import re
import api

# ------------------------------
# Credits Structure in data
#   
#    var iaddress = '172.18.35.80';
#
# ------------------------------
def find_hostIP(data):

    return re.search(r'(?<=iaddress).*?\'(?P<IP>.*?)\'', data).group("IP")


# ------------------------------
# Credits Structure in data
#
#    "oneColumn":"公必(学分|平均绩点)","twoColumn":"33.0"
#    "oneColumn":"专必(学分|平均绩点)","twoColumn":"89.0"
#    "oneColumn":"专选(学分|平均绩点)","twoColumn":"24.0"
#    "oneColumn":"公选(学分|平均绩点)","twoColumn":"16.0"
#
# ------------------------------
def find_zxf_req(data):

    return find_xf(data)


def find_zxf_earned(data):

    return find_xf(data)


def find_zjd_average(data):

    return find_xf(data)


def find_xf(data):

    result = []
    patterns = ["公必", "专必", "公选", "专选"]

    for pattern in patterns:
        regexp = pattern + ".*?(\d+\.*\d*)"
        match = re.search(regexp, data)
        result.append(("0.0" if not match else match.group(1)))

    return result  # [gbxf, zbxf, gxxf, zxxf] xf can also be jd(pjjd)


# ------------------------------
#  Course Structure
#  {
#      "xnd":"2013-2014",
#      "xq":"2",
#      "kcywmc":"Database and  Application",
#      "xs":"36.0",
#      "jxbh":"19000154133003",
#      
#       useful attributes
#     ---------------------
#      "cjlcId":"1231231",    // parameter for score detail
#      "kcmc":"数据库应用",
#      "jsxm":"罗志高",
#      "xf":"2.0",
#      "zzcj":"92",
#      "jd":"4.2",
#      "jxbpm":"12\/38",
#     ---------------------
#  }
# ------------------------------
def find_kcjd(data, opener):

    regexp_firstattr = r'primary:\[{"(.*?)"'
    match_firstattr = re.search(regexp_firstattr, data)

    if match_firstattr:
        firstattr = match_firstattr.group(1)
    else:
        return []

    courses = []
    regexp_course = '{"' + firstattr + '".*?}'
    patterns = ["kcmc", "jsxm", "xf", "zzcj", "jd", "jxbpm", "xnd", "xq", "jxbh", "cjlcId"]

    for match_course in re.findall(regexp_course, data):
        course = {}

        for pattern in patterns:
            regex_attr = '(?<=' + pattern + '":").*?' + '(?=")'
            attr = re.search(regex_attr, match_course)
            course[pattern] = ("" if not attr else attr.group())

        course["jxbpm"] = course["jxbpm"].replace("\\", "")
        course["score_detail"] = api.get_score_detail(course["cjlcId"], opener)

        courses.append(course)
    
    return courses  # [{course1},  {course2}, {course3}, ...]


# ------------------------------
#  Student Infomation Struct
#  {
#      "ksh":"考生号",
#      "lxdh":"联系电话",
#       ...
#
#       useful attributes
#     ---------------------
#      "xm":"姓名",
#      "nj":"年级",
#      "xh":"学号",
#      "xymc":"学院名称",
#      "bjmc":"班级名称",
#      "zyfxmc":"专业方向名称",
#      "xmpy":"姓名拼音",
#     ---------------------
#  }
# ------------------------------
def find_student_info(data):

    stuInfo = {}
    patterns = [
        "xm", "zyh", "nj", "xh", "bjmc",
        "xymc", "byxx", "lxdh", "ksh", "rxny",
        "hkszd", "txdz", "xmpy", "zyfxmc", "njmc"
    ]

    for pattern in patterns:
        stuInfo[pattern] = re.search(pattern + '":"(.*?)"', data).group(1)

    return stuInfo


# ------------------------------
#  Course Score Details Struct
#  {
#      "fxyscj":"70",   // when course is PE, 1000m result will be "fxyscj":"3\'33\""
#      "xh":"12222222",
#       ...
#
#       useful attributes
#     ---------------------
#      "mrqz":"40",
#      "fxcj":"70",
#      "fxmc":"平时成绩"
#     ---------------------
#  }
# ------------------------------
def find_score_detail(data):

    details = []
    main = re.search(r'primary:.*?]}', data).group()

    items_regexp = r'{.*?}'
    patterns = ["fxmc", "mrqz", "fxcj"]

    for items_match in re.findall(items_regexp, main):
        detail = []
        for pattern in patterns:
            regexp = pattern + '":"(.*?)"'
            detail.append(re.search(regexp, items_match).group())
        details.append(detail)
        
    return details


def find_selected_courses(data):
    
    courses = []
    patterns = ["jxbh", "kcmc", "xf", "xm", "sksjdd", "xnd", "xq"]
    item_regexp = r'primary.*?]'
    unit = re.findall(r'{.*?}', re.search(item_regexp, data).group())

    for item_match in unit:
        course = {}

        for pattern in patterns:
            regexp = pattern + '":"(.*?)"'
            match = re.search(regexp, item_match)
            course[pattern] = ("" if not match else match.group(1))
        course["sksjdd"] = course["sksjdd"].replace("\\", "")

        courses.append(course)

    return courses


def find_course_table_html(data):

    regexp = r'<table.*?</table>'
    table = re.search(regexp, data).group()

    return table  # format: <table ...> ... </table>

# result form table[第几节课][第几周] = [几节课, 课名, 课室, 第几节到第几节, 第几周到第几周]
#def find_course_table(data):
#    print data
#    table = {}
#    for i in range(1, 16):
#
#        regexp_day = r'第' + str(i) + '节.*?(<td.*?>(.*?)</td>)*</tr>'
#        regexp_class = r'<td.*?td>'
#        match_day = re.search(regexp_day, data).group()
#        print match_day
#        match_class = re.findall(regexp_class, match_day)
#        table_classid = [[],]
#
#        for class_ in match_class:
#            print class_
#            class_attr = []
#            regexp = r'rowspan=(\d+).*?>(.*?)<br>(.*?)<br>(.*)<br>(.*)</td>'
#            match = re.search(regexp, class_)
#
#            if match:
#                for attr_id in range(1, 6):
#                    print match.group()
#                    # five group: length, name, address, during, week
#                    class_attr.append(match.group(attr_id))
#            table_classid.append(class_attr)
#
#        table[i] = table_classid
#
#    return table  
