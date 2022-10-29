#!/bin/sh
docker build -t ams-eflow-energymix-reader .
docker tag ams-eflow-energymix-reader:latest 768867912825.dkr.ecr.eu-central-1.amazonaws.com/ams-eflow-energymix-reader:latest
docker push 768867912825.dkr.ecr.eu-central-1.amazonaws.com/ams-eflow-energymix-reader:latest