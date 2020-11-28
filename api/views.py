from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import JsonResponse

import pymysql
import json
import cgi
import random


db = pymysql.connect("localhost","hack2020","simple7Start","hack2020")

def index(request):
    # req from DB list of clients
    cursor = db.cursor()
    cursor.execute("SELECT id, areaType, birthday, age FROM passport LIMIT 20")
    rows = cursor.fetchall()

    # generate draft json fromat
    result = "["
    for row in rows:
      result += "{"
      result += """ "id":"{0}", "areaType":{1}, "birthday":"{2}", "age":{3}""".format(row[0],row[1],row[2],row[3])
      result += "},"
    result += "{}]"

    return HttpResponse(result)

def client(request,clientId):
    # req info about client by id

    gipertenziya = str(random.randint(0,90))
    onmk = str(random.randint(0,90))
    infarkt = str(random.randint(0,90))
    heart_failure = str(random.randint(0,90))
    other_ill = str(random.randint(0,90))

    cursor = db.cursor()
    cursor.execute("""
      SELECT
        p.areaType,
        p.birthday,
        p.age,
        s1.sex,
        s1.family,
        s1.ethnos,
        s1.national,
        s1.religion,
        s1.study,
        s1.profession,
        s1.working,
        s1.pension,
        s1.work_end_by_ill,
        s1.diabet,
        s1.diabet_long,
        s1.arterial_gipper
      FROM
        passport p,
        sovershen1 s1
      WHERE
        p.id like '{0}'
        AND s1.id like '{0}'
    """.format(clientId))
    rows = cursor.fetchone()

    # genereate draft json format
    result = "{"
    result += """
	"areaType":"{0}",
	"birthday":"{1}",
	"age":"{2}",
	"sex":"{3}",
	"family":"{4}",
	"ethnos":"{5}",
        "national":"{6}",
        "religion":"{7}",
        "study":"{8}",
        "profession":"{9}",
        "working":"{10}",
        "pension":"{11}",
        "work_end_by_ill":"{12}",
        "diabet":"{13}",
	"diabet_long":"{14}",
	"arterial_gipper":"{15}",
	"id":"{16}",
	"gipertenziya":{17},
	"onmk":{18},
	"infarkt":{19},
	"heart_failure":{20},
	"other_ill":{21}
	""".format(rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7],rows[8],rows[9],rows[10],rows[11],rows[12],rows[13],rows[14],rows[15],clientId,gipertenziya,onmk,infarkt,heart_failure,other_ill)
    result += "}"

    return HttpResponse(result)


#db.close()
#db2.close()