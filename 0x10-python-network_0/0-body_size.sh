#!/bin/bash

# Check if the URL is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send request and retrieve the response headers
headers=$(curl -sI "$1")

# Extract the content length from the response headers
content_length=$(echo "$headers" | awk '/Content-Length/ {print $2}' | tr -d '\r')

# Check if the content length is empty
if [ -z "$content_length" ]; then
  echo "Unable to retrieve content length"
  exit 1
fi

echo "$content_length"