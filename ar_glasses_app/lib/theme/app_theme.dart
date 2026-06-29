import 'package:flutter/material.dart';

class AppTheme {
  static const _dark = Color(0xFF0d0d1a);
  static const _card = Color(0xFF1a1a2e);
  static const _accent = Color(0xFF4f8ef7);
  static const _success = Color(0xFF27ae60);
  static const _warn = Color(0xFFe67e22);
  static const _danger = Color(0xFFe94560);

  static ThemeData get dark => ThemeData(
        useMaterial3: true,
        brightness: Brightness.dark,
        scaffoldBackgroundColor: _dark,
        colorScheme: const ColorScheme.dark(
          primary: _accent,
          secondary: _success,
          error: _danger,
          surface: _card,
        ),
        cardTheme: const CardThemeData(
          color: _card,
          elevation: 0,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.all(Radius.circular(12)),
          ),
        ),
        appBarTheme: const AppBarTheme(
          backgroundColor: _dark,
          foregroundColor: Colors.white,
          elevation: 0,
          centerTitle: false,
        ),
        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ElevatedButton.styleFrom(
            backgroundColor: _accent,
            foregroundColor: Colors.white,
            shape: const StadiumBorder(),
            padding:
                const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
          ),
        ),
        iconTheme: const IconThemeData(color: Colors.white70),
        dividerColor: Colors.white12,
        extensions: const [_AppColors()],
      );

  static Color get accent => _accent;
  static Color get success => _success;
  static Color get warn => _warn;
  static Color get danger => _danger;
  static Color get card => _card;
  static Color get background => _dark;
}

class _AppColors extends ThemeExtension<_AppColors> {
  const _AppColors();
  @override
  ThemeExtension<_AppColors> copyWith() => this;
  @override
  ThemeExtension<_AppColors> lerp(covariant ThemeExtension<_AppColors>? other, double t) => this;
}
