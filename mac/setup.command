#!/bin/sh
cd `dirname $0`
pip3 install --upgrade pip3
pip3 install --proxy http://proxy.noc.titech.ac.jp:3128  --update pip3
pip3 install --proxy http://proxy.noc.titech.ac.jp:3128 -r ../requirements.txt
chmod u+x ../auto_holiday_request.py
python3 ../auto_holiday_request.py