#!/bin/bash
# 在容器内执行（通过 stdin 喂入，不读任何挂载目录）。全部在容器本地 /build 完成。
set -e

echo "===> onnx 版本校验"
python3 -c "import onnx; print('onnx', onnx.__version__, '| has mapping:', hasattr(onnx,'mapping'))"

mkdir -p /build && cd /build

echo "===> [1/3] 克隆 rknn_model_zoo（容器本地）"
git clone --depth 1 https://github.com/airockchip/rknn_model_zoo.git

echo "===> [2/3] 下载 YOLOv8n ONNX"
cd rknn_model_zoo/examples/yolov8/model
bash download_model.sh
ls -la yolov8n.onnx

echo "===> [3/3] 转换 ONNX → RKNN (target=rk3576, INT8 量化)"
cd ../python
python3 convert.py ../model/yolov8n.onnx rk3576 i8 ../model/yolov8n_rk3576.rknn

cp ../model/yolov8n_rk3576.rknn /build/yolov8n_rk3576.rknn
echo "===> 容器内完成："
ls -la /build/yolov8n_rk3576.rknn
