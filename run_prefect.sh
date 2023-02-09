#!/bin/bash
pathToProject="test_poetry/prefect_project"
cd $pathToProject
for i in *
do
    echo "Launching $i"
    poetry run python $i
done
