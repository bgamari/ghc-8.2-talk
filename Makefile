talk.pdf : talk.mkd
	pandoc --to=beamer $< -o $@
