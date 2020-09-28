# Very simple code to apply Correlates of War country codes

import pandas as pd
import os.path

COW_PATH = os.path.join(
    os.path.split(os.path.abspath(__file__))[0], "cow_codes.csv"
)

CODE = 'CCode'
NAME = 'StateNme'

#import the cow codes df - it is ALREADY sorted by ccode number
cow_data = pd.read_csv(COW_PATH, sep=',', header=0)

#Finds country code(s) and returns the state name(s)
#if multiple codes, return a tuple with same shape as codes
#round_up
def code_to_name(ccodes, round_up=True):
    if round_up:
        idxs = cow_data[CODE]].searchsorted(ccodes, side='left')
        return cow_data.loc[idxs][NAME].tolist()
    else:
        idxs = [0] * len(ccodes)
        for i in range(len(ccodes)):
            #idxmax handles duplicates in the cow data file
            c = ccodes[i]
            idx = (cow_data[CODE] == c).idxmax()
            #if idx = 0, c should be 2, the first valid code. otherwise there was no match.
            if idx == 0 and c != 2:
                idxs[i] = None
            else:
                idxs[i] = idx
        return cow_data.loc[idxs][NAME].tolist()