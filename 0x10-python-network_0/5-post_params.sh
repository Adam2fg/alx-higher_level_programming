#!/bin/bash
# takes in URL, sends POST request to URL, display body of response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

