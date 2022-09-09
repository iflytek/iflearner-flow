#!/bin/bash
set -e

mysql -uroot -P3306 -pflow_server@123 -e "source /home/init.sql;"