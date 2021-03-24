#!/bin/sh
brew install python
pip --proxy:http://proxy.noc.titech.ac.jp:3128 install --upgrade pip
pip --proxy:http://proxy.noc.titech.ac.jp:3128 install -r ../requirements.txt
python ../auto_holiday_request.py ./driver/mac/chromedriver