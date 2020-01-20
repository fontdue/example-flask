import os
from functools import wraps
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from app import app
from app import config

_transport = RequestsHTTPTransport(
    url=config.GRAPHQL_URL,
    use_json=True,
)

_client = Client(
    transport=_transport,
    fetch_schema_from_transport=True,
)

_query_cache = {}

def _get_query_string(name):
    # in development we read the query from disk every time. this is a bit of a
    # performance issue in prod, so we'll cache the contents of those in memory
    if not app.config['ENV'] == 'development' and name in _query_cache:
        return _query_cache[name]

    filename = 'queries/{}.graphql'.format(name)
    query_file = open(os.path.join(os.path.dirname(__file__), filename), 'r')
    query_string = query_file.read()
    query_file.close()
    _query_cache[name] = query_string
    return query_string

def query(name):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            query_string = _get_query_string(name)
            kwargs['data'] = _client.execute(gql(query_string), kwargs)
            return f(*args, **kwargs)
        return decorated_function
    return decorator
