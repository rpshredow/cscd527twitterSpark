# TweetRead.py
import os
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json
 
class TweetsListener(StreamListener):
 
    def __init__(self, csocket):
        self.client_socket = csocket
 
    def on_data(self, data):
        try:
            print(data.split('\n'))
            self.client_socket.send(data)
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
def sendData(c_socket):
    auth = OAuthHandler("Do2LglI9daTDLs7G9jdxzrLax", 
    	"owDpyUPKr0qBb6aG3gNOzLRYLAWvaSwQVO2K5l3232RiR26eZ2")
    auth.set_access_token("112331273-u0XL6ELmW7iUd6Z61o5sY4SasqwScE3bdL6T5enK", 
    	"qxFhkfYzQ6omO2tXzKE8lcpkw0cmGLZQ9arWD6GWxU5Tk")
	
    twitter_stream = Stream(auth, TweetsListener(c_socket))
    twitter_stream.filter(languages=["en"], track=["bernie sanders", "joe biden", "elizabeth warren", "donald trump"], is_async=True, stall_warnings=True)
 
if __name__ == "__main__":
    s = socket.socket()     # Create a socket object
    host = "localhost"      # Get local machine name
    port = 5556             # Reserve a port for your service.
    s.bind((host, port))    # Bind to the port
 
    print("Listening on port: %s" % str(port))
 
    s.listen(5)                 # Now wait for client connection.
    c, addr = s.accept()        # Establish connection with client.
 
    print( "Received request from: " + str( addr ) )
 
    sendData( c )