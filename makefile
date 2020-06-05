FILE ?=
STUBDIR = ./stubs
BOREALIS = ../borealis

static_analysis:
	mypy $(FILE)

test:
	pytest

stubs:
	stubgen $(BOREALIS) -o $(STUBDIR)
	mv $(STUBDIR)/borealis/* $(STUBDIR)
	rm -r $(STUBDIR)/borealis
