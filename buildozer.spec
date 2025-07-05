[app]
title = TestApp
package.name = testapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,json

version = 0.1
requirements = python3,kivy==2.1.0,kivymd==1.1.1,pillow,requests

[buildozer]
log_level = 2

[android]
api = 30
minapi = 21
ndk = 25b
sdk = 30
arch = arm64-v8a

permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[app]
icon = icon.png
