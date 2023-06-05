import sys

import pandas as pd

filepath_csv = "../raw_data/csv_data.csv"


def chain(path, fval=None, rval=None, dval=None, vval=None):
	df = pd.read_csv(path)
	filt = df[df.applymap(lambda x: 'Toyota' in str(x)).any(axis=1)]
	repl = filt.replace(rval)
	view = repl.head(vval)
	delc = view.drop(columns=dval)
	header = delc.columns.tolist()
	body = delc.values.tolist()
	print("Size of df object: ", sys.getsizeof(body))
	return [header] + body



