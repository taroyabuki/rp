SRC=$(wildcard *.py)

PDF=$(SRC:.py=.pdf)

all: $(PDF)

.SUFFIXES: .pdf .py

.py.pdf:
	python3 $<
	if [ -f /usr/bin/pdfcrop ]; then\
		pdfcrop $@;\
		rm $@;\
		mv $(basename $@)-crop.pdf $@;\
	fi

clean:
	rm -f *.pdf
