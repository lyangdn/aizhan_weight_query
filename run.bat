@echo off

if "%~1"=="" (
  echo 使用方式：run.bat input_url.txt
  exit /b 1
)

timeout /t 3 >nul

python top_www_domain.py -i "%~1"

python aizhan_weight_query.py
