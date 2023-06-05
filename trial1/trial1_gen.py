import csv
import re
import sys
from typing import Optional


class TcsvGen:
	def __init__(self, filepath):
		self.filepath = filepath
		self.file = open(self.filepath, 'r', encoding='utf8')
		self.reader = csv.reader(self.file)
		self.header = [next(self.reader)]
		
		
	def topr(self, num: int):
		# Returns TypeError if value is not an integer
		if not isinstance(num, int):
			raise TypeError("Value must be of integer type")
		
		# Returns number of rows as specified by num
		rows = []
		for i, row in enumerate(self.reader):
			if i >= num:
				break
			rows.append(row)
		self.reader = rows
	
		return self
	
	def filtr(self, value: list, col_ind: Optional[int] = None):
		# Returns TypeError if value is not a list
		if not isinstance(value, list):
			raise TypeError("Value must be of list type")
		
		# Filters value(s) if no column index provided
		elif col_ind is None:
			value_pattern = "|".join(r"\b{}\b".format(v) for v in value)
			self.reader = (
				row for row in self.reader if re.search(value_pattern, ",".join(row), re.IGNORECASE))
			
		# Filters value(s) if column index entered
		else:
			self.reader = (row for row in self.reader for values
						   in value if row[col_ind] == values)
		return self
	
	def repv(self, values_dict: dict, col_ind: Optional[int] = None):
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
		
		self.reader = (replace_values(row) for row in self.reader)
		return self

	def delc(self, col_index: list[int]):
		self.reader = ([col[i] for i in range(len(col)) if i not in
						sorted(col_index, reverse=True)] for col in self.reader)
		
		self.header = ([col[i] for i in range(len(col)) if i not in
						sorted(col_index, reverse=True)] for col in self.header)
		return self

	def tolist(self):
		print("Size of self.reader object: ", sys.getsizeof(self.reader))
		header = [row for i, row in enumerate(self.header) if i == 0]
		# Append rows to header
		for row in self.reader:
			header.extend([row])
		self.reader = header
		self.file.close()
		return list(self.reader)
	
	def tocsv(self, to_csv_path=None):
		print("Size of self.reader object: ", sys.getsizeof(self.reader))
		header = [row for i, row in enumerate(self.header) if i == 0]
		# Append rows to header
		for row in self.reader:
			header.extend([row])
		self.reader = header
		with open(to_csv_path, 'w', newline='', encoding='utf-8') as f:
			writer = csv.writer(f)
			writer.writerows(self.reader)