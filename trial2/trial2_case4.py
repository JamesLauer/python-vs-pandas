import cProfile
import sys
import time
import pandas as pd
from trial2.trial2_norm import Tcsv
from trial2.trial2_gen import TcsvGen

file_path = "../raw_data/region41_en.csv"
filter_words = ['Toyota',
				'Nissan',
				'Volkswagen']
replace_words = {'Land Cruiser': 'Sea Surfer',
				 'X-Trail': 'Trail-Z',
				 'Tiguan': 'Siguan'}
# For Standard and Generator Class'
delete_cols_index = [2, 5, 6, 8]
# Column names corresponding to index's in "delete_cols_index" for Pandas input
delete_cols_name = ['bodyType', 'year', 'mileage', 'power']
top_rows = 10000


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
				 .topr(top_rows)
				 .repv(replace_words)
				 .delc(delete_cols_index)
				 .tolist()
				 )
	return transform


@time_it_decorator
def gen():
	transform = (TcsvGen(filepath=file_path)
				 .filtr(filter_words)
				 .topr(top_rows)
				 .repv(replace_words)
				 .delc(delete_cols_index)
				 .tolist()
				 )
	return transform


@time_it_decorator
def pandas():
	df = pd.read_csv(file_path)
	if len(filter_words) == 1:
		filtr = df[df.astype(str).apply(
			lambda x: x.str.contains('|'.join(filter_words), regex=False)).any(axis=1)]
	else:
		filtr = df[
			df.applymap(lambda x: any(keyword in str(x) for keyword in filter_words)
				).any(axis=1)]
	repv = filtr.replace(replace_words)
	view = repv.head(top_rows)
	delc = view.drop(columns=delete_cols_name)
	header = delc.columns.tolist()
	body = delc.values.tolist()
	print("Size of df object: ", sys.getsizeof(body))
	return [header] + body

# norm = norm()
# gen = gen()
# pandas = pandas()

# cProfile.run('norm()', sort='time')
# cProfile.run('gen()', sort='time')
cProfile.run('pandas()', sort='time')
