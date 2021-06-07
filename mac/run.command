#!/bin/sh
cd `dirname $0`
chmod u+x run.command
python3 ../auto_holiday_request.py "../driver/mac/chromedriver"