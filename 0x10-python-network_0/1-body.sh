#!/bin/bash
# takes in URL, sends a GET request to URL and display body of response
curl -sfL "$1" -X GET
