#!/bin/bash
# takes in URL, sends a request to that URL and displays the size of the response body
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2

