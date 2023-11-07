#!/bin/bash

if [ $# -eq 0 ]; then
    echo Warning: No namespace provided. Please provide a target namespace.
    exit 1
fi

NAMESPACE=$1

oc project $1

echo "Building application"
tkn pipeline start ci-pipeline \
  -w name=source,volumeClaimTemplateFile=tekton/volume-claim-template.yaml \
  -w name=dockerconfig,secret=quay-push-secret \
  -p ocp-namespace="$NAMESPACE" \
  -p git-url=https://github.com/aushacker/python.git \
  -p git-revision=master \
  -p IMAGE=quay.io/sdavies/fastapi:latest \
  -p CONTEXT=fastapi \
  --use-param-defaults --showlog
