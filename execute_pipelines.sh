#!/bin/bash
poetry run pytest .
cd example_pipeline
poetry run pipeline run
expand -t1 norm.csv | csvlook 