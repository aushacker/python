#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Warning: No project provided. Please provide a target project name."
    exit 1
fi

NAMESPACE=$1

oc new-project $NAMESPACE

oc apply -f ./tekton/ci-pipeline.yaml
