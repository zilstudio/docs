#!/bin/sh

seq 1 100 | while read n
do
	fname="lesson${n}.md"
	if [ -f ${fname} ]
	then
		tex_name="lesson${n}.tex"
		pdf_name="lesson${n}.pdf"
		echo "generating ${tex_name}..."
		./make-lesson.py $n > "$tex_name"

		echo "generating ${pdf_name}..."
		pdflatex "${tex_name}"
	fi
done

exit


rm *.aux *.log
