import os
import sys
import wsgi
import cherrypy
#from cherrypy import wsgiserver
try:
        from cheroot.wsgi import Server as wsgiserver
except ImportError:
        from cherrypy.wsgiserver import CherryPyWSGIServer as wsgiserver
        # from cherrypy import wsgiserver

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
        execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
        pass

# Get the environment information we need to start the server
ip = os.environ['OPENSHIFT_PYTHON_IP']
port = int(os.environ['OPENSHIFT_PYTHON_PORT'])
host_name = os.environ['OPENSHIFT_GEAR_DNS']

class HelloWorld(object):
    def index(self):
        return "Hello World!"
    index.exposed = True

    def hello(self):
        return '<h1>FUCKED UP WHOLE NIGHT JUST TO GET THIS</h1>'
    hello.exposed = True

# server = wsgiserver.CherryPyWSGIServer((ip, port), wsgi.application, server_name=host_name)
cherrypy.config.update({'server.socket_port': port})
cherrypy.config.update({'server.socket_host': ip})
cherrypy.quickstart(HelloWorld())
# server.start()
