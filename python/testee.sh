#!/bin/bash

DIALOG=${DIALOG=dialog}
tempfile=`tempfile 2>/dev/null` || tempfile=/tmp/test$$
trap "rm -f $tempfile" 0 1 2 5 15

$DIALOG --title "LOGIN" --clear \
--inputbox "Usuario: " 16 51 2> $tempfile


retval=$?

case $retval in
0)
echo "Usuario digitado `cat $tempfile`";;
1)
echo "Login cancelado.";;
255)
if test -s $tempfile ; then
cat $tempfile
else
echo "ESC pressionado."
fi
;;
esac


[]s
