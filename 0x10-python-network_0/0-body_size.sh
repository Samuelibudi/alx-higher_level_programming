#!/usr/bin/env bash
# Script to display size of body response from give URL
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
