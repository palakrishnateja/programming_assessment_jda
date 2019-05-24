#!/usr/local/bin/python3
from http.server import SimpleHTTPRequestHandler
import socketserver
import os

def launch_http_server(host_name,host_port,images_dir):
    try:
        os.chdir(images_dir)
        myServer = socketserver.TCPServer((host_name, host_port), SimpleHTTPRequestHandler) 
        print('serving at url - http://{hostname}:{port}'.format(hostname = host_name,port=host_port))
        myServer.serve_forever()

    except KeyboardInterrupt:
        print('^C received, shutting down the web server')
        myServer.socket.close()
    except Exception as e:
        print('Server launch failed with error - {e}'.format(e=e))

#Driver program
def main():
    hostname = input('Host Name-') #localhost'
    portno = int(input('Port No-')) #9090
    imagesdir = os.path.join(os.path.dirname(os.path.abspath(__file__))+os.sep+'..'+os.sep+'downloaded_images')
    if not os.path.isdir(imagesdir):
        os.mkdir(imagesdir)
    launch_http_server(hostname,portno,imagesdir)
    

if __name__=='__main__':
    main()
