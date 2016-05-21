# -*- coding: utf-8 -*-
def hex2dd(hexno):
	def iter(product, no, count):
		if count < 0:
			return product
		return iter(product+[int(no/0x10**count)], no % 0x10**count, count-2)

	return '.'.join(map(str, (iter([], hexno, 6))))

	