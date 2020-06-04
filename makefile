FILE ?=

static_analysis:
	mypy $(FILE)

test:
	pytest
