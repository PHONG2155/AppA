[app]
# --- Thông tin app ---
title = Login App
package.name = logindemo
package.domain = org.phong

# PHẢI có version
version = 0.1

# file python chính để chạy app
entrypoint = main.py

# thư mục code nguồn
source.dir = .
source.include_exts = py,kv,png,jpg,ttf,txt

# chỉ cho chạy dọc
orientation = portrait

# thư viện python sẽ được đóng gói vào APK
# (dùng đúng phiên bản kivy mà ta đang build trong CI: 2.3.0)
requirements = python3,kivy==2.3.0

# kiến trúc CPU build ra (chỉ 64-bit ARM để đơn giản hoá build)
android.archs = arm64-v8a

# API Android target và min API
android.api = 34
android.minapi = 21

# NDK và NDK API (khớp với NDK r25b mà buildozer tải)
android.ndk = 25b
android.ndk_api = 21

# ép accept license trong chế độ CI
android.accept_sdk_license = True

# giảm spam log (2 = info)
log_level = 2
