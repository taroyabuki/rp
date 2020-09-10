#!/bin/sh
docker run \
-d \
-e PASSWORD=password \
-e ROOT=TRUE \
-p 8787:8787 \
-v $(PWD):/home/rstudio \
--name rs \
taroyabuki/rstudio
