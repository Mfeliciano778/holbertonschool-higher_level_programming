#!/bin/bash
# gets body size of url
curl -s "$1" | wc -c
