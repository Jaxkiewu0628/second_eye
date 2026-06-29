class Detection {
  final String label;
  final double confidence;
  final double x, y, w, h; // normalized 0-1
  final int frameW, frameH;

  const Detection({
    required this.label,
    required this.confidence,
    required this.x,
    required this.y,
    required this.w,
    required this.h,
    required this.frameW,
    required this.frameH,
  });

  factory Detection.fromJson(Map<String, dynamic> j) => Detection(
        label: j['label'] as String,
        confidence: (j['conf'] as num).toDouble(),
        x: (j['x'] as num).toDouble(),
        y: (j['y'] as num).toDouble(),
        w: (j['w'] as num).toDouble(),
        h: (j['h'] as num).toDouble(),
        frameW: (j['fw'] as num? ?? 640).toInt(),
        frameH: (j['fh'] as num? ?? 480).toInt(),
      );
}
