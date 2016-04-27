#!/bin/bash
set -x # echo on
GIT_ROOT="`git rev-parse --show-toplevel`"
ln -s "$GIT_ROOT"/dev-tools/git_hooks/* "$GIT_ROOT"/.git/hooks
