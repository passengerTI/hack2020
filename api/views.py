from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

import pymysql
import json
import cgi



db = pymysql.connect("localhost","hack2020","simple7Start","hack2020")

cursor = db.cursor()
cursor.execute("SELECT id, areaType, birthday, age FROM passport LIMIT 10")
rows = cursor.fetchall()

result = "["

for row in rows:
  result += "{"
  result += """ "id":"{0}", "areaType":{1}, "birthday":"{2}", "age":{3}
  """.format(row[0],row[1],row[2],row[3])
  result += "},"
result += "{}]"

def index(request):
    return HttpResponse(result)