.PHONY: clean docs livedocs

clean:
	rm -rf docs/_build

docs:
	sphinx-build docs docs/_build/html

livedocs:
	sphinx-autobuild docs docs/_build/html -a \
		--ignore '*.tmp' \
		--port 8181
