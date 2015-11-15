#!/usr/bin/env python
# -*- coding: utf-8 -*-

import markdown
import codecs
import sys
import os


md = markdown.Markdown(None, extensions=['mdx_latex'])

if len(sys.argv) != 2:
    print '''Usage: make-lesson.py INPUT'''
    sys.exit(-1)

fname = sys.argv[1]

if not os.path.exists(fname):
    print "Invalid lesson: \"%s\"" % (sys.argv[1])
    sys.exit(-1)

f = codecs.open(fname, encoding='utf-8')
text = f.read()

latex_out = md.convert(text)[8:-10]

print '''\documentclass[12pt,a4paper]{article}
\input{style}
\input{func}
\\renewcommand\\thesection{}
\\renewcommand\\thesubsection{}
\\renewcommand\\thesubsubsection{}
\\lohead{\\hfill Экспериментальная студия аудио-видео технологий}

\\begin{document}
\\vspace*{0.5cm}
'''

print latex_out.encode('utf-8').strip()

print '''
\\end{document}

'''
