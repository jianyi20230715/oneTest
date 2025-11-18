import requests

from urllib.parse import urlparse
from tools import append_dict_to_json


def extract_hostname_with_parse(url):
    """
    使用 urllib.parse 库提取规范的 hostname。
    """
    # 确保 URL 有一个协议头，否则 urlparse 无法正确解析
    if not url.startswith(("http://", "https://", "//")):
        url = "http://" + url  # 临时添加一个协议头进行解析

    parsed_url = urlparse(url)
    hostname = parsed_url.hostname

    # if hostname:
    #     # 可选：去除 www. 前缀
    #     return hostname.removeprefix("www.")
    return hostname  # 如果解析失败，返回原始 URL


if __name__ == "__main__":
    base_land = "https://toolb.cn/favicon/"
    base_froeign = "https://www.google.com/s2/favicons?domain="

    with open(r'config.txt', "r", encoding="utf-8") as f:
        for line in f.readlines():

            name, url, category = line.split()
            data_dic = {
                    "id": 25,
                    "name": name,
                    "url": url,
                    "logo": None,
                    "desc": None,
                    "catelog": category,
                    "status": None,
                    "sort_order": 9999,
                    "create_time": None,
                    "update_time": None
                }

            cleaned_url = extract_hostname_with_parse(url)
            if requests.get(base_land + cleaned_url).status_code == 200:
                data_dic["logo"] = base_land + cleaned_url
            elif requests.get(base_froeign + cleaned_url).status_code == 200:
                res = requests.get(base_froeign + cleaned_url)
                data_dic["logo"] = res.url

            append_dict_to_json("config.json", data_dic)
