#!/bin/bash
# 在容器内执行：拉取 rknn_model_zoo → 下载 YOLOv8n ONNX → 转成 RK3576 RKNN
set -e
cd /work

echo "===> [0/4] 校验 onnx 版本（须 <1.16，已在镜像内固定为 1.14.1）"
python3 -c "import onnx; print('onnx', onnx.__version__); assert hasattr(onnx,'mapping'), 'onnx 版本过新，缺 mapping'"

echo "===> [1/4] 准备 rknn_model_zoo"
if [ ! -d rknn_model_zoo ]; then
    git clone --depth 1 https://github.com/airockchip/rknn_model_zoo.git
fi

echo "===> [2/4] 下载 YOLOv8n ONNX"
cd rknn_model_zoo/examples/yolov8/model
if [ ! -f yolov8n.onnx ]; then
    bash download_model.sh
fi
ls -la yolov8n.onnx

echo "===> [3/4] 复制到容器本地 /tmp（避开 QEMU bind-mount 读文件死锁 Errno35）"
cd /work
rm -rf /tmp/mz && cp -r /work/rknn_model_zoo /tmp/mz

echo "===> [4/4] 转换 ONNX → RKNN (target=rk3576, INT8 量化)"
cd /tmp/mz/examples/yolov8/python
# convert.py 用法: convert.py <onnx> <平台> <量化类型 i8/fp> <输出路径>
python3 convert.py ../model/yolov8n.onnx rk3576 i8 ../model/yolov8n_rk3576.rknn

echo "===> 完成，产物拷回挂载目录："
cp ../model/yolov8n_rk3576.rknn /work/yolov8n_rk3576.rknn
ls -la /work/yolov8n_rk3576.rknn
