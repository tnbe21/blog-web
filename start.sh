#!/bin/sh

envMode=${1}
pass=${2}
. ./env/bin/activate
./env/bin/pserve ${envMode}.ini --reload pass=${pass}
