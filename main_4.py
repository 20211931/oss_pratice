#1
# s = 'cafe'
# len(s)
# b = s.encode('utf8')
# b
# len(b)
# b.decode('utf8')

#2
# cafe = bytes('cafe', encoding='utf8')
# cafe
# cafe[0]
# cafe[:1]
# cafe_arr = bytearray(cafe)
# cafe_arr
# cafe-arr[-1:]

#3
# bytes.fromhex('31 4B CE A9')

#4
# import array
# numbers = array.array('h', [-2,-1,0,1,2])
# numbers
# octects = bytes(numbers)
# octects


# 5
# import struct
# fmt = '<3s3sHH'
# with open('./simsoms.gif', 'rb') as fp:
#   img = memoryview(fp.read())
# header = img[:10]
# bytes(header)
# struct.unpack(fmt, header)
# del header
# del img


# 6
# for codec in ['latin_1', 'utf8', 'uft16']:
#   print(codec, 'El Nino'.encode(codec), sep='\t')
# for codec in ['ascii', 'latin_1', 'cp1252', 'cp437', 'utf8', 'utf-16le', 'gb2312']:
#   print(codec, 'A'.encode(codec), sep='\t')


# 7
# city = 'Sao Paulo'
# city.encode('utf-8')
# city.encode('utf_16')
# city.encode('iso8859_1')
# city.encode('cp437', errors = 'ignore')
# city.encode('cp437', errors = 'replace')
# city.encode('cp437', errors = 'xmlcharrefreplace')

# 8
# octects = b'Montr\xe9al'
# octects.decode('cp1252')
# octects.decode('iso8859_7')
# octects.decode('koi8_r')
# octects.decode('utf8')
# octects.decode('utf8', errors='replace')
# 'e'.encode(utf8)

# 9
# u16 = 'El Nino'.encode('utf16')
# u16
# list(u16)
# u16le = 'El Nino'.encode('utf_16le')
# list(u16le)
# u16be = 'El Nino'.encode('utf_16be')
# list(u16be)