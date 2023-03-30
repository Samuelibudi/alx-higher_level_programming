#!/bin/bash
# Script that takes URL and sends GET request and displays body response
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
