"""
The intent of this program is to process the data output from the big query to further process in ML. This is the python version. We'll code in Go again to learn about golang.
"""
import pandas as pd
import base64
import time
import urllib

def main():
    src_file = input("Please open the filename: ") # Default is json. TODO we have to do the validation here.

    if src_file is None or src_file is '':
       src_file = '~/work/attack.2018-04-11.json' 

    df = ''

    with open(src_file,'r') as f:
        df = pd.read_json(f)
        df = b64decoding(df)
    export_to_csv(df)

    return 0

def b64decoding(df):
    '''
    decode the specific column to base64 decoding 
    '''
    df['logdata'] = list(map(lambda x: urllib.parse.unquote(base64.b64decode(x + "===").decode('latin1')), df['logdata'])) # Strip non-ascii character
    return df

# export to xls
def export_to_excel(json):
    filename = "output+%f" % time.time()
    return json.to_excel(filename,sheet_name='exported')

def export_to_csv(frame):
    filename = "output+%f.csv" % time.time()
    with open(filename,'w') as f:
        f.write(pd.DataFrame.to_csv(frame))

if __name__ == '__main__':
    main()
