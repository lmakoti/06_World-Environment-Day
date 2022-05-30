from pyjstat import pyjstat

EXAMPLE_URL = 'http://json-stat.org/samples/galicia.json'

# read from json-stat
dataset = pyjstat.Dataset.read(EXAMPLE_URL)

# write to dataframe
df = dataset.write('dataframe')
print(df)

# read from dataframe
dataset_from_df = pyjstat.Dataset.read(df)

# write to json-stat
print(dataset_from_df.write())