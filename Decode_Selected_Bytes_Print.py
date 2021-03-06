#!/usr/bin/env python
__version__    = "0.0.1"
__date__       = "07.03.2013"
__author__     = "Joseph Zeranski"
__maintainer__ = "Joseph Zeranski"
__email__      = "madsc13ntist gmail.com"
__copyright__  = "Copyright 2013, " + __author__
__license__    = "MIT"
__status__     = "Prototype"
__credits__    = [""]
__description__= "Use IDAPython to perform a decoding operation on each selected byte in IDA Pro. and print the (printable) results."

####################### MIT License ####################### 
# Copyright (c) 2013 Joseph Zeranski
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
###########################################################

import os
from time import strftime

def decoder(byte):
	"""XOR each byte by 0xf3 (243)"""
	return byte ^ 0xf3

def printByte(byte):
	return str(hex(byte).lstrip("0x")).zfill(2)

########################### MAIN ###########################
if __name__ == '__main__':
	print("\n-------------------- %s ------------------------------" % (os.path.basename(__file__)))
	print("[%s]" % (strftime("%Y-%m-%d %H:%M:%S")))
	print("Desc: %s" % (decoder.__doc__))
	print("Offsets: 0x%x-0x%x  (%d bytes)" % (SelStart(), SelEnd(), SelEnd() - SelStart()))
	orig_bytes    = []
	decoded_bytes = []
	ascii_bytes   = []
	for b in range(SelStart(), SelEnd()+1):
		orig_byte = GetOriginalByte(b)
		decoded_byte = decoder(orig_byte)
		orig_bytes.append(printByte(orig_byte))
		decoded_bytes.append(printByte(decoded_byte))
		try:
			if chr(decoded_byte) == '\n':
				ascii_bytes.append('\\n')
			elif chr(decoded_byte) == '\r':
				ascii_bytes.append('\\r')
			elif chr(decoded_byte) == '\t':
				ascii_bytes.append('\\t')
			else:
				ascii_bytes.append(chr(decoded_byte))
		except:
			ascii_bytes.append("%s" % (printByte(decoded_byte)))
	
	print("\norig:\t%s"   % (" ".join(orig_bytes)))
	print("decode:\t%s"   % (" ".join(decoded_bytes)))
	print("ASCII:\t%s"    % ("".join(ascii_bytes)))
	
		
