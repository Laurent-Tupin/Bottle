'''
Documentation: http://bottlepy.org/docs/dev/
Install:
    pip install bottle
'''

import bottle

#print(bottle.__author__)

@bottle.route('/')
def index():
    tpl_1 = bottle.template('Welcome {{str_name}}!', str_name = 'William')
    return tpl_1

bottle.run(app = None, server = 'wsgiref', host='localhost', port = 8080, debug = True)



