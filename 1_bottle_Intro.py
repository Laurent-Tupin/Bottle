'''
Documentation: http://bottlepy.org/docs/dev/
Install:
    pip install bottle
'''

import bottle

#print(bottle.__author__)

@bottle.route('/')
def index():
    str_return = 'Welcome !'
    return str_return

bottle.run(app = None, server = 'wsgiref', host='localhost', port = 8080, debug = True)



