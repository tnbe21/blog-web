#!/bin/sh

initFile=${1}
pass=${2}
. ./env/bin/activate
nohup pserve ${initFile} --reload pass=${pass} >out.log 2>err.log &
