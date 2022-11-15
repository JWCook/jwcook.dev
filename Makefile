.PHONY: clean docs livedocs

clean:
	rm -rf _build

docs:
	sphinx-build pages _build/html

livedocs: clean
	sphinx-autobuild pages _build/html -a \
		--watch assets \
		--watch pages/conf.py \
		--ignore '*.tmp' \
		--port 8181

publish:
	rsync -a _build/html/*                  tilde.team:~/public_html/
	rsync -a assets/dotfiles/tagline.txt    tilde.team:~/public_html/
	rsync -a assets/images/avatar.png       tilde.team:~/public_html/
	rsync -a assets/dotfiles/.project       tilde.team:~/
	ssh tilde.team 'cp ~/public_html/tagline.txt ~/.ring'
	ssh tilde.team 'touch ~/public_html/index.html'
