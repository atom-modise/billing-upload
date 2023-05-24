#!/bin/bash

commit_message=$1
branch_name=$2

echo "Äddign new changes"
git add .

echo "Commiting new changes"
git commit -m "$commit_message"

echo "pushing new changes"
git push origin $branch_name

