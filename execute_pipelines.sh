#!/bin/bash
poetry run pytest .
cd example_pipeline
poetry run pipeline run
