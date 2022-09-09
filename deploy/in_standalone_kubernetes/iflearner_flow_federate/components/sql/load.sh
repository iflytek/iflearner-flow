#!/bin/bash
set -e

mysql -uroot -P3306 -pflow_federate@123 -e "source /home/init.sql;"