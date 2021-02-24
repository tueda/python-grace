#!/bin/bash
set -eu
set -o pipefail

# Check if the working repository is clean.
{
  [[ $(git diff --stat) == '' ]] && [[ $(git diff --stat HEAD) == '' ]]
} || {
  echo 'error: working directory is dirty' 1>&2
  exit 1
}

# Determine the next version.
if [[ $# == 0 ]]; then
  next_version=patch
else
  next_version=$1
fi

# Bump the version.
poetry version $next_version
git commit -a -m "chore: bump version to $(poetry version -s)"
git tag $(poetry version -s)
poetry version prepatch
git commit -a -m "chore: bump version to $(poetry version -s)"
