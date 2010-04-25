#!/usr/bin/env python
# vim:fileencoding=utf-8
'''
lv_presentation_gen.py - lv presentation generator
'''

from optparse import OptionParser

op = OptionParser()
op.add_option('-s','--separator',dest='sep',help='set page separator',default='----')
op.add_option('-o','--output',dest='output',help='set output directory',default='.')

(opt,args) = op.parse_args()

sep = opt.sep

cnt = 0
for i in open(args[0]).read().split(sep):
  o = open('%s/%03d.txt' % (opt.output,cnt),'w').write(i)
  cnt += 1
