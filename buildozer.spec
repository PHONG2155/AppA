[app]
title = Login App
package.name = logindemo
package.domain = org.phong
source.dir = .
source.include_exts = py,kv,png,jpg,ttf,txt
entrypoint = main.py
orientation = portrait

# Các thư viện Python đưa vào APK
# Kivy 2.3.0 đang dùng trong workflow hiện tại (log trên nói p4a gọi kivy==2.3.0)
requirements = python3,kivy==2.3.0

# chỉ build arm64 cho nhẹ (bỏ armeabi-v7a)
android.archs = arm64-v8a

# API target & min API cho Android
android.api = 34
android.minapi = 21

# ép dùng NDK r25b (chính là bản buildozer đã tải)
android.ndk = 25b
android.ndk_api = 21

# tránh hỏi license
android.accept_sdk_license = True

# tắt logcat attach tự động (an toàn hơn cho CI)
log_level = 2
