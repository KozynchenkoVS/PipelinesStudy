#!/bin/bash
echo "This is script to run python, because author lack of knowledge how to not dagit for each file(dagster_project not created with built-in command)"
poetry run dagit -f test_poetry/dagster_project/try_op_job.py
