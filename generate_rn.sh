#!/bin/bash

#git_repo=$1
git_repo=https://github.com/SAP/openui5.git
git clone $git_repo
cd openui5

#Showing commits since a given tag/version until now
git log --pretty="%h - %s (%an)" 1.44.16..HEAD
git log --pretty=format:"%h - %an, %ar : %s" --since=1.days
