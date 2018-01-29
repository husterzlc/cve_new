import os
import pickle
import codecs
from CVE_json_uncrawed import craw

if __name__=="__main__":
    
    with codecs.open('uncrawed.txt','r','utf-8') as f:
      lines = f.readline()
      print lines
      while lines:
        try:
          craw(lines)
        except Exception:
          with open("uncrawed1.txt",'a') as f1:
                f1.write(lines)
                f1.write("\n")
        lines = f.readline()
        print lines
