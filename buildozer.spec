[app]
title = LoginApp
package.name = loginapp
package.domain = org.example
source.dir = .
source.include_exts = py,kv,png,jpg,atlas
version = 0.1
orientation = portrait
fullscreen = 0

# Kivy + SDL2 bootstrap
requirements = python3,kivy==2.3.0

# tên file apk output
android.archive = False

[buildozer]
log_level = 2
warn_on_root = 1

[app.android]
# chỉ build arm64-v8a cho nhanh
android.archs = arm64-v8a
minapi = 21
sdk = 34
ndk = 27b
