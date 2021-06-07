# Experiment_Application
本アプリケーションは、休日実験申請を部分的に自動化する目的で作成されたものです。
専用のGUIを通して休日実験申請を行うことができます。

# 必須環境
| 項目        | 内容                             | 
| :---------: | :------------------------------: | 
| 対応OS      | Windows/Linux(Mac版は未実装)     | 
| 必要環境    | python3(python3.7以降で動作確認) | 
| 対応browser | chrome, firefox                  | 
※まれに、chromedriverのversionに問題があり、互換性がないとエラーが表示される場合があります。その場合は、対応するversionを確認し、driverディレクトリ配下に新しいchromedriverを配置してください。

# 起動方法
1. githubより、本アプリケーションをダウンロードしてください。
```
# gitの場合
$ git clone [repository_name]
```
2. pythonがPCにインストールされていない場合は、以下のURLからpython3.9.2をインストールしてください。(必ず、ADD Python3.9 to PATHにチェックを入れること)

3. zipファイルをダウンロードした場合は解凍し、set_upという名前のファイルをダブルクリックする。(必須モジュールのインストールがメインなので、初回のみクリック)
4. GUIが起動するので、日付、実験内容、危険要因、同伴者等の情報を入力し、Pushを押す。
5. コマンドプロンプト(黒い画面)が起動するので、氏名、学籍番号、電話番号、メールアドレス、学年などの情報を入力する(初回のみ)
6. しばらく待つと、web browserが開き、自動で入力が始まるので、入力が終了したら"確認する"をクリックする。
7. 次回以降の始動には、run.batファイルを使用してください。(set_up.batでも起動はしますが、時間がかかりますので非推奨です)

# トラブルシューティング
## 氏名入力を間違えてしまった/名前が文字化けしている
argsディレクトリ配下のsetting.jsonを開き、"name"の項目を書き換えてください。もしくは、GUI画面の"初期設定"ボタンを押し、初期設定をやり直してください。
## browserが開かない
chromedriverの互換性に問題がある可能性があります。driverを再インストールし、driverディレクトリ配下においてください。
## browserは開くが、画面が真っ白
tokyo techのproxy設定がなされていない。もしくは学外ネットワークから操作している可能性があります。ネットワーク設定を確認してください。 
## システムに接続されているデバイスが機能していませんという警告文が表示されている
chromedriverがUSB接続端末を確認する際、省エネルギーモードであった場合に表示される警告文です。起動には影響しませんので、そのままコマンドプロンプトを閉じていただいて問題ありません。 
## 記号が文字化けすると連絡があった。
windowsが採用している文字コードとDBが採用している文字コードが異なるために発生する問題です。
下記問い合わせ先にご連絡ください。
# 問い合わせ
普喜　幹  
motoki619@gmail.com
