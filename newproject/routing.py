from bottle import route, run

@route('/login')
def login():
    return '<h1>On the Login Page</h1>'

@route('/register')
def register():
    return '<h1>On the Register Page</h1>'

@route('/article/<id>')
def article(id):
    return '<h1>You are viewing article: ' + id + '</h1>'

@route('/page/<id>/<name>')
def page(id, name):
    return '<h1>You are viewing article: ' + id + ' with a name of '+ name +'</h1>'

@route('/posted', method='POST')
def posted():
    return '<h1>Posted</h1>'


if __name__ == '__main__':
    run(debug=True, reloader=True)