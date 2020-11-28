#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import xlrd
import pymysql
import sys

db = pymysql.connect("localhost","hack2020","simple7Start","hack2020")

rb = xlrd.open_workbook('base.xls',formatting_info=True)
sheet_names = rb.sheet_names()
print(sheet_names)

sheet = rb.sheet_by_index(1)

cursor = db.cursor()
cursor.execute("TRUNCATE sovershen11")

print(sheet.ncols)
for rownum in range(sheet.nrows):
  print(rownum)
  if rownum == 0:
    print(rownum)
    next
  else:
    row = sheet.row_values(rownum)
    cursor.execute("""INSERT INTO sovershen11(id,sex,family,ethnos,national,religion,study,profession,working,pension,work_end_by_ill,diabet,diabet_long,arterial_gipper,col15,col16,col17,col18,col19,col20,col21,col22,col23,col24,col25,col26,col27,col28,col29,col30)
    VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}","{9}","{10}","{11}","{12}","{13}","{14}","{15}","{16}","{17}","{18}","{19}","{20}","{21}","{22}","{23}","{24}","{25}","{26}","{27}","{28}","{29}")
    """.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29]))
    #print(row[0])

db.close()