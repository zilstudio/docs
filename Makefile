TEX = pdflatex
MD2LATEX = ./make-lesson.py

DEPS = func.tex style.tex
MD_SRC = $(wildcard lesson*.md)
TEX_SRC = $(MD_SRC:.md=.tex)
PDFS = $(MD_SRC:.md=.pdf)

all: $(PDFS)

%.tex: %.md
	$(MD2LATEX) $< > $@

%.pdf: %.tex $(DEPS)
	$(TEX) $<
	rm *.aux *.log

upload: all
	scp $(PDFS) webmaster@poltavski.ru:/home/webmaster/www/poltavski.ru/zil/docs 

.PHONY: clean

clean:
	rm -rf *.log *.aux $(PDFS) $(TEX_SRC)
