#!/bin/bash
# sends a JSON POST request to URL, display body of response
curl -sL -H "content-type:application/json"  -d @"$2" -X POST "$1"

