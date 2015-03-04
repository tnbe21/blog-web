#!/bin/bash

PID=`ps a | grep 'python server.py' | grep -v grep | awk '{print $1}'`
if [ -z $PID ]; then
  echo "start blog-web"
  python server.py &
else
  echo "has already started blog-web"
fi
