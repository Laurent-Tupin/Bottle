'''
Documentation: http://bottlepy.org/docs/dev/
Install:
    pip install bottle
'''

import bottle
import request

#print(bottle.__author__)

# ERROR
@bottle.error(404)
def not_found(error):
    return 'The request failed: {}'.format(str(error))

@bottle.error(401)
def not_found(error):
    return 'Cusotmized error: {}'.format(str(error))


# Entrance point
@bottle.route('/', method = ['GET','POST','DELETE'])
@bottle.view('1_Template_Intro')
def index():
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
    if request.method == 'DELETE':
        pass
    #    tpl_welcome = bottle.template('Welcome {{str_name}}!', str_name = 'William')
    d_welcome = dict(str_name = 'William')
    return d_welcome


# LOGIN
@bottle.route('/login')
def login():
    # LOGIN function
    # if it fails...
    bottle.redirect('/')
    

bottle.run(app = None, server = 'wsgiref', host='localhost', port = 8080, debug = True)



