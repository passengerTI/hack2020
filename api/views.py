from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

import pymysql
import json
import cgi


db = pymysql.connect("localhost","hack2020","simple7Start","hack2020")

def index(request):

    cursor = db.cursor()
    cursor.execute("SELECT id, areaType, birthday, age FROM passport LIMIT 20")
    rows = cursor.fetchall()

    result = "["

    for row in rows:
      result += "{"
      result += """ "id":"{0}", "areaType":{1}, "birthday":"{2}", "age":{3}""".format(row[0],row[1],row[2],row[3])
      result += "},"
    result += "{}]"

    return HttpResponse(result)

def client(request,clientId):
    cursor = db.cursor()
    cursor.execute("SELECT areaType, birthday, age FROM passport WHERE id like '{0}'".format(clientId))
    rows = cursor.fetchone()

    result = "[{"
    result += """ "areaType":"{0}", "birthday":"{1}", "age":"{2}" """.format(rows[0],rows[1],rows[2])
    result += "}]"

    return HttpResponse(result)


#db.close()
#db2.close()