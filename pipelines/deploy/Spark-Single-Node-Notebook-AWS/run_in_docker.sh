#!/usr/bin/env bash
docker container stop rtdip
docker container rm rtdip
docker system prune -a -f
docker image rm  "rtdip:Dockerfile"
docker build -t "rtdip:Dockerfile" .
docker run --name rtdip --publish 8080:8080 "rtdip:Dockerfile"
