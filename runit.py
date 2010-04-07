#!/usr/bin/env python
# runit.py

import os
from os.path import expanduser

pid = os.fork()
if not pid:
    os.execl(expanduser("~")+"/.distrofy_plugin/getHotBabe.py")
os.wait()[0]
