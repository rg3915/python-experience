# -*- coding: utf-8 -*-
'''
Parâmetros de entrada:
python word_to_pdf.py <in_file.doc> <out_file.pdf>
python word_to_pdf.py file.doc file.pdf
'''
import os
import sys
import urllib2

# the input docx
file = os.path.abspath(sys.argv[1])
in_file = open(file, 'rb')
out_file = os.path.abspath(sys.argv[2])

data = in_file.read()

#set up the request
req = urllib2.Request("http://converter-eval.plutext.com:80/v1/00000000-0000-0000-0000-000000000000/convert", data)
req.add_header('Content-Length', '%d' % len(data))
req.add_header('Content-Type', 'application/octet-stream')

# make the request
res = urllib2.urlopen(req)

# write the response to a file
pdf = res.read()
f = open(out_file, 'wb')
f.write(pdf)