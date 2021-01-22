#!/bin/bash
cp kernelci-ci-gkernelci.json.example GBuildbot-worker/.kernelci-ci-gkernelci.json
docker-compose up -d
