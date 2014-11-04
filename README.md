SYSU-JWXT-API
=============

api for educational administration system of my school, created with python, provided for personal learning only

### API list

  Student & Login Info

    get_hostIP(opener)           - login host IP address
    get_student_info(opener)     - student detail information
                                                                                                 
  Credit
   
    get_zxf_req(opener)                       - request credits in all
    get_zxf_earned(year, term, opener)        - earned credits of certain year and term
    get_zjd_average(year, term, opener)       - average credits of certain year and term
    get_kcjd(year, term, opener)              - course credits of certain year and term
    
  Course
  
    get_score_detail(cjlcId)                  - detail of course score
    get_selected_courses(year, term)          - selected courses of certain year and term
    get_course_table_html(year, term, opener) - html data of course table from jwxt
   
### Todo

    get_course_table(year, term, opener)      - result form table[第几节课][第几周] = 
                                               [几节课, 课名, 课室, 第几节到第几节, 第几周到第几周]
