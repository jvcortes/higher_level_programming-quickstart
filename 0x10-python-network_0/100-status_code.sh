#!/bin/bash
# curls to an URL and displays the HTTP code of the response
curl -so /dev/null -w "%{http_code}" "$1"
