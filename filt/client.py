#!/usr/bin/env python
'''filt/client.py
This is the processes of client of Filt.
'''

import sys
import json
import base64
import requests

from abc import abstractmethod


class FiltClient:
    '''
    The client class of Filt.
    '''

    def __init__(self, url):
        '''
        Set self.target and self.option.
        '''
        if type(url) is not str:
            # if argument data is not string,
            # raise error
            sys.stderr.write('url must be str')
            raise TypeError
        
        self.url = url 
        
    def send(self, target, option=None, verify=True):
        '''
        Send data to Filt,
        and return result.
        '''
        try:
            # convert target to string
            target = str(target)
        except:
            sys.stderr.write('Target must be convertable to str')

        if option is None:
            # if option is not set,
            # ready empty dict
            option = {}
        elif type(option) is not dict:
            # if option is not dict,
            # raise error
            sys.stderr.write('Option must be dict')
            raise TypeError
        
        if type(verify) is not bool:
            # if option is not bool,
            # raise error
            sys.stderr.write('Option must be bool')
            raise TypeError
        
        # substitute to self.`variables`
        self.target = target
        self.request = option
        self.verify = verify

        # init request's target
        self.base64_target = target.encode('utf-8')
        self.request['target'] = base64.b64encode(self.base64_target)
        self.request['target'] = self.request['target'].decode('utf-8')

        # send request
        headers = {'content-type': 'application/json'}
        self.response = requests.post(
            self.url,
            json.dumps(self.request),
            verify=self.verify,
            headers=headers
        )

        # decode message from base64
        self.result = json.loads(self.response.text)
        
        for index in range(len(self.result['message'])):
            message = self.result['message'][index].encode('utf-8')
            message = base64.b64decode(message)
            self.result['message'][index] = message.decode('utf-8')

        return self.result
