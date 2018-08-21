import falcon
from crawl.toutiao import Toutiao


class ToutiaoService(object):

    def on_post(self, request, response):
        try:
            print(request.context['body']['body']['timestamp'])
            timestamp = request.context['body']['body']['timestamp']
            type = request.context['body']['body']['type']

            toutiao_crawl = Toutiao(timestamp, type)

            response.context['body'] = {'body': toutiao_crawl.get_data()}
            response.status = falcon.HTTP_200

        except KeyError:
            raise falcon.HTTPBadRequest('400 Bad Request with key missing')