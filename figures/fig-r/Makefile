SRC=$(wildcard *.R)

PDF=$(SRC:.R=.pdf)

all: $(PDF)

.SUFFIXES: .pdf .R

.R.pdf:
	Rscript $<
	if [ -f /usr/bin/pdfcrop ]; then\
		pdfcrop $@;\
		rm $@;\
		mv $(basename $@)-crop.pdf $@;\
	fi

clean:
	rm -f *.pdf
