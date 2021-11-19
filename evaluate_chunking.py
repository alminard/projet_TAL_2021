#python evaluate_chunking.py file.conll
from seqeval.metrics import accuracy_score
from seqeval.metrics import classification_report
from seqeval.metrics import f1_score

import sys

y_true = []
y_pred = []
f = open(sys.argv[1],"r")
sent_t = []
sent_p = []
for line in f :
    line = line.rstrip()
    if "\t" in line:
        elt = line.split("\t")
        t = elt[1]
        p = elt[2]
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

#print (y_true)
#print (y_pred)

print (f1_score(y_true, y_pred))

print (accuracy_score(y_true, y_pred))

print (classification_report(y_true, y_pred))
