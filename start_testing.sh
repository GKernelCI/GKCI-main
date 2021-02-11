#!/bin/bash
cp kernelci-ci-gkernelci.json.example GBuildbot-worker/.kernelci-ci-gkernelci.json
python sparser.py
docker-compose up -d
