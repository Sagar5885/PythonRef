from bottle import run, route, request

@route('/')
def index():
    return {"name" : "jsonData", "myList" : [1, 2, 3, 4, 5]}

run(debug=True, reloader=True)