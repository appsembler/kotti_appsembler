import os

from pyramid.paster import get_app
from paste.deploy import loadapp

def get_sqlalchemy_url_stackato():
    STACKATO = 'VCAP_SERVICES' in os.environ
    DB_STRING_FMT = 'postgresql://{user}:{password}@{hostname}:{port}/{name}'
    if STACKATO:
        import json
        vcap_services = json.loads(os.environ['VCAP_SERVICES'])
        srv = vcap_services['postgresql-8.4'][0]
        return DB_STRING_FMT.format(**srv['credentials'])

def my_loadapp(*args, **kwargs):
    global_conf = None
    sqlalchemy_url = get_sqlalchemy_url_stackato()
    if sqlalchemy_url:
        global_conf = {'sqlalchemy_url': sqlalchemy_url}
    kwargs['global_conf'] = global_conf
    return loadapp(*args, **kwargs)

application = get_app('production.ini', 'main', loadapp=my_loadapp)
