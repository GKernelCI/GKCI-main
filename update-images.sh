#!/bin/env bash
docker pull buildbot/buildbot-master:master
docker pull buildbot/buildbot-worker:master
docker pull nginxproxy/nginx-proxy:alpine
docker pull ubuntu:bionic
docker pull nginx:stable-alpine
docker-compose pull --include-deps
