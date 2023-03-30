#!/bin/bash
# Script that takes URL, sends a POST request to be passed and displays body response.
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
