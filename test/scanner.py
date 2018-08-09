#!/usr/bin/env python
'''example/scanner.py
This is test code of scanner.
'''
import unittest
import subprocess


class TestInheritancedScanner(unittest.TestCase):
    '''
    Test class of filt/scanner.py
    (the class base is example/scanner.py)
    '''

    def test_scan_same(self):
        '''
        test method for scan same data
        '''
        # params
        param1 = 'Zml6eg=='
        param2 = 'Zml6eg=='
        param3 = ''

        expected = 'eyJoaXQiOiAidHJ1ZSIsICJtZXNzYWdlcyI6IFsic2FtZSJdfQ=='

        cmd = f'''echo '{param1}\n{param2}\n{param3}\n' | python sample/scan.py'''
        actual = subprocess.getoutput(cmd)

        self.assertEqual(expected, actual)

    def test_scan_different(self):
        '''
        test method for scan different data
        '''
        # params
        param1 = 'Zml6eg=='
        param2 = 'YnV6eg=='
        param3 = ''

        expected = 'eyJoaXQiOiAiZmFsc2UiLCAibWVzc2FnZXMiOiBbXX0='

        cmd = f'''echo '{param1}\n{param2}\n{param3}\n' | python sample/scan.py'''
        actual = subprocess.getoutput(cmd)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    # run scanner
    unittest.main()
