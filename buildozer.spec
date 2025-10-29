[app]
title = Login App
package.name = logindemo
package.domain = org.phong

version = 0.1

entrypoint = main.py
source.dir = .
source.include_exts = py,kv,png,jpg,ttf,txt

orientation = portrait

requirements = python3,kivy==2.3.0

# chỉ build 1 ABI 64-bit
android.archs = arm64-v8a

# API/NDK khớp với workflow
android.api = 34
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

android.accept_sdk_license = True

log_level = 2


[buildozer]
p4a.branch = master
android.accept_sdk_license = True
