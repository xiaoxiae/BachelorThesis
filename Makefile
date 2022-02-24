NAME=thesis
ABSTRACT=abstract
LATEXMKOPTS=-pdf -outdir=build/
LATEXMK=latexmk $(LATEXMKOPTS)

PDFS=$(NAME).pdf $(ABSTRACT)-en.pdf $(ABSTRACT)-cz.pdf

all:
	$(LATEXMK) $(NAME)
	$(LATEXMK) $(ABSTRACT)-cz
	$(LATEXMK) $(ABSTRACT)-en

clean:
	$(LATEXMK) -C
