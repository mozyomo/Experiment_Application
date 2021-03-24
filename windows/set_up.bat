@echo off
cd /d %~dp0
python -m pip --proxy=http://proxy.noc.titech.ac.jp:3128 install --upgrade pip
pip --proxy=http://proxy.noc.titech.ac.jp:3128 install -r ../requirements.txt
@py.exe ../auto_holiday_request.py "./driver/chromedriver.exe" %*
