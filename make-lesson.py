#!/usr/bin/env python
# -*- coding: utf-8 -*-

import markdown
import codecs
import sys
import os


md = markdown.Markdown(None, extensions=['mdx_latex'])

if len(sys.argv) != 2:
    print '''Usage: make-lesson.py LESSON_NUMBER'''
    sys.exit(-1)

lesson_number = int(sys.argv[1])
fname = 'lesson' + str(lesson_number) + '.md'

if not os.path.exists(fname):
    print "Invalid lesson number: %s" % (sys.argv[1])
    sys.exit(-1)

f = codecs.open(fname, encoding='utf-8')
text = f.read()

latex_out = md.convert(text)[8:-10]

print '''\documentclass[12pt]{article}
\input{style}
\input{func}
\\renewcommand\\thesection{}

\\begin{document}
\\vspace*{2cm}
'''

print latex_out.encode('utf-8').strip()

print '''
\\end{document}

'''
