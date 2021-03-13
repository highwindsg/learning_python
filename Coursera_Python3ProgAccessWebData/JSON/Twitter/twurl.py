#!/usr/bin/env python3

import urllib
import oauth
""" Create a file 'hidden.py' in the same folder with the necessary APIs keys 
and should contain the 'consumer_key', 'cosumer_secret_key',
'token_key' and 'token_secret_key'. """
import hidden



def augment(url, parameters):
    secrets = hidden.oath()
    consumer = oauth.OAuthConsumer(secrets["consumer_key"], secrets["consumer_secret"])
    token = oauth.OAuthToken(secrets["token_key"], secrets["token_secret"])
    oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer,
                                                               token = token,
                                                               http_method = "GET",
                                                               http_url = url,
                                                               parameters = parameters
                                                               )
    oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(),
                               consumer,
                               token
                               )
    return oauth_request.to_url()


    