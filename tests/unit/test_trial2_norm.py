import unittest
import csv

from trial2.trial2_norm import (
	Tcsv
	)


def get_mock_csv_path(filepath: str) -> list:
	"""
	Gets test csv data from file for use in assertions
	:param filepath:
	:return: mocked csv data as list
	"""
	with open(filepath, 'r', newline='') as f:
		test_csv_path = [row for row in csv.reader(f)]
		return test_csv_path


class TestTcsvViewr(unittest.TestCase):
	
	def setUp(self) -> None:
		self.csv_path = "unit_test_data/csv_data.csv"
	
	def test_topr_with_top_rows(self):
		mock_data_path = 'unit_test_data/testdata_topr_with_top_rows.csv'
		test_data = get_mock_csv_path(filepath=mock_data_path)
		test_func = Tcsv(self.csv_path).topr(4).tolist()
		self.assertEqual(test_data, test_func)


class TestTcsvFilter(unittest.TestCase):
	
	def setUp(self) -> None:
		self.csv_path = "unit_test_data/csv_data.csv"
	
	def test_filtr_raise_error_when_incorrect_value_type(self):
		values = 'software'
		with self.assertRaises(Exception):
			Tcsv(self.csv_path).filtr(values).tolist()
	
	def test_filtr_single_value_single_col(self):
		mock_data_path = 'unit_test_data/testdata_filtr_single_value_single_col.csv'
		test_data = get_mock_csv_path(filepath=mock_data_path)
		values = ['software']
		test_func = Tcsv(self.csv_path).filtr(values, 3).tolist()
		self.assertEqual(test_data, test_func)

	def test_filtr_single_value_all_col(self):
		mock_data_path = 'unit_test_data/testdata_filtr_single_value_all_col.csv'
		test_data = get_mock_csv_path(filepath=mock_data_path)
		values = ['software']
		test_func = Tcsv(self.csv_path).filtr(values).tolist()
		self.assertEqual(test_data, test_func)
	
	def test_filtr_multi_value_single_col(self):
		mock_data_path = 'unit_test_data/testdata_filtr_multi_value_single_col.csv'
		test_data = get_mock_csv_path(filepath=mock_data_path)
		values = ['seed', 'a']
		test_func = Tcsv(self.csv_path).filtr(values, 9).tolist()
		self.assertEqual(test_data, test_func)
	
	def test_filtr_multi_value_all_col(self):
		mock_data_path = 'unit_test_data/testdata_filtr_multi_value_all_col.csv'
		test_data = get_mock_csv_path(filepath=mock_data_path)
		values = ['mycityfaces', 'Gilbert', '5']
		test_func = Tcsv(self.csv_path).filtr(values).tolist()
		self.assertEqual(test_data, test_func)


class TestTcsvDelCol(unittest.TestCase):
	def setUp(self) -> None:
		self.csv_path = "unit_test_data/csv_data.csv"
	
	def test_delc_single_col(self):
		mock_data_path = 'unit_test_data/testdata_delc_single_col.csv'
		test_data = get_mock_csv_path(filepath=mock_data_path)
		index = [2]
		test_func = Tcsv(self.csv_path).delc(index).tolist()
		self.assertEqual(test_data, test_func)
	
	def test_delc_multi_col(self):
		mock_data_path = 'unit_test_data/testdata_delc_multi_col.csv'
		test_data = get_mock_csv_path(filepath=mock_data_path)
		index = [2, 5]
		test_func = Tcsv(self.csv_path).delc(index).tolist()
		self.assertEqual(test_data, test_func)
		
	def test_delc_multi_col_with_value_instead_of_index(self):
		# To be completed
		pass


class TestTcsvRepv(unittest.TestCase):
	def setUp(self) -> None:
		self.csv_path = "unit_test_data/csv_data.csv"
	def test_repv_single_value_all_col(self):
		mock_data_path = 'unit_test_data/testdata_repv_single_values_all_col.csv'
		test_data = get_mock_csv_path(filepath=mock_data_path)
		values = {'LifeLock': 'Goggle'}
		test_func = Tcsv(self.csv_path).repv(values).tolist()
		self.assertEqual(test_data, test_func)
	
	def test_repv_multi_values_all_col(self):
		mock_data_path = 'unit_test_data/testdata_repv_multi_values_all_col.csv'
		test_data = get_mock_csv_path(filepath=mock_data_path)
		values = {'LifeLock': 'Goggle', 'web': 'net', '5': '1billion'}
		test_func = Tcsv(self.csv_path).repv(values).tolist()
		self.assertEqual(test_data, test_func)
	
	def test_repv_multi_values_single_col(self):
		mock_data_path = 'unit_test_data/testdata_repv_multi_values_single_col.csv'
		test_data = get_mock_csv_path(filepath=mock_data_path)
		values = {'lifelock': 'deadlock', 'chosenlist-com': 'chosendictionary-org'}
		index = 0
		test_func = Tcsv(self.csv_path).repv(values, index).tolist()
		self.assertEqual(test_data, test_func)
	
	def test_repv_single_values_single_col(self):
		mock_data_path = 'unit_test_data/testdata_repv_single_values_single_col.csv'
		test_data = get_mock_csv_path(filepath=mock_data_path)
		values = {'lifelock': 'dreadlocks'}
		index = 0
		test_func = Tcsv(self.csv_path).repv(values, index).tolist()
		self.assertEqual(test_data, test_func)
		
	def test_repv_multi_values_with_named_col(self):
		# To be completed
		pass
		
	def test_repv_multi_values_with_named_col_2(self):
		# To be completed
		pass
		
class TestTcsvChain(unittest.TestCase):
	def setUp(self) -> None:
		self.csv_path = "unit_test_data/csv_data.csv"
	
	def test_chain_1(self):
		mock_data_path = 'unit_test_data/testdata_chain_1.csv'
		test_data = get_mock_csv_path(filepath=mock_data_path)
		fvals = ['web']
		rvals = {'lifelock': 'lockstock'}
		dvals = [2, 5]
		test_func = Tcsv(self.csv_path).filtr(fvals).repv(rvals).topr(3).delc(dvals).tolist()
		self.assertEqual(test_data, test_func)
		
	def test_chain_2(self):
		mock_data_path = 'unit_test_data/testdata_chain_2.csv'
		test_data = get_mock_csv_path(filepath=mock_data_path)
		fvals = ['b', 'software']
		rvals = {'web': 'interweb'}
		dvals = [4, 6]
		test_func = Tcsv(self.csv_path).topr(7).delc(dvals).repv(rvals).filtr(fvals).tolist()
		self.assertEqual(test_data, test_func)
		
	def test_chain_3(self):
		mock_data_path = 'unit_test_data/testdata_chain_3.csv'
		test_data = get_mock_csv_path(filepath=mock_data_path)
		fvals = ['seed', '4', '5']
		rvals = {'seed': 'pod'}
		dvals = [0]
		test_func = Tcsv(self.csv_path).filtr(fvals).repv(rvals).delc(dvals).tolist()
		# test_func = Tcsv(self.csv_path).filtr(fvals).tolist()
		self.assertEqual(test_data, test_func)
		
	def test_chain_4(self):
		mock_data_path = 'unit_test_data/testdata_chain_4.csv'
		test_data = get_mock_csv_path(filepath=mock_data_path)
		fvals = ['seed']
		findex = 9
		rvals = {'chosenlist-com': 'chosenlist.com'}
		rindex = 1
		dvals = [0]
		test_func = Tcsv(self.csv_path).filtr(fvals, findex).repv(rvals, rindex).delc(
			dvals).tolist()
		self.assertEqual(test_data, test_func)