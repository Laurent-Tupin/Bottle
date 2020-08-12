'''
Documentation: http://bottlepy.org/docs/dev/
Install:
    pip install bottle
'''

import bottle

#print(bottle.__author__)

@bottle.route('/')
@bottle.view('1_Template_Intro')
def index():
    #    tpl_welcome = bottle.template('Welcome {{str_name}}!', str_name = 'William')
    d_welcome = dict(str_name = 'William')
    return d_welcome

bottle.run(app = None, server = 'wsgiref', host='localhost', port = 8080, debug = True)



