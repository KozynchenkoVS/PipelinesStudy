#!/bin/bash
echo "This is script to run python, because author lack of knowledge how to not dagit for each file(dagster_project not created with built-in command)"
cd "test_poetry/dagster_project"
poetry run dagit -f try_op_job.py
