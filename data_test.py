import pandas as pd

raw_url = 'https://raw.githubusercontent.com/CJTAYL/USL/main/seeds_dataset.txt'
df = pd.read_csv(raw_url, delim_whitespace=True, header=None)