from pngcrcpy import pngcrc
from struct import pack


def crc_formatted(s):
	'''
		crc formatted for writing to file
		(four bytes)
		'''
	return pack('>L', pngcrc.crc(s))

def len_formatted(l):
	'''
		length of chunk formatted for writing to file
		(four bytes)
		'''
	return pack('>L', l)


def create_png(name):
	'''
		Create new png file
		Return file handle
		'''
	f = open(name, 'wb')

	f.write('\x89\x50\x4e\x47\x0d\x0a\x1a\x0a')	# PNG file header
	return f

def write_chunk(type, data, f):
	'''
		Write PNG chunk to f (file handle)
		Append length and prepend CRC
		Both type and data should be arrays of bytes
		'''
	l = len(data)				# length
	f.write(len_formatted(l))

	for b in type:	f.write(b)	# type
	for b in data:	f.write(b)	# data

	str = ''.join(type) + ''.join(data)
	f.write(crc_formatted(str))	# crc
