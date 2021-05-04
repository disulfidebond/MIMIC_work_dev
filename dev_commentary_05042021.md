# Overview
The data to be parsed is on Janus in the file NOTEEVENTS.csv

This has the following schema:
COLUMN1,COLUMN2,...,COLUMN_N

Where Columns 1...n-1 are set values, and COLUMN_N is a long free-form text field with multiple entries.

The columns are defined as:
* ROW_ID: Integer starting at 1
* SUBJECT_ID: 5+ digit integer
* HADM_ID: likely Hospital Admission ID, 6+ digit integer
* CHARTDATE: obfucated date string with the format NNNN-NN-NN
* CHARTTIME: appears to be all empty values or np.nan in a pandas dataframe
* STORETIME: same as CHARTTIME
* CATEGORY: appears to be only one value, 'Discharge summary'
* DESCRIPTION: appears to be only one value, 'Report'
* CGID: appears to be all empty values, or np.nan in a pandas dataframe
* ISERROR: appears to be all empty values, or np.nan in a pandas dataframe
* TEXT: Example is below.

> Service:

> ADDENDUM:

> MAGICAL STUDIES: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum

> THORAX CT: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore

