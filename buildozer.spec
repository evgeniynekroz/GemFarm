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
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up JDK 11
        uses: actions/setup-java@v2
        with:
          java-version: 11

      - name: Set up Android SDK
        uses: reactivecircus/android-sdk-action@v2
        with:
          api-level: 30
          build-tools-version: 30.0.3

      - name: Install dependencies
        run: |
          sudo apt update
          sudo apt install -y python3-pip
          pip3 install buildozer

      - name: Build APK
        run: |
          cd path/to/your/project
          buildozer android debug
          
      - name: Upload APK to artifacts
        uses: actions/upload-artifact@v2
        with:
          name: app-debug.apk
          path: ./bin/app-debug.apk