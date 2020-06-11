FILE ?=
STUBDIR = ./stubs
BOREALIS = ../borealis

static_analysis:
	mypy $(FILE)

test:
	pytest

stubs:
	stubgen $(BOREALIS) -o $(STUBDIR)
	rsync -a $(STUBDIR)/borealis/ $(STUBDIR)
	rm -r $(STUBDIR)/borealis $(STUBDIR)/stubs $(STUBDIR)/stubs.*
