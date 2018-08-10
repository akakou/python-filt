#!/usr/bin/env python
'''test/sample/scan.py
This is the test case of scanner.
'''

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
