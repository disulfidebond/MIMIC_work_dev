import pandas as pd
import string, os, math
import numpy as np
from tqdm import tqdm
import random
from datetime import datetime
from collections import Counter

t = datetime.now()
ts_string = t.strftime('%m%d%Y_%H%M%S')

# location of input file and output directory
NOTES_CSV = '/LAB_SHARED/DATA/MIMIC/RAW/NOTEEVENTS.csv'
OUTDIR = '/LAB_SHARED/home/jrcaskey/MIMIC_tmpDir/'


# read in using tqdm for memory management and progress meter
frame_data = []
for df_chunk in tqdm(pd.read_csv(NOTES_CSV, chunksize=100000, error_bad_lines=False, engine='python')):
  frame_data.append(df_chunk)
frame = pd.concat(frame_data)


cols = list(frame)
subject_ID_series = frame['SUBJECT_ID'].values
subject_ID_series = subject_ID_series[~np.isnan(subject_ID_series)]
s_id_list = subject_ID_series.tolist()
hamid_series = frame['HADM_ID'].values
hamid_series = hamid_series[~np.isnan(hamid_series)]
hamid_list = hamid_series.tolist()
hamid_list_uniq = list(set(hamid_list))
category_series = frame['CATEGORY'].values
category_list = category_series.tolist()
category_list = list(filter(lambda x: x != '', category_list))
category_list_uniq = list(set(category_list))
desc_series = frame['DESCRIPTION'].values
desc_list = desc_series.tolist()
desc_list_uniq = list(set(desc_list))
desc_list = list(filter(lambda x: x != '', desc_list))
# desc_d = Counter(desc_list)

s = 'There are ' + str(len(list(set(s_id_list)))) + ' unique non-na subject IDs, and ' + str(len(s_id_list)) + ' total non-na subject IDs.'
print(s)
s = 'There are ' + str(len(list(set(hamid_list)))) + ' unique non-na Hospital Admission IDs, and ' + str(len(hamid_list)) + ' total non-na Hospital Admission IDs.'
print(s)
s = 'There are ' + str(len(list(set(category_list)))) + ' unique Category values, and ' + str(len(category_list_uniq)) + ' total Category values.'
print(s)

# get counts for each category
cat_dict = dict()
cat_dict['DESCRIPTION_NAMES'] = desc_list_uniq
c_df = frame.loc[frame['CATEGORY'] == 'Physician ',]
d_list = []
for d in tqdm(desc_list_uniq):
  d_df = c_df.loc[c_df['DESCRIPTION'] == d,]
  ct_d = len(d_df.index)
  d_list.append(ct_d)
cat_dict['Physician '] = d_list

# output to csv file
df_desc_itemized = pd.DataFrame(cat_dict, columns=cat_dict.keys())
df_desc_itemized.to_csv('ProgressNotes_MIMIC.csv', index=False)

print('job done')
