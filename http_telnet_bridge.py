import sys
import time
import telnetlib
import re
import urlparse
import urllib
from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler


### HTTP GET request handler class ###

class telnet_message_handler( BaseHTTPRequestHandler ) :
   
   def log_message(self, format, *args):
      return

   def telnet_query( self, query, HOST ) :
      tn = telnetlib.Telnet(HOST)
      tn.write(query+'\n')
      tn.close()
      return

   def telnet_message_query( self, query, HOST, WAIT ) :
      tn = telnetlib.Telnet(HOST)
      tn.write(query+'\n')
      if WAIT > 0 :
         time.sleep(WAIT)
         try :
            response = tn.read_very_eager()
         except EOFError :
            response = ''
         message = re.sub( '[\r,\n]', ' ', response )
      else :
         message = ''
      tn.close()
      return message

   def do_GET(self) :
      parsed_path = urlparse.urlparse(self.path)
      query = urllib.unquote( parsed_path.query )
      response = ''
      message = ''
      if len(query) > 0 :
         parts = query.split('|')
         if len(parts) >= 3 :
            HOST = parts[0]
            WAIT = float(parts[1])
            CMD = parts[2]
            response = self.telnet_message_query( CMD, HOST, WAIT )
            if len(parts) >= 4 :
                epat = parts[3]
                message = re.sub( epat, r'\1', response )
                if len(parts) >= 5 :
                    mpat = parts[4]
                    match = re.match( mpat, message )
                    if match :
                        message = '1'
                    else :
                        message = '0'
            else :
                message = response
         elif len(parts) == 2 :
            HOST = parts[0]
            CMD = parts[1]
            self.telnet_query( CMD, HOST )
      self.send_response(200)
      self.end_headers()
      self.wfile.write(message)
      if self.server.DEBUG :
          print( '[HTTP TELNET BRIDGE] <' + query + '> ==> <' + response + '> ==> <' + message + '>' )
      return


### MAIN ###

LOCALHOST = ""
LOCALPORT = 8000
server_address = (LOCALHOST, LOCALPORT)

if (len(sys.argv) == 2) and (sys.argv[1].lower() == 'debug') :
    DEBUG = True
    print( '[HTTP TELNET BRIDGE] starting server, DEBUG ENABLED' )
else:
    DEBUG = False
    print( '[HTTP TELNET BRIDGE] starting server, no debug' )

server = HTTPServer( server_address, telnet_message_handler )
server.DEBUG = DEBUG
server.serve_forever()

