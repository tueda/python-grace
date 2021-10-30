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
release_version=$(poetry version -s)
git commit -a -m "chore(release): bump version to $release_version"
git tag $release_version
poetry version prepatch
dev_version=$(poetry version -s)
git commit -a -m "chore: bump version to $dev_version"

echo "A release tag $release_version was successfully created."
echo "The development version is now $dev_version"
echo "To push it to the origin:"
echo "  git push origin $release_version"
