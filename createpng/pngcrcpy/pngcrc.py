# From http://www.libpng.org/pub/png/spec/1.1/PNG-CRCAppendix.html

# Table of CRCs of all 8-bit messages.
crc_table = [0] * 256
crc_table_computed = 0;
   
def make_crc_table():
	'''
		Make the table for a fast CRC.
		'''
	global crc_table, crc_table_computed

	for n in range(0,256):
		c = n

		for k in range(0,8):
			if c & 1:
				c = 0xedb88320L ^ (c >> 1)
			else:
				c = c >> 1

		crc_table[n] = c

	crc_table_computed = 1
   

def update_crc(crc, str):
	global crc_table, crc_table_computed

	c = crc
	if not crc_table_computed:
		make_crc_table()
	for n in range(0,len(str)):
		index = (c ^ ord(str[n])) & 0xff
		c = crc_table[index] ^ (c >> 8)
	return c


def crc(str):
	return update_crc(0xffffffffL, str) ^ 0xffffffffL

