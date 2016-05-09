#!/usr/bin/env python

import sys
import string

word_count = 0
old_word = None
data = []
temp=[]
sumx=0

for line in sys.stdin:
  (key,val) = line.strip().split('\t',1)
  if old_word != key:
    if old_word:
      #print '%s\t%s' % ( old_word,word_count)
      if old_word == 'PrezOno':
          avg=sumx/word_count
      data.append((old_word,sumx/word_count))
      #temp=[]
      sumx =0
      word_count = 0
  old_word = key
  try:
    word_count = word_count + 1
    #temp.append(int(val))
    sumx += int(val)
  except:
    continue
if old_word == 'PrezOno':
          avg=sumx/word_count
data.append((old_word,sumx/word_count))
#print '%s\t%s' % (old_word,word_count)

print("average for PrezOno is %s" %avg)

for i in data:
    print('%s\t%s' % (i[0],i[1]-avg))

