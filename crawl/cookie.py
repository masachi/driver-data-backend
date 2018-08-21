import requests


def get_cookies():
    res = requests.get('https://m.toutiao.com')
    cookies = requests.utils.dict_from_cookiejar(res.cookies)
    # print cookies
    print ('tt_webid' + cookies['tt_webid'])
    return cookies['tt_webid']


if __name__ == "__main__":
    get_cookies()