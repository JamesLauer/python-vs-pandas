import cProfile
import sys
import time
import pandas as pd
from trial1.trial1_norm import Tcsv
from trial1.trial1_gen import TcsvGen

file_path = "../raw_data/region41_en.csv"
filter_words = ['Toyota']
replace_words = {'Land Cruiser': 'Sea Surfer'}
# For Standard and Generator Class'
delete_cols_index = [2, 5]
# Column names corresponding to index's in "delete_cols_index" for Pandas input
delete_cols_name = ['bodyType', 'year']


def time_it_decorator(func):
	def time_it(*args, **kwargs):
		start = time.time()
		func_return = func(*args, **kwargs)
		end = time.time()
		print(f"{func}:")
		print("Execution time: ", end - start)
		print()
		return func_return
	return time_it


@time_it_decorator
def norm():
	transform = (Tcsv(filepath=file_path)
				 .filtr(filter_words)
				 .repv(replace_words)
				 .delc(delete_cols_index)
				 .tolist()
				 )
	return transform


@time_it_decorator
def gen():
	transform = (TcsvGen(filepath=file_path)
				 .filtr(filter_words)
				 .repv(replace_words)
				 .delc(delete_cols_index)
				 .tolist()
				 )
	return transform


@time_it_decorator
def pandas():
	df = pd.read_csv(file_path)
	filtr = df[
		df.applymap(lambda x: any(keyword in str(x) for keyword in filter_words)).any(
			axis=1)]
	repv = filtr.replace(replace_words)
	view = repv.head(None)
	delc = view.drop(columns=delete_cols_name)
	header = delc.columns.tolist()
	body = delc.values.tolist()
	print("Size of df object: ", sys.getsizeof(body))
	return [header] + body


# norm = norm()
# gen = gen()
# pandas = pandas()

# cProfile.run('norm()', sort='time')
cProfile.run('gen()', sort='time')
# cProfile.run('pandas()', sort='time')
