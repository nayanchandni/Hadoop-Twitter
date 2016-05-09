#!/usr/bin/env python

import sys
import string

"""for line in sys.stdin:
  words = line.strip().lower().translate(None,string.punctuation).split()
  for word in words:
      print '%s\t%s' % (word, 1)
      print 'WordCount\t1'"""

import json

for line in sys.stdin:
        a=json.loads(line)
        if (a['user']['screen_name']):
            print '%s\t%s' % (a['user']['screen_name'], len(a['text']))


