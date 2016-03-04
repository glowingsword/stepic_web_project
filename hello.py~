from cgi import parse_qs
import string

def app(environ, start_response):
  if environ['REQUEST_METHOD'] == 'GET':
    body = string.replace(environ['QUERY_STRING'], '&', '\r\n')
    print(body);
    start_response('200 OK', [('Content-Type', 'text/plain')]  )
    yield body
