# RK3576 YOLOv8 转换环境 —— x86_64（RKNN-Toolkit2 只支持 x86 Linux）
# 在 arm64 Mac 上通过 QEMU 模拟运行，仅用于一次性模型转换。
FROM --platform=linux/amd64 ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 python3-pip git wget ca-certificates \
        libgl1 libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 用清华 PyPI 镜像（国内直连 pythonhosted 会超时）+ 加长超时
RUN pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip3 config set global.timeout 120
# RKNN-Toolkit2 2.x 才支持 RK3576（V1.6.0 不支持）
RUN pip3 install --no-cache-dir --retries 8 rknn-toolkit2
# rknn-toolkit2 2.3.2 会拉入新版 onnx，但它需要 onnx<1.16（否则缺 onnx.mapping）
RUN pip3 install --no-cache-dir --retries 8 "onnx==1.14.1"

WORKDIR /work
