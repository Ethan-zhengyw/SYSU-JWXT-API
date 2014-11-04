#-*-coding: utf-8-*-
import sysu_jwxt.data_module as data_module
import sysu_jwxt.api as api

def menu():
    print " -------------------------------------------------------------"
    print "             commands:                                "
    print "                      q 0 - quit"
    print "                      h 1 - print this menu            "
    print "                   info 2 - student informations       "
    print "                                                       "
    print "                  cre_r 3 - credits request            "
    print "                  cre_e 4 - credits earned             "
    print "                  cre_a 5 - average credits            "
    print "                     kc 6 - course selected            "
    print "                  kc_jd 7 - course score               "
    print " -------------------------------------------------------------\n"


def execute(op, opener):
    if op == "1" or op == "h":
        menu()
    elif op == "2" or op == "info":
        info(opener)
    elif op == "3" or op == "cre_r":
        cre_r(opener)
    elif op == "4" or op == "cre_e":
        cre_e(opener)
    elif op == "5" or op == "cre_a":
        cre_a(opener)
    elif op == "6" or op == "kc":
        kc(opener)
    elif op == "7" or op == "kc_jd":
        kc_jd(opener)
    else:
        print " [Command Error!]\n"


def viewall(opener):
    print " Student information\n#-----------------------------"
    print " Host IP: " + "\t" + api.get_hostIP(opener)
    stuInfo = api.get_student_info(opener)
    for attr in stuInfo:
        print " " + attr + ": " + "\t" + stuInfo[attr]
    print

    print " All Credits Request\n#-----------------------------"
    print "", print_with_attr(api.get_zxf_req(opener)), "\n"

    print " All Credits Earned\n#-----------------------------"
    print "", print_with_attr(api.get_zxf_earned("", "", opener)), "\n"

    print " Average GPA of All courses \n#-----------------------------"
    print "", print_with_attr(api.get_zjd_average("", "", opener)), "\n"


def cre_r(opener):
    print " All Credits Request\n#-----------------------------"
    print "", print_with_attr(api.get_zxf_req(opener)), "\n"


def cre_e(opener):
    print " All Credits Earned\n#-----------------------------"
    year = raw_input(" Year(xxxx-xxxx): ")
    term = raw_input(" Term(1|2|3): ")
    print "", print_with_attr(api.get_zxf_earned(year, term, opener)), "\n"


def cre_a(opener):
    print " Average GPA of All courses \n#-----------------------------"
    year = raw_input(" Year(xxxx-xxxx): ")
    term = raw_input(" Term(1|2|3): ")
    print "", print_with_attr(api.get_zjd_average(year, term, opener)), "\n"


def kc(opener):
    print " Courses Selected\n#-----------------------------"
    year = raw_input(" Year(2012-2013): ")
    term = raw_input(" Term(1|2|3): ")
    years = ["2009-2010", "2010-2011", "2011-2012", "2012-2013", "2013-2014", "2014-2015"]
    terms = ["1", "2", "3"]
    if year != "":
        year = years
    if term != "":
        term = terms
    for year in years:
        for term in terms:
            courses = api.get_selected_courses(year, term, opener)
            count = 0
            if len(courses):
                print "\n [" + year, term + "]\n#-----------------------------"
            for course in courses:
                count = count + 1
                print " " + str(count) + "\t",
                for attr in ["kcmc", "xm"]:
                    print course[attr] + "\t",
                print
    print


def kc_jd(opener):
    print " Courses Score\n#-----------------------------"
    year = raw_input(" Year(2012-2013): ")
    term = raw_input(" Term(1|2|3): ")
    years = ["2009-2010", "2010-2011", "2011-2012", "2012-2013", "2013-2014", "2014-2015"]
    terms = ["1", "2", "3"]
    if year != "":
        years = [year]
    if term != "":
        terms = [term]
    for year in years:
        for term in terms:
            kcjd = api.get_kcjd(year, term, opener)
            if not len(kcjd):
                break
            print " [" + year + " " + term + "]\n#-----------------------------"
            for a in kcjd:
                for b in a:
                    if b == "score_detail":
                        print " " + b + ":"
                        for l in a[b]:
                            print "\t[",
                            for x in l:
                                print x,
                            print "]"
                    else:
                        print b + ": \t", a[b]
                print


def info(opener):
    print " Student information\n#-----------------------------"
    print " Host IP: " + "\t" + api.get_hostIP(opener)
    stuInfo = api.get_student_info(opener)
    for attr in stuInfo:
        print " " + attr + ": " + "\t" + stuInfo[attr]
    print


def print_with_attr(result):
    stream = '[公必: ' + result[0] + ', 专必: ' + result[1] + ', 公选: ' + result[2] + ', 专选: ' + result[3] + ']'
    return stream

def detail_year_term():
    print "\n#-----------------------------------"
    earned = api.get_zxf_earned(year, term, opener)
    gpa = api.get_zjd_average(year, term, opener)
    print earned, "\t", gpa, 
