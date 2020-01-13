#!/bin/bash
time grep -E '^(\([0-9]{3}\) [0-9]{3}-[0-9]{4}|[0-9]{3}-[0-9]{3}-[0-9]{4})$' file.txt
echo
time egrep -x '(\([0-9]{3}\) [0-9]{3}\-[0-9]{4}|[0-9]{3}\-([0-9]){3}\-[0-9]{4})' file.txt
echo
time awk '/^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$|^[0-9]{3}-[0-9]{3}-[0-9]{4}$/' file.txt