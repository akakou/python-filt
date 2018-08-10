# python-filt
## Overview
Python filt is the packeage for using [Filt](https://github.com/akakou/filt).  
You can use to make below.

### Filt Client
Use filt to check whether the target hits the signature.

### Filt Scanner
Get target and signature, check whether the target hits the signature, and return result to Filt.

## Installation
Type command below.

```sh
$ git clone https://github.com/akakou/python-filt
$ cd python-filt
$ sudo pip install .
```

## How to make scanner
### 1. project directory
Make the project folder.
```sh
$ mkdir sample
$ cd sample
```

### 2. `Settings.toml`
Make `Setting.toml` in project directory
```Settings.toml
# this is sample/Settings.toml
excutable_file = "scanner.py"
```

### 3. python file
Make python file and write like below.
```python
#!/usr/bin/env python
"""
This is sample/scanner.py
"""

from filt.scanner import BaseScanner 

# **DO NOT use** stdin and stdout.
# Scanner use them to communicate with filt.

class SampleScanner(BaseScanner):
    def scan(self, target, signature):
        """
        Check target and signature,
        and return is_hit(bool) and message(str).
        """
        # WRITE HERE
        return (is_hit, message)

if __name__ == '__main__':
    # run scanner
    sample_scanner = SampleScanner()
    sample_scanner.run()
```

## How to make client
Make python file and write like below.

```python
#!/usr/bin/env python
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
```
