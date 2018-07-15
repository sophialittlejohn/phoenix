#!/bin/bash
set -e

coverage run ./manage.py test --noinput

# Grab the coverage for gitlab: use "TOTAL:\s+\d+\%" in the gitlab-ci-settings
LOG=$(mktemp)
coverage report -m  2>&1 >$LOG
cat $LOG
grep TOTAL $LOG | awk '{ print "TOTAL: "$4; }'
rm $LOG

coverage html
chmod 777 -R local_coverage_report/
