'''
Author: Lyangdn
Date: 2023-11-02 17:30:52
LastEditTime: 2023-11-02 23:13:27
Description: 
Software: Visual Studio Code
Copyright (c) 2023 by Lyangdn, All Rights Reserved. 
'''
import requests
import urllib3
import argparse
import os
import datetime
from lxml import etree
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor
import csv
# 解决requests请求出现的InsecureRequestWarning错误
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
BULE_BOLD = "\033[1;34m"
RESET = "\033[0m"
RED_BOLD = "\033[1;31m"

def query(url,outfile):
    domain=url
    url = "https://www.aizhan.com/cha/{}/".format(url)

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,vi;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://www.aizhan.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'linux',
    }

    response = requests.get(url=url, headers=headers,timeout=5)
    lxml_tree = etree.HTML(response.text)
    href_name = lxml_tree.xpath(
        '//div[@id="webpage_title"]//text()')
    print("\n-> Title信息: {0}".format("".join(href_name)))
    br = lxml_tree.xpath(
        '//a[@id="baidurank_br"]//img//@alt')
    mbr = lxml_tree.xpath(
        '//a[@id="baidurank_mbr"]//img//@alt')
    pr = lxml_tree.xpath(
        '//a[@id="360_pr"]//img//@alt')
    sm_pr = lxml_tree.xpath(
        '//a[@id="sm_pr"]//img//@alt')
    sogou_pr = lxml_tree.xpath(
        '//a[@id="sogou_pr"]//img//@alt')
    google_pr = lxml_tree.xpath(
        '//a[@id="google_pr"]//img//@alt')
    print(f"查询url为：{url}")
    print("[+] 综合权重: \n 百度权重: {0}\t移动权重:{1}\t360权重:{2}\t神马权重:{3}\t搜狗权重:{4}\t谷歌PR:{5}".format("".join(
        br), "".join(mbr), "".join(pr), "".join(sm_pr), "".join(sogou_pr), "".join(google_pr)))

    icp = lxml_tree.xpath(
        '//ul[@id="icp"]//text()')
    print("[+] 备案信息: \n", repr(" ".join(icp)).replace(
        "\\n", "").replace("\\t", "").replace("'", ""))
    # with open(f"{outfile}", "a") as f:
    #     f.write("\n\n-> Title信息: {0}\n".format("".join(href_name)))
    #     f.write(f"查询域名为：{domain}\n")
    #     f.write(f"查询url为：{url}\n")
    #     f.write("[+] 综合权重: 百度权重: {0}\t移动权重:{1}\t360权重:{2}\t神马权重:{3}\t搜狗权重:{4}\t谷歌PR:{5}".format("".join(
    #     br), "".join(mbr), "".join(pr), "".join(sm_pr), "".join(sogou_pr), "".join(google_pr)))
    #     f.write("[+] 备案信息: \n", repr(" ".join(icp)).replace( "\\n", "").replace("\\t", "").replace("'", ""))
    with open(f"{outfile}","a") as csvfile:
        w=csv.writer(csvfile)
        # w.writerow(["查询域名","查询url","Title信息","百度权重","移动权重","360权重","神马权重","搜狗权重","谷歌权重","icp备案信息"]) 
        w.writerow([domain,url,"".join(href_name),"".join(br),"".join(mbr),"".join(pr),"".join(sm_pr),"".join(sogou_pr),"".join(google_pr),repr(" ".join(icp)).replace( "\\n", "").replace("\\t", "").replace("'", "")])
def Copyright(outfile):
    global BULE_BOLD
    global RED_BOLD
    global RESET
    title='声明：此脚本仅用于学习'
    text = f'''
    使用方法:
        单个 python3 {os.path.basename(__file__)} -u url
        批量 python3 {os.path.basename(__file__)} -f filename
        导出指定文件 python3 {os.path.basename(__file__)} -o outfilename 
        导出文件名为：{outfile}
    开始rush B................................
    '''
    print(f"\t{RED_BOLD}{title}{BULE_BOLD}{text}{RESET}")

example_text = f"""
    python {os.path.basename(__file__)} -u qq.com
    python {os.path.basename(__file__)} -f 1.txt
"""
try:
    parser = argparse.ArgumentParser(
        description=example_text, formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-u", "--url", required=False)
    parser.add_argument("-f", "--files", default="top_domain.txt")
    time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    parser.add_argument("-o", "--outfile", default=f"{time}.csv")
    args = parser.parse_args()
    outfile=args.outfile
    url = args.url
    files = args.files
    Copyright(outfile)
    with open(f"{outfile}","w") as csvfile:
        w=csv.writer(csvfile)
        w.writerow(["查询域名","查询url","Title信息","百度权重","移动权重","360权重","神马权重","搜狗权重","谷歌权重","icp备案信息"]) 
    if url:
        if "http://" in url or "https://" in url:
            url = urlparse(url).netloc
            query(url=url, outfile=outfile)
        else:
            url = url
            query(url=url,outfile=outfile)
    else:
        count = 0
        with open(files, "r", encoding="utf-8") as f:
                # 创建最大线程数的线程池
                with ThreadPoolExecutor(10) as threadPool:
                        for url in f:
                            try:
                                if url:
                                    if "http://" in url or "https://" in url:
                                        url = urlparse(url).netloc
                                    else:
                                        url = url
                                threadPool.submit(query, url.replace("\n", ""),outfile)
                                count += 1
                            except Exception as e:
                                print("[-] error: ",e)
                                continue
        print("\ntotle: [{}]".format(count))
except:
    pass
