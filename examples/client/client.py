#!/usr/bin/env python
'''example/scanner.py
This is the sample code of client.
'''

from filt.client import FiltClient


def main():
    # set param
    url = 'https://localhost:3000'
    target = "hello world"
    option = {"hoge": "fuga"}

    # construct filt client
    filt = FiltClient(url)

    # send data to filt
    result = filt.send(target, verify=False)
    print(result)

    # add option and send data 
    result = filt.send(target, option=option, verify=False)
    print(result)


if __name__ == '__main__':
    main()