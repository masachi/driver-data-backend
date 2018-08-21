import falcon
import json


class RequireJSON(object):

    def process_request(self, request, response):
        if not request.client_accepts_json:
            raise falcon.HTTPNotAcceptable('Response encoded as JSON')

        if request.method in ('POST'):
            if 'application/json' not in request.content_type:
                raise falcon.HTTPUnsupportedMediaType('Requests encoded as JSON')


class JSONTranslator(object):
    def process_request(self, request, response):

        if request.content_length in (None, 0):
            return

        body = request.stream.read()

        if not body:
            raise falcon.HTTPBadRequest('Empty request body')
        try:
            request.context['body'] = json.loads(body.decode('utf-8'))

        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(falcon.HTTP_753, 'Incorrect JSON')

    def process_response(self, request, response, resource):
        if 'body' not in response.context:
            return

        response.body = json.dumps(response.context['body'])
