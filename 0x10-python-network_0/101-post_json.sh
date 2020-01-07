#!/bin/bash
# curls to an URL using a JSON POST HTTP request
curl -sH "Content-Type: application/json" --data "$(< "$2")" "$1"
