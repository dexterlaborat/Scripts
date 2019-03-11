import os
import config
import requests
import sys
import argparse
import re
import bs4 as bs
class SomeWorm:
    def __init__(self,host):
        config.step = 0
        config.host=host
    def extraction(self,url):
      try:
        host=config.host
        links=[]
        config.step += 1
        req = requests.get(url)
        soup = bs.BeautifulSoup(req.text,'lxml')
        for u in soup.find_all('a') or soup.find_all('link'):
            regex=re.search('http(.*)',str(u.get('href')))
            link=u.get('href')
            if regex:
                pass
            else:
                try:
                    link=host+link
                except Exception as e:
                    pass
            if link not in links:
                links.append(str(link))
        for relink in range(config.step,len(links)):
            print(links[relink])
            self.extraction(links[relink])

        return links
      except Exception as e:
          pass
    def sqli(self,links):
        pd="'"
        for lnk in links:
            if re.search('(.*)\?(.*)',lnk):
                lns = lnk.split('&')
                for l in range(len(lns)):
                    lns[l-1] += pd
                    req = '&'.join(lns)
                    code = requests.get(req).status_code
                    print(req,"---",code)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url',help="Enter url")
    args=parser.parse_args()
    sw=SomeWorm(args.url)
    links = sw.extraction(args.url)
    sw.sqli(links)

