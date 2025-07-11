[app]
title = CodeSaver
package.name = CodeSaver_app
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,jpeg
source.include_patterns = Flags/*,Reso/*,*.txt,*.jpeg,*.jpg,*.png
version = 0.1
requirements = python3,kivy,kivymd,pillow
icon.filename = %(source.dir)s/Logo.png

# Permissions Android
android.permissions = INTERNET,CALL_PHONE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2

[android]
api = 34
minapi = 21
ndk = 25b
sdk = 34
android.archs = arm64-v8a, armeabi-v7a
orientation = portrait
android.orientation = portrait
android.orientations = portrait

# Ajout pour éviter les crashes
android.add_src = .
android.gradle_dependencies = 
android.add_compile_options = sourceCompatibility JavaVersion.VERSION_1_8, targetCompatibility JavaVersion.VERSION_1_8
