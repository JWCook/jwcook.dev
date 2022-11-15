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
	rsync -a _build/html/* tilde:~/public_html/
	rsync -a .ring tilde:~/
	ssh tilde 'touch ~/public_html/index.html'
