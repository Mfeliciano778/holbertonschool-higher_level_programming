#!/bin/bash
# displays all methods of url
curl -sI | grep "Allow:" | cut -d" " l-f 2-11
