enum ConnectionState { disconnected, scanning, connecting, connected }
enum DetectionMode { off, yolov5, face }

class DeviceState {
  final ConnectionState connection;
  final String? deviceName;
  final String? deviceIp;
  final int batteryPct;
  final DetectionMode detectionMode;
  final bool rtspActive;
  final int fps;

  const DeviceState({
    this.connection = ConnectionState.disconnected,
    this.deviceName,
    this.deviceIp,
    this.batteryPct = 0,
    this.detectionMode = DetectionMode.yolov5,
    this.rtspActive = false,
    this.fps = 0,
  });

  DeviceState copyWith({
    ConnectionState? connection,
    String? deviceName,
    String? deviceIp,
    int? batteryPct,
    DetectionMode? detectionMode,
    bool? rtspActive,
    int? fps,
  }) =>
      DeviceState(
        connection: connection ?? this.connection,
        deviceName: deviceName ?? this.deviceName,
        deviceIp: deviceIp ?? this.deviceIp,
        batteryPct: batteryPct ?? this.batteryPct,
        detectionMode: detectionMode ?? this.detectionMode,
        rtspActive: rtspActive ?? this.rtspActive,
        fps: fps ?? this.fps,
      );

  bool get isConnected => connection == ConnectionState.connected;

  String get rtspUrl =>
      deviceIp != null ? 'rtsp://$deviceIp/live/0' : '';

  String get wsUrl =>
      deviceIp != null ? 'ws://$deviceIp:8080' : '';
}
