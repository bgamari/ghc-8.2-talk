talk.pdf : talk.mkd allocs.pdf
	pandoc --to=beamer --slide-level=2 --bibliography=refs.bib $< -o $@

allocs.pdf : plot.py allocs
	python plot.py
