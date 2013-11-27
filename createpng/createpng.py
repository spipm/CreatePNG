import createpng_lib as createpng

from sys import argv

# converting chunk types
typearr = {'IHDR': ['\x49', '\x48', '\x44', '\x52'],
			'IEND':['\x49', '\x45', '\x4e', '\x44'],
			'IDAT':['\x49', '\x44', '\x41', '\x54'],
			'tEXt':['\x74', '\x45', '\x58', '\x74'],
			'zTXt':['\x7a', '\x54', '\x58', '\x74'],
			'iTXt':['\x69', '\x54', '\x58', '\x74'],
			'pHYs':['\x70', '\x48', '\x59', '\x73'],
			'sPLT':['\x73', '\x50', '\x4c', '\x54'],
			'iCCP':['\x69', '\x43', '\x43', '\x50'],
			'gAMA':['\x67', '\x41', '\x4d', '\x41'],
			'cHRM':['\x63', '\x48', '\x52', '\x4d'],
			}


###
# create new png with png identifier
f = createpng.create_png(argv[1])



#--------------------------------------------------------------------------
###
# IHDR		(Basic header)
'''
			http://www.libpng.org/pub/png/spec/1.1/PNG-Chunks.html#C.IHDR
   Width:              4 bytes
   Height:             4 bytes
   Bit depth:          1 byte
   Color type:         1 byte
   Compression method: 1 byte
   Filter method:      1 byte
   Interlace method:   1 byte
   '''
createpng.write_chunk(typearr['IHDR'], 
			['\x00', '\x00', '\x00', '\x01',	# width
			'\x00', '\x00', '\x00', '\x01', 	# height
			'\x08',								# bit depth
			'\x00',								# color type
			'\x00',								# compression method
			'\x00',								# filter method
			'\x00']								# interlace method
			, f)


#--------------------------------------------------------------------------
###
# pHYs		(The pHYs chunk specifies the intended pixel size or aspect ratio for display of the image. It contains:
#
#   Pixels per unit, X axis: 4 bytes (unsigned integer)
#   Pixels per unit, Y axis: 4 bytes (unsigned integer)
#   Unit specifier:          1 byte


#--------------------------------------------------------------------------
###
# sPLT

# 
#   Palette name:    1-79 bytes (character string)
#   Null terminator: 1 byte
#   Sample depth:    1 byte
#   Red:             1 or 2 bytes
#   Green:           1 or 2 bytes
#   Blue:            1 or 2 bytes
#   Alpha:           1 or 2 bytes
#   Frequency:       2 bytes

#--------------------------------------------------------------------------
###
# gAMA

# 4 bytes

#--------------------------------------------------------------------------
###
# cHRM

#   White Point x: 4 bytes
#   White Point y: 4 bytes
#   Red x:         4 bytes
#   Red y:         4 bytes
#   Green x:       4 bytes
#   Green y:       4 bytes
#   Blue x:        4 bytes
#   Blue y:        4 bytes

# Each value is encoded as a 4-byte unsigned integer, representing the x or y value times 100000. For example, a value of 0.3127 would be stored as the integer 31270. 



#--------------------------------------------------------------------------
###
# A zTXt chunk contains:

#   Keyword:            1-79 bytes (character string)
#   Null separator:     1 byte
#   Compression method: 1 bytes			has to be zero
#   Compressed text:    n bytes			is zlib compression

#--------------------------------------------------------------------------
###
# iTXt International textual data
# This chunk is semantically equivalent to the tEXt and zTXt chunks, but the textual data is in the UTF-8 encoding of the Unicode character set instead of Latin-1. This chunk contains:

#   Keyword:             1-79 bytes (character string)
#   Null separator:      1 byte
#   Compression flag:    1 byte
#   Compression method:  1 byte
#   Language tag:        0 or more bytes (character string)
#   Null separator:      1 byte
#   Translated keyword:  0 or more bytes
#   Null separator:      1 byte
#   Text:                0 or more bytes

#--------------------------------------------------------------------------
###
# iCCP

#   Keyword:            1-79 bytes (character string)
#   Null separator:     1 byte
#   Compression method: 1 bytes			has to be zero
#   Compressed text:    n bytes			is zlib compression



#--------------------------------------------------------------------------
###
# IDAT		(actual image data)

import zlib

# 1x1 pixel image data
d = '\x01\xea'

z = [i for i in zlib.compress(d)]

createpng.write_chunk(typearr['IDAT'], z, f)


#--------------------------------------------------------------------------
###
# tEXt 




#--------------------------------------------------------------------------
###
# IEND		(End of PNG)
createpng.write_chunk(typearr['IEND'], [], f)


f.close()