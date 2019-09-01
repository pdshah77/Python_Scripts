'''
	Write a Program to Implement a PrefixMapSum class with the following methods:

insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value.
sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.

	Developed By: Parth Shah
	Python Version: Python 3.7
	
'''

class PrefixMapSum:
	map_dict = {}
	
	def insert(self,key,value):
		self.map_dict[key] = value
		
	def sum(self,prefix):
		sum = 0
		leng = len(prefix)
		for key,value in self.map_dict.items():
			if key[:leng] == prefix:
				sum += value
		print(sum)

mapsum = PrefixMapSum()

mapsum.insert("columnar", 3)
mapsum.sum("col")
#assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
mapsum.sum("col")
#assert mapsum.sum("col") == 5
