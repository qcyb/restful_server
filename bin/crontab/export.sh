#!/usr/bin/env bash

if [[ "$DEBUG" == "True" || "$DEBUG" == "1" ]]; then
    sleep 360
else
    python /app/src/trade/management/commands/mysql_dump.py -host mysql -P 3306 -u root -p 'root' -db trade -dir '/app/run/backup/'
fi
