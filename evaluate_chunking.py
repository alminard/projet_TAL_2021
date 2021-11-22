#python evaluate_chunking.py file.conll
#evaluation of automatic chunking (semoral tool)
#file format : token \t ref \t sys
#ref and sys follow the BILOU annotation format
#seqeval : https://github.com/chakki-works/seqeval
from seqeval.metrics import accuracy_score
from seqeval.metrics import classification_report
from seqeval.metrics import f1_score

import sys

y_true = []
y_pred = []
sent_t = []
sent_p = []

f = open(sys.argv[1],"r")

for line in f :
    line = line.rstrip()

    if "\t" in line:
        elt = line.split("\t")
        t = elt[1]
        p = elt[2]
        #Modification of the annotation format : from BILOU to IOBES
        t = t.replace("L-", "E-").replace("U-","S-")
        p = p.replace("L-", "E-").replace("U-","S-")
        sent_t.append(t)
        sent_p.append(p)
    elif len(sent_t) > 0 and len(sent_t) == len(sent_p):
        y_true.append(sent_t)
        y_pred.append(sent_p)

        sent_t = []
        sent_p = []
f.close()

print (f1_score(y_true, y_pred))

print (accuracy_score(y_true, y_pred))

print (classification_report(y_true, y_pred))
