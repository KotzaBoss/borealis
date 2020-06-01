FILE ?=

static_analysis:
	mypy $(FILE)
