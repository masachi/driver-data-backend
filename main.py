import falcon
from middleware.validate import JSONTranslator, RequireJSON
from service.toutiao import ToutiaoService

driver_data = falcon.API(
    middleware=[
        RequireJSON(),
        JSONTranslator()
    ]
)

driver_data.add_route('/toutiao/latest', ToutiaoService())
