#!/bin/bash
# sends a request to URL, display response status code only
curl -s -o /dev/null -w "%{http_code}" "$1"

