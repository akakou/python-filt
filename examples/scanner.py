#!/usr/bin/env python
'''example/scanner.py
This is the sample code of scanner.
'''

from filt.scanner import BaseScanner 

# **DO NOT use** stdin and stdout.
# Scanner use them to communicate with filt.

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
