#!/usr/bin/env bash
set -e
# Run these commands from inside a repository.
git status --short --branch
git branch -avv
git log --graph --oneline --decorate --all
git show --stat --oneline HEAD
git tag -n
git status --porcelain
