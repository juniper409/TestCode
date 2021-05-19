#!/usr/bin/env bash

git add *
echo "Committ Message: "
read message
git commit -m " $message"
git push --all
