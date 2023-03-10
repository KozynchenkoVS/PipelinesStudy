#!/bin/bash
poetry run pytest .
cd example_pipeline
poetry run pipeline run
cat norm.csv | perl -pe 's/((?<=,)|(?<=^)),/ ,/g;' | column -t -s, | less -S