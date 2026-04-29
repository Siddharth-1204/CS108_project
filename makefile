LATEX = pdflatex
FILE = report

report.pdf: $(FILE).tex
	$(LATEX) $(FILE).tex
	$(LATEX) $(FILE).tex
	$(LATEX) $(FILE).tex
	$(LATEX) $(FILE).tex
    
.PHONY : clean
clean:
	rm -f *.aux *.log *.out *.toc