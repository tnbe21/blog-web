#!/bin/bash

PID=`ps a | grep blog.tnbe21.env | grep -v grep | awk '{print $1}'`
if [ $PID ]
then
  echo "stop blog-web"
  kill $PID
else
  echo "has no blog-web process"
fi
