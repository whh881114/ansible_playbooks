#!/bin/bash

registry_url="harbor.freedom.org"
registry_project="freedom"
image="$registry_url"/"$registry_project"/jenkins-centos7:2.319.1-1.1

docker build -t $image .
docker push $image