#!/bin/bash

#set -x # echo on

echo "Local test host, creating local environment."

TEST_ENVIRONMENT=".test_environment"
SAMPLE_TEST_ENVIRONMENT="dev_tools/sample_test_environment"

if [ -e "$TEST_ENVIRONMENT" ]; then
    
    VALID_ENVIRONMENT="`diff -q "$TEST_ENVIRONMENT" "$SAMPLE_TEST_ENVIRONMENT"`"
    if [ -n "$VALID_ENVIRONMENT" ]; then
        
        echo "Local test environment found at $TEST_ENVIRONMENT."
        echo
        
        exit
    else
        
        echo "Local test environment at $TEST_ENVIRONMENT was not modified."
        echo "Edit this file to add your test account information."""
        echo
        
        exit 1
    fi
else

    echo "Local test environment not found, creating sample at $TEST_ENVIRONMENT."
    echo "Edit this file to add your test account information."
    echo

    cp $SAMPLE_TEST_ENVIRONMENT $TEST_ENVIRONMENT

fi
