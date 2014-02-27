#!/usr/bin/python
"""Script can be used to calculate the Gini Index of a column in a CSV file.

Classes are strings."""

import fileinput
import csv
import json
from collections import defaultdict, Counter

(
    CMTE_ID, AMNDT_IND, RPT_TP, TRANSACTION_PGI, IMAGE_NUM, TRANSACTION_TP,
    ENTITY_TP, NAME, CITY, STATE, ZIP_CODE, EMPLOYER, OCCUPATION,
    TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID, CAND_ID, TRAN_ID, FILE_NUM,
    MEMO_CD, MEMO_TEXT, SUB_ID
) = range(22)

CANDIDATES = {
    'P80003338': 'Obama',
    'P80003353': 'Romney',
}

############### Set up variables
# TODO: declare datastructures
candidates_two= defaultdict(int)
count = 0.0
cand = defaultdict(lambda: defaultdict(int))

############### Read through files

for row in csv.reader(fileinput.input(files=('itpas2.txt')), delimiter='|'):
    candidate_id = row[CAND_ID]
    if candidate_id not in CANDIDATES:
        continue
    candidate_name = CANDIDATES[candidate_id]
    zip_code = row[ZIP_CODE]
    count += 1
    candidates_two[candidate_name] += 1
    cand[zip_code][candidate_name] += 1

    ###
    # TODO: save information to calculate Gini Index
    ##/

gini_final_zip = []
for i in cand:
    donate_zip = float(sum(cand[i][j] for j in cand[i]))

    cand_zip = []
    for j in cand[i]:
        gini_one = (cand[i][j] / donate_zip)**2
        cand_zip.append(gini_one)

    score_with_weight = (1 - sum(cand_zip)) * (donate_zip / count)
    gini_final_zip.append(score_with_weight)


###
# TODO: calculate the values below:
gini = 1 - sum((candidates_two[j] / count)** 2 for j in candidates_two)  # current Gini Index using candidate name as the class
split_gini = sum(gini_final_zip)  # weighted average of the Gini Indexes using candidate names, split up by zip code
##/

print "Gini Index: %s" % gini
print "Gini Index after split: %s" % split_gini
