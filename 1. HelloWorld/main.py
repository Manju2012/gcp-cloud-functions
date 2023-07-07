# cmd to run this script ->  functions-framework --target hello_world

def hello_world(request):
    """
    Purpose: request
    """
    req_args = request.args
    req_json = request.get_json(silent=True)

    # name = req_args['name'] if req_args and 'name' in req_args else "world"
    if req_args and 'name' in req_args and 'lastname' in req_args:
        name = req_args['name']
        lastname = req_args['lastname']
        
    elif req_json and 'name' in req_json and 'lastname' in req_json:
        name = req_json['name']
        lastname = req_json['lastname']
        
    else:
        name = "World"
        lastname = ''
    return f"Hello {name} {lastname}"
# end def