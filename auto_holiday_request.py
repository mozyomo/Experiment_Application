#!/usr/bin/env python
# coding: utf-8

import time
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import gui_for_ahr
import json
from tools import first_time_setting, send_mail

json_for_event = open("./args/input.json", "r", encoding = "utf-8")
event_dic = json.load(json_for_event)

if not 're_setting' in event_dic:     
     first_time_setting()
else :
     chenge_setting('re_setting')

json_for_setting = open("./args/setting.json", "r", encoding = "utf-8")
setting_dic = json.load(json_for_setting)
now = datetime.datetime.now()

TO_ADDRESS = "shimojima.m.aa@m.titech.ac.jp"
this_year = '{0:%Y}'.format(now)
this_month = '{0:%m}'.format(now)
this_day = '{0:%d}'.format(now)
month1 = event_dic["month1"]
day1 = event_dic["day1"]
month2 = event_dic["month2"]
day2 = event_dic["day2"]
naiyou = event_dic["naiyou"]
coworker = event_dic["coworker"]
youin = event_dic["youin"]
taisaku = event_dic["taisaku"]

close_key = "closed"
arg = sys.argv[1]

partition = "=" * 30
name = setting_dic["name"]
gakuseki = setting_dic["gakuseki"] 
mail_text = f"申請日:{this_year}年{this_month}月{this_day}日\
      \n氏名:{name} \n 学籍番号:{gakuseki} \n {partition} \
      \n 申請する日時：{month1}月{day1}日 10:00 ~{month2}月{day2}日 22:00\
      \n 作業内容: {naiyou} \n 危険要因: {youin} \n 対策: {taisaku} \n 実験同伴者: {coworker}"
if close_key in event_dic.keys() :
     print("The experiment application tool has been closed. \n The termination process was done correctly.")

else :
     if arg == "None":
          driver =  webdriver.Chrome()
     else :
          driver = webdriver.Chrome(arg)
     website = 'http://www.bio.titech.ac.jp/in/support/night-ex/pdf_form_student.php'
     driver.get(website)
     if (driver.current_url == website):
          Inputs = driver.find_element_by_name('pat1_name') 
          Inputs.send_keys(setting_dic["name"])
          select = Select(driver.find_element_by_name('pat1_shokumei'))
          select.select_by_value(setting_dic["gakunen"])
          Inputs = driver.find_element_by_name('pat1_gakuseki')
          Inputs.send_keys(setting_dic["gakuseki"])
          Inputs = driver.find_element_by_name('pat1_tel1')
          Inputs.send_keys('5527')
          Inputs = driver.find_element_by_name('pat1_tel2')
          Inputs.send_keys(setting_dic["tell_num"])
          Inputs = driver.find_element_by_name('pat1_email1')
          Inputs.send_keys(setting_dic["mail_add"])
          Inputs = driver.find_element_by_name('pat1_email2')
          Inputs.send_keys(setting_dic["mail_add"])
          Inputs = driver.find_element_by_name('rep_name')
          Inputs.send_keys('太田啓之')
          Inputs = driver.find_element_by_name('rep_tel')
          Inputs.send_keys('090-7422-1920')
          Inputs = driver.find_element_by_name('rep_email1')
          Inputs.send_keys('ohta.h.ab@m.titech.ac.jp')
          Inputs = driver.find_element_by_name('rep_email2')
          Inputs.send_keys('ohta.h.ab@m.titech.ac.jp')
          Inputs = driver.find_element_by_name('exp_date_y')
          Inputs.send_keys('{0:%Y}'.format(now))
          Inputs = driver.find_element_by_name('exp_date_m')
          Inputs.send_keys('{0:%m}'.format(now))
          Inputs = driver.find_element_by_name('exp_date_d')
          Inputs.send_keys('{0:%d}'.format(now))
          Inputs = driver.find_element_by_name('pat1_name') 
          Inputs = driver.find_element_by_name('pat1_day1')
          Inputs.send_keys(f"{month1}月{day1}日 10:00 ~ {month2}月{day2}日 22:00")
          Inputs = driver.find_element_by_name('pat1_place')
          Inputs.send_keys('B1B2棟331, 326号室') 
          Inputs = driver.find_element_by_name('pat1_naiyo')
          Inputs.send_keys(f"{naiyou}, 同伴者： {coworker}") 
          Inputs = driver.find_element_by_name('risk1_name')
          Inputs.send_keys(naiyou)
          Inputs = driver.find_element_by_name('risk1_youin')
          Inputs.send_keys(youin) 
          Inputs = driver.find_element_by_name('risk1_taisaku')
          Inputs.send_keys(taisaku) 
     print('Text input is complete.')                                                      #errorなく動作すると、cmdに「テキスト入力完了」と表示される
     #send_mail(TO_ADDRESS, mail_text)
     print(mail_text)

