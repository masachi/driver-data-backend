# coding=utf-8
from crawl.ascpGenerator import get_as_cp
from crawl.user_agents import get_user_agents
from crawl.cookie import get_cookies
import random
import requests
import json


class Toutiao(object):

    baseUrl = 'https://m.toutiao.com/list/?tag='
    tag = ''
    params = '&ac=wap&count=20&format=json_raw'
    as_param = '&as='
    cp_param = '&cp='
    max_behot_time = '&max_behot_time='

    def __init__(self, timestamp, tag):
        self.timestamp = timestamp
        self.tag = tag

    # def get_real_tag(self, tag):
    #
    #
    #
    def get_data(self):
        as_cp = get_as_cp(self.timestamp)

        url = self.baseUrl + self.tag + self.params + self.as_param + as_cp['as'] + self.cp_param + as_cp['cp'] + self.max_behot_time + str(
            int(self.timestamp))

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Host': 'm.toutiao.com',
            'User-Agent': random.choice(get_user_agents()),
            'Cookie': 'tt_webid=' + get_cookies()
        }

        response = requests.get(url=url, headers=headers)

        # print response.text

        data = (json.loads(response.text))['data']
        result = []
        for each in data:
            # print (each['abstract'])

            if not each['abstract'] in (None, ''):
                result.append(each)

        return result
