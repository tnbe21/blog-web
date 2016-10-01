#!/bin/sh

initFile=${1}
mysql_pass=${2}
admin_root_path=${3}
. ./env/bin/activate
nohup pserve ${initFile} --reload mysql_pass=${2} admin_root_path=${3} >out.log 2>err.log &
