#!/bin/bash

if [ -z "$1" ]; then
  echo "使用方式：bash run.sh input_url.txt"
  exit 1
fi

# 等待3秒
sleep 3

# 执行 top_www_domain.py 脚本
python3 top_www_domain.py -i "$1"

# 执行 aizhan_weight_query.py 脚本
python3 aizhan_weight_query.py
