#!/usr/bin/env bash
# Script to display size of body response from give URL
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
