#!/bin/bash

registry_url="harbor.freedom.org"
registry_project="freedom"
image="$registry_url"/"$registry_project"/common-centos7:latest

docker build -t $image .
docker push $image