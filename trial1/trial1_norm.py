import csv
import re
import sys
from typing import Optional


class Tcsv:
	def __init__(self, filepath):
		data = []
		self.filepath = filepath
		with open(self.filepath, 'r', encoding='utf8') as f:
			for line in f:
				data.append(line.strip().split(','))
		self.reader = data[1:]
		self.header = data[0]

	def topr(self, num: int):
		"""
		- Return top number of rows
		- To view top 150 rows: rows = Tcsv(filepath).topr(150).tolist()
		:param num: Number of rows to return (required)
		:return: list of rows
		"""
		# Returns TypeError if value is not an integer
		if not isinstance(num, int):
			raise TypeError("Value must be of integer type")
		
		# Appends top number (num) of rows to list
		self.reader = [row for i, row in enumerate(self.reader) if i <= num - 1]
		return self
	
	def filtr(self, value: list, col_ind: Optional[int] = None):
		"""
		- Filters rows based on input list and column index
		- To filter "Toyota" and "Mazda" in column 2: Tcsv().filter(["Toyota", "Mazda], 2).tolist()
		- To filter "Toyota" in all columns: Tcsv().filter(["Toyota"]).tolist()
		:param value: List of values to return (required)
		:param col_ind: Index of column to filter (optional)
		:return: Class object, requires.tolist() method to convert to list
		"""
		# Returns TypeError if value is not a list
		if not isinstance(value, list):
			raise TypeError("Value must be of list type")

		elif col_ind is None:
			value_pattern = "|".join(r"\b{}\b".format(v) for v in value)
			self.reader = [row for row in self.reader if re.search(value_pattern, ",".join(row), re.IGNORECASE)]
			
		# Filters value(s) if column index entered
		else:
			self.reader = [row for row in self.reader for values in value if row[col_ind] == values]
		return self
	
	def delc(self, col_index: list[int]):
		"""
		- Deletes column based on index values given
		- E.g. to delete column indexes 0 and 5:
		del_colums = Tcsv(csv_data).delc([0, 5]).tolist()
		:param col_index: List of column indexes (required)
		:return: Class object, requires.tolist() method to convert to list
		"""

		self.reader = [[col[i] for i in range(len(col)) if i not in
						sorted(col_index, reverse=True)] for col in self.reader]
		
		header = [[col[i] for i in range(len(col)) if i not in
						sorted(col_index, reverse=True)] for col in [self.header]]
		
		self.header = [*header][0]
		
		return self
	
	def repv(self, values_dict: dict, col_ind: Optional[int] = None):
		"""
		- replaces value from key value pair in column index
		- E.g. to replace "Facey" with "Facebook" and "Redthis" with "Reddit":
		replaced = Tcsv(csv_data).repv({"Facey": "Facebook", "Redthis": "Reddit"}.tolist()
		:param values_dict: Dictionary of key value pairs (required)
		:param col_ind: Index of column to replace values in (optional)
		:return: Class object, requires.tolist() method to convert to list
		"""
	
		def replace_values(row):
			# Replaces values if column index specified
			if col_ind is not None:
				if row[col_ind] in values_dict:
					row[col_ind] = values_dict[row[col_ind]]
			# Replaces values if no index specified
			else:
				for i, col in enumerate(row):
					if col in values_dict:
						row[i] = values_dict[col]
			return row
		
		self.reader = [replace_values(row) for row in self.reader]
		return self
	
	def tolist(self):
		print("Size of self.reader object: ", sys.getsizeof(self.reader))
		header = [self.header]
		# Append rows to header
		for row in self.reader:
			header.extend([row])
		self.reader = header
		return list(self.reader)
	
	def tocsv(self, to_csv_path=None):
		print("Size of self.reader object: ", sys.getsizeof(self.reader))
		header = [self.header]
		# Append rows to header
		for row in self.reader:
			header.extend([row])
		self.reader = header
		with open(to_csv_path, 'w', newline='', encoding='utf-8') as f:
			writer = csv.writer(f)
			writer.writerows(self.reader)
	