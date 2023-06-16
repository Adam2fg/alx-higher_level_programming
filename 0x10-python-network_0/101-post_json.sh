#!/bin/bash
# sends a JSON POST request to URL, display body of response
curl -sL -H "content-type:application/json"  -d "$(cat "$2")" "$1"

