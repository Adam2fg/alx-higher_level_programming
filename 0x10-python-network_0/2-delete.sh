#!/bin/bash
# sends a DELETE request to the URL passed as first arg and display response body
curl -s "$1" -X DELETE
