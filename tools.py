import json

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
