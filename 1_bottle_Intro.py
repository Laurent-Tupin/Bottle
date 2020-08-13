'''
Documentation: http://bottlepy.org/docs/dev/
Install:
    pip install bottle
'''

import bottle

#print(bottle.__author__)

# ERROR
@bottle.error(404)
def not_found(error):
    return 'The request failed: {}'.format(str(error))

@bottle.error(401)
def not_found_401(error):
    return 'Cusotmized error: {}'.format(str(error))


# Entrance point
@bottle.route('/', method = ['GET','POST','DELETE'])
@bottle.view('1_Template_Intro')
def index():
    if bottle.request.method == 'GET':
        pass
    if bottle.request.method == 'POST':
        pass
    if bottle.request.method == 'DELETE':
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
    
#Wikipage   /wikipage?id=10&section=b
@bottle.route('/wikipage')
def wiki_page():
    str_pageid = bottle.request.query.pageid or '-1'
    str_section = bottle.request.query.section or 'zz'
    tpl_wiki = bottle.template('The wikipage {{pageid}}, section {{section}}', 
                               pageid = str_pageid, section = str_section)
    return tpl_wiki 




bottle.run(app = None, server = 'wsgiref', host='localhost', port = 8080, debug = True)



