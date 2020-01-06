#!/bin/bash
# curls to an URL through a HTTP request with a custome header
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
