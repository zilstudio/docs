#!/bin/sh

for i in lesson*.tex
do
	pdflatex $i
done

rm *.aux *.log
