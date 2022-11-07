.PHONY: clean docs livedocs

clean:
	rm -rf _build

docs:
	sphinx-build pages _build/html

livedocs:
	sphinx-autobuild pages _build/html -a \
		--watch assets \
		--watch pages/conf.py \
		--ignore '*.tmp' \
		--port 8181
