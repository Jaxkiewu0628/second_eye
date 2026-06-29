#!/bin/bash
# 宿主机驱动：脚本经 stdin 喂入容器（不用 bind-mount），产物用 docker cp 取出。
set -e
cd "$(dirname "$0")"

docker rm -f rknnconv 2>/dev/null || true

echo "===> 启动容器转换（无挂载目录，规避 QEMU 死锁）"
docker run -i --name rknnconv --platform linux/amd64 rknn-rk3576 bash -s < container_convert.sh

echo "===> 取出 RKNN 产物到宿主机"
docker cp rknnconv:/build/yolov8n_rk3576.rknn ./yolov8n_rk3576.rknn
docker rm -f rknnconv >/dev/null

echo "===> DONE:"
ls -la ./yolov8n_rk3576.rknn
