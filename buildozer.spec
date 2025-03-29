name: Build APK

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest  # Используем Ubuntu для сборки

    steps:
      # Проверяем код из репозитория
      - name: Checkout code
        uses: actions/checkout@v2

      # Устанавливаем JDK (Java Development Kit) для сборки Android приложения
      - name: Set up JDK 11
        uses: actions/setup-java@v2
        with:
          java-version: 11  # Устанавливаем Java 11

      # Устанавливаем Android SDK
      - name: Set up Android SDK
        uses: reactivecircus/android-sdk-action@v2
        with:
          api-level: 30        # API уровень Android (можно выбрать другой, если нужно)
          build-tools-version: 30.0.3  # Версия инструментов сборки Android

      # Устанавливаем необходимые зависимости
      - name: Install dependencies
        run: |
          sudo apt update
          sudo apt install -y python3-pip
          pip3 install buildozer   # Устанавливаем buildozer для сборки APK

      # Собираем APK с помощью Buildozer
      - name: Build APK
        run: |
          cd GemFarm  # Переходим в директорию с проектом, где есть файл buildozer.spec
          buildozer android debug  # Команда для сборки APK

      # Проверка, что APK был создан
      - name: Check APK existence
        run: |
          if [ -f ./bin/app-debug.apk ]; then echo "APK exists"; else echo "APK not found"; exit 1; fi

      # Загружаем APK файл как артефакт
      - name: Upload APK to artifacts
        uses: actions/upload-artifact@v2  # Используем v2
        with:
          name: app-debug.apk      # Имя файла артефакта
          path: ./bin/app-debug.apk  # Путь к собранному APK файлу