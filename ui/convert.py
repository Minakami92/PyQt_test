#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import uic
 
fin = open('form.ui', 'r')
fout = open('form.py', 'w')
uic.compileUi(fin,fout,execute=False)
fin.close()
fout.close()
