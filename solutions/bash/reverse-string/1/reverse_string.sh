#!/usr/bin/env bash

if [ "$1" == ""  ]; then
    echo ""
else   
     var="$1"
    rav=$(echo "$var" | rev)
    echo "$rav"
fi

