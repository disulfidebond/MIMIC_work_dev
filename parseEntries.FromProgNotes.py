import pandas as pd
import string, os, math
import numpy as np
from tqdm import tqdm
import random
from datetime import datetime
from collections import Counter

t = datetime.now()
ts_string = t.strftime('%m%d%Y_%H%M%S')

NOTES_CSV = '/LAB_SHARED/DATA/MIMIC/RAW/NOTEEVENTS.csv'
OUTDIR = '/LAB_SHARED/home/jrcaskey/MIMIC_tmpDir/'

print('importing data')
frame_data = []
# TQDM shows a progress bar as it imports, and can manage memory allocation
for df_chunk in tqdm(pd.read_csv(NOTES_CSV, chunksize=100000, error_bad_lines=False, engine='python')):
  frame_data.append(df_chunk)
frame = pd.concat(frame_data)


# requires file with a subset of description names to filter
df_progNotes = pd.read_csv('ProgressNotes_MIMIC.csv')
df_categories = df_progNotes['DESCRIPTION_NAMES'].tolist()


# select only Physician category, and only the descriptions in ProgressNotes
c_df = frame.loc[frame['CATEGORY'] == 'Physician ',]
d_list = []
print('selecting descriptions from the categories provided')
for d in tqdm(df_categories):
  d_df = c_df.loc[c_df['DESCRIPTION'] == d,]
  d_list.append(d_df)

# ensure there are no duplicated HADM_ID values
df_concat = pd.concat(d_list)
df_out = df_concat.drop_duplicates(subset=['HADM_ID'])
df_out = df_out.dropna(subset=['HADM_ID'])
# sample 5000 values randomly
df_sampled = df_out.sample(n=5000, random_state=42, replace=False)

# create output files
for rowid, hadmid, desc, text in zip(df_sampled.ROW_ID, df_sampled.HADM_ID, df_sampled.DESCRIPTION, df_sampled.TEXT):
  if pd.isnull(hadmid):
    print('empty hadmid for rowid', rowid)
  else:
    header = 'HADMID:' + str(int(hadmid)) + ',' + 'DESCRIPTION:' + str(desc) + '\n'
    printable = ''.join(c for c in text if c in string.printable)
    with open('%s%s.txt' % (OUTDIR, int(hadmid)), 'a') as outfile:
      outfile.write(header)
      outfile.write(printable + '\n')
      outfile.write('\n************\n\n')
