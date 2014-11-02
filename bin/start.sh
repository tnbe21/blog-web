#!/bin/bash

PID=`ps a | grep blog.tnbe21.env | grep -v grep | awk '{print $1}'`
if [ -z $PID ]
then
  echo "start blog-web"
  ~/bin/python/blog.tnbe21.env/bin/python server.py &
else
  echo "has already started blog-web"
fi
