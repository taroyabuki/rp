#!/bin/sh
docker run \
-d \
-p 8888:8888 \
-v $(pwd):/home/jovyan/work \
--name jr \
jupyter \
start-notebook.sh \
--NotebookApp.token='password'
