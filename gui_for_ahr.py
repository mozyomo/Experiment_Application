import PySimpleGUI as sg
from tools import get_prefix
import json

sg.theme('DarkAmber')
layout =[ [sg.Text('開始・終了日時'), sg.InputText(size=(3,1), key = 'month1'), sg.Text('月'), sg.InputText(size=(3,1), key = 'day1'), sg.Text('日'), sg.Text('〜'), sg.InputText(size=(3,1), key = 'month2'), sg.Text('月'), sg.InputText(size=(3,1), key = 'day2'), sg.Text('日') ],
[sg.Text('実験内容(一つ選択)')],
[sg.Button('DNA抽出', key = 'naiyou/DNA抽出'), sg.Button('脂質抽出', key = 'naiyou/脂質抽出'),sg.Button('植菌', key = 'naiyou/植菌')],
[sg.Button('RNA抽出', key = 'naiyou/RNA抽出'), sg.Button('植物植え替え', key = 'naiyou/植物植え替え'), sg.Button('事務作業', key = 'naiyou/事務作業')],
[sg.Button('その他')],
[sg.Text('危険有害要因')],
[sg.Button('ガラスの飛散', key = 'youin/ガラスの飛散'), sg.Button('試薬の飛散', key = 'youin/試薬の飛散'), sg.Button('ガスバーナーからの引火', key = 'youin/ガスバーナーからの引火')],
[sg.Button('過労によるミス', key = 'youin/過労によるミス')],
[sg.Text('対策(一つ選択)')],
[sg.Button('ガラス器具の扱いに注意する', key = 'taisaku/ガラス器具の扱いに注意する'), sg.Button('白衣着用', key = 'taisaku/白衣着用'), sg.Button('ゴーグルの着用', key = 'taisaku/ゴーグルの着用')],
[sg.Button('手袋着用', key = 'taisaku/手袋着用'), sg.Button('火の扱いに注意する', key = 'taisaku/火の扱いに注意する'), sg.Button('適度に休憩を取る', key = 'taisaku/適度に休憩を取る')],
[sg.Text('同伴者')],
[sg.Button('唐司', key = 'coworker/唐司'), sg.Button('周', key = 'coworker/周'), sg.Button('伊藤', key = 'coworker/伊藤'), sg.Button('金谷', key = 'coworker/金谷'), sg.Button('普喜', key = 'coworker/普喜'), sg.Button('渡辺', key = 'coworker/渡辺')],
[sg.Button('打越', key = 'coworker/打越'), sg.Button('福田', key = 'coworker/福田'), sg.Button('保科', key = 'coworker/保科'), sg.Button('三木', key = 'coworker/三木'), sg.Button('堀', key = 'coworker/堀'), sg.Button('井原', key = 'coworker/井原')],
[sg.Button('Push', key = 'push'), sg.Button('初期設定の変更', key = 're_setting')]
]
window = sg.Window("休日実験申請", layout)

dic_for_event = {}

while True:             
    event, values = window.read()
    if event == None:
        dic_for_event["closed"] = True
        break
    else :
        dic_for_event.update(values)
    if event in (sg.Button, 'push'):
        #何もしない.Jsonファイルへ出力されているので、mainで読み取る.
        break
#    elif event is None :
#        dic_for_event["None"] = None
#        break
    else :
        prefix, key = get_prefix(event)
        dic_for_event[prefix] = key

with open("./args/input.json", "w", encoding = "utf-8") as f:
    json.dump(dic_for_event, f, ensure_ascii=False)
window.close()
