import time
import telnetlib
import re
import urlparse
import urllib
from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler

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
#      print( 'writing <'+query+'>' )
      tn.write(query+'\n')
      if WAIT > 0 :
#         print( 'waiting <'+str(WAIT)+'>' )
         time.sleep(WAIT)
         try :
            response = tn.read_very_eager()
#            print( 'got <'+response+'>' )
         except EOFError :
            response = ''
         message = re.sub( '[\r,\n]', ' ', response )
#         print( 'final <'+message+'>' )
      else :
         message = ''
      tn.close()
      return message

   def do_GET(self) :
      parsed_path = urlparse.urlparse(self.path)
      query = urllib.unquote( parsed_path.query )
      message = ''
      if len(query) > 0 :
         parts = query.split('|')
         if len(parts) == 3 :
            HOST = parts[0]
            WAIT = float(parts[1])
            CMD = parts[2]
            message = self.telnet_message_query( CMD, HOST, WAIT )
         elif len(parts) == 2 :
            HOST = parts[0]
            CMD = parts[1]
            self.telnet_query( CMD, HOST )
      self.send_response(200)
      self.end_headers()
      self.wfile.write(message)
      print( '[HTTP TELNET BRIDGE] <' + query + '> ==> <' + message + '>' )
      return

LOCALHOST = ""
LOCALPORT = 8000

print( '[HTTP TELNET BRIDGE] starting server' )
server_address = (LOCALHOST, LOCALPORT)
server = HTTPServer( server_address, telnet_message_handler )
server.serve_forever()

