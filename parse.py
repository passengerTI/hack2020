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
  print(rownum,end=" ")
  if rownum == 0:
    print(rownum)
    next
  else:
    row = sheet.row_values(rownum)
    cursor.execute("""INSERT INTO sovershen11(id,sex,family,ethnos,national,religion,study,profession,working,pension,work_end_by_ill,diabet,diabet_long,arterial_gipper,arterial_gipper_long,onmk,onmk_dann,infarkt,infarkt_long,heart_failur,heart_failur_long,other_ill,other_ill_long,col24,col25,col26,col27,col28,col29,col30,col31,col32,col33,col34,col35,col36,col37,col38,col39,col40,col41,col42,col43,col44,col45,col46,col47,col48,col49,col50,col51,col52,col53,col54,col55,col56,col57,col58,col59,col60)
    VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}","{9}","{10}","{11}","{12}","{13}","{14}","{15}","{16}","{17}","{18}","{19}","{20}","{21}","{22}","{23}","{24}","{25}","{26}","{27}","{28}","{29}","{30}","{31}","{32}","{33}","{34}","{35}","{36}","{37}","{38}","{39}","{40}","{41}","{42}","{43}","{44}","{45}","{46}","{47}","{48}","{49}","{50}","{51}","{52}","{53}","{54}","{55}","{56}","{57}","{58}","{59}")
    """.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29],row[30],row[31],row[32],row[33],row[34],row[35],row[36],row[37],row[38],row[39],row[40],row[41],row[42],row[43],row[44],row[45],row[46],row[47],row[48],row[49],row[50],row[51],row[52],row[53],row[54],row[55],row[56],row[57],row[58],row[59]))
    #print(row[0])

db.close()