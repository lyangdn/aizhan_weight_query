'''
Author: Lyangdn
Date: 2023-11-02 22:16:37
LastEditTime: 2023-11-02 23:01:25
Description: 提取域名提供给爱站查询
Software: Visual Studio Code
Copyright (c) 2023 by Lyangdn, All Rights Reserved. 
'''
import argparse
import urllib3
from urllib.parse import urlparse
from tld import get_fld

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--infile", required=True)
parser.add_argument("-o", "--outfile", default="top_domain.txt")
args = parser.parse_args()

infile = args.infile
outfile = args.outfile

unique_domains = set()  # 用于存储唯一域名的集合

with open(infile, "r") as f:
    for url in f:
        try:
            parsed_url = urlparse(url)
            domain = parsed_url.netloc.split(":")[0]  # 移除端口号部分
            # 只提取二级域名
            first_url = get_fld(url)
            unique_domains.add(first_url)
            unique_domains.add(f"www.{first_url}")
            unique_domains.add(domain)
        except Exception as e:
            continue

with open(outfile, "w") as f:
    for domain in unique_domains:
        print(domain)
        f.write(f"{domain}\n")