#!/bin/bash
# takes in URL and display all HTTP methods the server accepts
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
