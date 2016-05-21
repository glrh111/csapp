import unittest
from chapter11 import hex2dd

class Test1(unittest.TestCase):
	hex_ip = 0x8002c2f2
	dd_ip = '128.2.194.242'
	def test_hex2dd(self):
		self.assertTrue(hex2dd(self.hex_ip) == self.dd_ip)

if __name__ == '__main__':
	unittest.main()	

