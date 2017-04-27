def wsgi_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    response_body = '<iframe width="933" height="700" src="https://app.powerbi.com/view?r=eyJrIjoiNjI1ZTI2YWItNjdhOC00ZWVhLWI4ZTctYzRjZTAyYmEzNmQ5IiwidCI6ImViOWExMWM5LTJiMTctNDMzZi1hOTJhLTA4MjQ0OGVlZGVlZiJ9" frameborder="0" allowfullscreen="true"></iframe>
    yield response_body.encode()

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 5555, wsgi_app)
    httpd.serve_forever()
