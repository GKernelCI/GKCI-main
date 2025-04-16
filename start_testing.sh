#!/bin/bash
cp kernelci-ci-gkernelci.json.example GBuildbot-worker/.kernelci-ci-gkernelci.json
sed -i "s/your local docker GID/$(cat /etc/group | grep docker | cut -d: -f3)/" docker-compose.yml.template
python sparser.py || exit $?
docker compose up -d
