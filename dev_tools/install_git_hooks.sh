#!/bin/bash
set -x # echo on
GIT_ROOT="`git rev-parse --show-toplevel`"
ln -s "$GIT_ROOT"/dev_tools/git_hooks/pre-commit "$GIT_ROOT"/.git/hooks
