"""
All views (routes) and associated functions are written here
"""
# import math
# import re
import requests
from flask import render_template
from ccmt2020 import app


@app.route("/", methods=["GET"])
def index():
    """Home Page"""
    return render_template("index.html")


@app.route("/byCollege", methods=["GET"])
def byCollege():
    """College wise"""
    request_url = "https://gist.githubusercontent.com/satish876/adc7164a111ca1c48d4b44ced95c0ad7/raw/84e768e043d9dfe55cd504fc9964b9ae725836ae/ccmt-2020-cutoff-collegewise"  # noqa: E501

    college_stats = requests.get(request_url)  # , params=param_string)
    data = None
    if college_stats.status_code == 200:
        data = [dict(college) for college in college_stats.json()]
    return render_template("displayBook.html", data=data)


@app.route("/byCourse", methods=["GET"])
def byCourse():
    """Course Wise"""

    request_url = "https://gist.githubusercontent.com/satish876/368d98ac3a1f5e7d2de591b0b603098b/raw/4a913917c080409ad7f571b92f7399ca0aaa1f16/ccmt-2020-cutoff-coursewise"  # noqa: E501

    course_stats = requests.get(request_url)  # , params=param_string)
    data = None
    if course_stats.status_code == 200:
        data = dict(course_stats.json())
    return render_template("displayCourse.html", data=data)
