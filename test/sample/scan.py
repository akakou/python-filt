#!/usr/bin/env python
'''test/sample/scan.py
This is the test case of scanner.
'''

import os, sys
sys.path.append(os.getcwd())

# import library which is 
# at higher order directory (filt)
path = os.path.dirname(os.path.abspath(__file__))
path = path.split('/')
path.pop()
path.pop()
path = '/'.join(path)
sys.path.append(path)

from filt.scanner import BaseScanner 


class SampleScanner(BaseScanner):
    '''
    This is the sample scanner.
    '''

    def scan(self, target, signature):
        '''
        Check target and signature are same.
        '''
        if target == signature:
            return (True, 'same')
        else:
            return (False, 'hoge')


if __name__ == '__main__':
    # run scanner
    sample_scanner = SampleScanner()
    sample_scanner.run()
