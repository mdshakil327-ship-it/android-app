[app]
title = CyberApp
package.name = cyberapp
package.domain = org.cyber
source.dir = .
source.exts = py,png,jpg,kv,atlas
source.exclude_dirs = tests, bin, venv, .github, kivy, .git, build, .buildozer
version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 34
android.minapi = 21
android.ndk = 25b
