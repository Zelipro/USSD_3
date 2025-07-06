[app]
title = CodeSaver
package.name = monappkivymd
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,kivymd,pillow
icon.filename = %(source.dir)s/Logo.png

[buildozer]
log_level = 2

[android]
api = 34
minapi = 21
ndk = 25b
sdk = 34
android.permissions = INTERNET
android.archs = arm64-v8a, armeabi-v7a
orientation = portrait
android.orientation = portrait
android.orientations = portrait
