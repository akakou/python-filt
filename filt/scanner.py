#!/usr/bin/env python
'''scanner/scanner.py
This script has the base of scaneer of Filt.
'''

import sys
import json
import base64

from abc import abstractmethod


class BaseScanner:
    '''
    The base of scanner of filt.
    If you want to make new scanner,
    make new class which inheritance this class,
    then implement methods (self.scan, self.ready, self.end).
    '''
    def __init__(self):
        '''
        Init some variables.
        '''
        self.result = {
            'hit': False,
            'messages': []
        }
        self.logs = []
        self.use_log = False
    
    def _input(self):
        '''
        Input data from scanner,
        and return decoded data from base64.
        '''
        data = input()
        
        if data == '':
            # if data is empty,
            # filt call end
            return None

        # decode from base64
        data = data.encode('utf-8')
        data = base64.b64decode(data)

        return data

    def _output(self, data):
        '''
        Eecode data to base64,
        and Output to scanner.
        '''
        if type(data) is not str:
            # if argument data is not string,
            # raise error
            sys.stderr.write('Data must be str')
            raise TypeError

        # encode to base64
        data = data.encode('utf-8')
        data = base64.b64encode(data).decode('utf-8')

        print(data)

    def _end(self):
        '''
        Convert data from dict to str,
        and output data.
        '''
        result = self.result

        # change bool to str
        if result['hit']:
            result['hit'] = 'true'
        else:
            result['hit'] = 'false'

        # dumps json
        result = json.dumps(result)

        # output
        self._output(result)

    def run(self):
        '''
        The main rootine of filt scanner.
        '''
        # input target
        target = self._input()
        self.ready(target)

        while True:
            # input signature
            signature = self._input()

            if signature is None:
                # if signature is None,
                # scanner process to end
                self.end()
                self._end()
                
                return

            # scan
            is_hit, message = self.scan(target, signature)

            if is_hit:
                # if signature hit,
                # hit flag makes true and append message
                self.result['hit'] = True
                self.result['messages'].append(message)
                
            if self.use_log:
                # if use_log,
                # append log to self.logs
                self.logs.append({
                    'hit': is_hit,
                    'message': message
                })

    @abstractmethod
    def ready(self, target):
        '''
        This function is called 
        when scanner get target.
        (this function is optional)
        '''
        pass

    @abstractmethod
    def end(self):
        '''
        This function is called 
        when scanner process to end.
        (this function is optional)
        '''
        pass

    @abstractmethod
    def scan(self, target, signature):
        '''
        Get target and sginature,
        and compare target and signature.
        (this function is not optional,
        you must implement)
        '''
        raise NotImplementedError()
