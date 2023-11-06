### 爱站一键化权重查询

查询结果图

![img](https://github.com/lyangdn/aizhan_weight_query/assets/95094405/a0e452cf-9487-499b-b779-e702fbf9e6ce)




爱站一键化权重查询工具，并且对www域名和主域名进行查询，更加方便提交漏洞与查询归属

本项目采用python3编写，请使用python3.8及以上版本运行本项目

项目开发环境为：

Ubuntu22.04

python3.8

使用方式（单文件使用方式）

```sh
git clone https://github.com/lyangdn/aizhan_weight_query.git
```

```shell
pip3 install -r requirements.txt
```


aizhan_weight_query.py使用方式：
```python
单个 python3 aizhan_weight_query.py -u url
批量 python3 aizhan_weight_query.py -f filename
导出指定文件 python3 aizhan_weight_query.py -o outfilename
```
top_www_domain.py使用方式：
```python
批量 python3 top_www_domain.py -i filename
导出指定文件 python3 top_www_domain.py -o outfilename
```

使用方式（双py文件批量使用）

查询主站权限
```sh
git clone https://github.com/lyangdn/aizhan_weight_query.git
```

```shell
pip3 install -r requirements.txt
```



Linux用户：

```sh
bash run.sh input_url.txt
```

其中``input_url.txt``自定义为输入文件

输出文件名为系统时间，格式为``年-月-日-时-分-秒.csv``

Windows用户

```shell
run.bat input_url.txt
```

其中``input_url.txt``自定义为输入文件

输出文件名为系统时间，格式为``年-月-日-时-分-秒.csv``
