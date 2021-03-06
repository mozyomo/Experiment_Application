#!/usr/bin/env python
# coding: utf-8
import json
import smtplib

def get_prefix(key) :
    split_list = key.split("/")
    prefix = split_list[0]
    key = split_list[1]

    return prefix, key

def first_time_setting() :
    with open("./args/setting.json", "r", encoding = "utf-8") as fr :
        setting_dic = json.load(fr)
    if setting_dic["counter"] == "False" :
        setting_dic["counter"] = "True"
        setting_dic["name"] = input("名前を入力してください :")
        name = setting_dic["name"]
        setting_dic["gakuseki"] =input("学籍番号を入力してください :")
        setting_dic["tell_num"] =input(f"{name}さんの電話番号を入力してください :")
        setting_dic["mail_add"] =input(f"{name}さんのメールアドレス(mアドレス)を入力してください :")
        setting_dic["gakunen"] = input(f"{name}さんの学年を番号で入力してください(D3:1, D2:2, D1:3, M2:4, M1:5, B4:6, その他:7) :")
        
        with open("./args/setting.json", "w", encoding = "utf-8")as fw :
            json.dump(setting_dic, fw, ensure_ascii=False)
        return None

    else :
        return None

def chenge_setting(key) :
    if key == 're_setting' :
        setting_dic["counter"] = "True"
        setting_dic["name"] = input("名前を入力してください :")
        setting_dic["gakuseki"] =input("学籍番号を入力してください :")
        setting_dic["tell_num"] =input(f"{name}さんの電話番号を入力してください :")
        setting_dic["mail_add"] =input(f"{name}さんのメールアドレス(mアドレス)を入力してください :")
        setting_dic["gakunen"] = input(f"{name}さんの学年を番号で入力してください(D3:1, D2:2, D1:3, M2:4, M1:5, B4:6, その他:7) :")
        with open("./args/setting.json", "w", encoding = "utf-8")as fw :
            json.dump(setting_dic, fw, ensure_ascii=False)
        return None
    else :
        return None

def send_mail(to_who, mail_content) :
    smtp_host = "smtp.gmail.com"
    smtp_port = 465
    username = "ohta.masuda.lab@gmail.com"
    password = "szqpsjnobdthncap" #後で変更
    from_address = "ohta.masuda.lab@gmail.com"
    to_address = to_who
    subject = "Notification for experiments weekend" #日本語表記にすると文字化けが起こるため、件名は英語表記推奨
    body = mail_content
    message = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s" % (from_address, to_address, subject, body))

    smtp = smtplib.SMTP_SSL(smtp_host, smtp_port)
    smtp.login(username, password)
    result = smtp.sendmail(from_address, to_address, message.encode('shift_jis'))
    return None
