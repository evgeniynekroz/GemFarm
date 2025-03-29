[app]
# Основные параметры приложения
title = GemClicker
package.name = com.yourname.gemclicker
package.domain = org
source.dir = .
version = 1.0.0

# Указываем расширения, которые нужно включить
source.include_exts = py,png,jpg,kv,atlas

# Android настройки
android.permissions = INTERNET
android.minapi = 28  # Минимальная версия Android 9+
android.sdk_path = /path/to/android-sdk  # Укажите путь к SDK
android.ndk_path = /path/to/android-ndk  # Укажите путь к NDK
android.debug = 1  # Для дебажной сборки

# Устанавливаем зависимости
dependencies = aiogram==2.25.2, 
aiohttp==3.8.6, 
aiosignal==1.3.2, 
astroid==2.15.8, 
async-timeout==4.0.3, 
attrs==25.3.0, 
audiostream==0.2, 
Babel==2.9.1, 
buildozer==1.5.0, 
certifi==2025.1.31, 
cffi==1.16.0, 
charset-normalizer==3.4.1, 
cmake==3.26.4, 
dill==0.3.7, 
distlib==0.3.9, 
distro==1.8.0, 
docutils==0.21.2, 
dotenv==0.9.9, 
filelock==3.18.0, 
frozenlist==1.5.0, 
idna==3.10, 
isort==5.12.0, 
jedi==0.19.0, 
Kivy==2.2.1, 
lazy-object-proxy==1.9.0, 
magic-filter==1.0.12, 
mccabe==0.7.0, 
multidict==6.2.0, 
ninja==1.11.1, 
packaging==23.1, 
parso==0.8.3, 
pexpect==4.9.0, 
pkgconfig==1.5.5, 
platformdirs==3.10.0, 
propcache==0.3.0, 
ptyprocess==0.7.0, 
pybind11==2.11.1, 
pycparser==2.21, 
pygame==2.5.0, 
Pygments==2.19.1, 
pyjnius==1.5.0, 
pylint==2.17.5, 
PySDL2==0.9.15, 
python-dotenv==1.0.1, 
pytz==2025.1, 
scikit-build==0.17.6, 
sh==2.2.2, 
six==1.16.0, 
tomlkit==0.12.1, 
typed-ast==1.5.5, 
virtualenv==20.29.3, 
wrapt==1.15.0, 
yarl==1.18.3

# Параметры сборки
[buildozer]
log_level = 2
warn = 1

# Указываем версию Python
python.version = 3.10

# Версия Android
android.minapi = 28  # Минимальная версия Android 9+
android.target = android-28  # Целевая версия API

# Архитектура Android
android.arch = armeabi-v7a

# Путь к манифесту
android.manifest = ./AndroidManifest.xml

# Включаем сборку
android.build = 1

[environment]
CFLAGS = -Wno-error
LDFLAGS = -Wno-error