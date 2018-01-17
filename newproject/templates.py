from bottle import run, template, route

@route('/')
def index():
    return template('index', name = 'Sagar')

if __name__ == '__main__':
    run(debug=True, reloader=True)