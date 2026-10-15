#!/usr/bin/env bash
set -e
git clone https://github.com/octocat/Hello-World.git upstream-inspection
cd upstream-inspection
git rev-parse --is-inside-work-tree
git remote -v
git branch -a
git log --oneline --decorate -10
git log --graph --oneline --decorate --all
git show --stat --oneline HEAD
git status --short --branch
# Inspection only: do not push or modify this upstream clone.
