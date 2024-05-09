#!/bin/bash

# Check if commit message is provided as an argument
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <commit_message>"
  exit 1
fi

# Make files executable
chmod u+x *.sh

# Commit message
commit_message="$1"

# Add all changes to the staging area
git add .

# Commit changes with the provided commit message
git commit -m "$commit_message"

# Push changes to the remote repository
git push
