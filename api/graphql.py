import os
from functools import wraps
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

from api import config

_transport = RequestsHTTPTransport(
    url=config.GRAPHQL_URL,
    use_json=True,
)

client = Client(
    transport=_transport,
    # fetch_schema_from_transport=True,
)

def query(name):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            filename = 'queries/{}.graphql'.format(name)
            query_file = open(os.path.join(os.path.dirname(__file__), filename), 'r')
            query_string = query_file.read()
            query_file.close()
            kwargs['data'] = client.execute(gql(query_string), kwargs)
            return f(*args, **kwargs)
        return decorated_function
    return decorator
