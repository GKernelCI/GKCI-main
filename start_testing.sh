#!/bin/bash
cp kernelci-ci-gkernelci.json.example GBuildbot-worker/.kernelci-ci-gkernelci.json
python sparser.py || exit $?
docker-compose up -d
