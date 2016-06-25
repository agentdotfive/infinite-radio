
TEST_ENVIRONMENT=".test_environment"
if [ -e "$TEST_ENVIRONMENT" ]; then
    echo "Loading test environment from $TEST_ENVIRONMENT..."
    source "$TEST_ENVIRONMENT"
fi

export PYTHONWARNINGS="ignore::DeprecationWarning:imp"

/usr/bin/env python -m unittest "$@"
