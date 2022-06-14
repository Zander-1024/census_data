import os
from time import sleep
from urllib.request import urlopen, urlretrieve
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re


def gethtml(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
    except AttributeError as e:
        return None
    return bs

out_dir = 'rkpc6'
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

# root_url = 'http://www.stats.gov.cn/tjsj/pcsj/rkpc/7rp/zk/'
root_url = 'http://www.stats.gov.cn/tjsj/pcsj/rkpc/6rp/'
bs = gethtml(root_url + 'lefte.htm')
fileurllist = bs.findAll('a',{'href':re.compile('^.*.xls')})
for fileurl in fileurllist:
    downurl = root_url + fileurl['href']
    name = fileurl['href'].split("/")[1].split('.')
    new_name = name[0] + re.split('\\s+', fileurl.string)[1] + '.xls'

    out_file = os.path.join(out_dir, new_name)
    print(f"Downloading... {out_file}")
    urlretrieve(downurl, out_file)
    sleep(10)
