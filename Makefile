.PHONY: all clean docs linkcheck livedocs publish size
SOURCE_DIR = pages
BUILD_DIR  = _build/html

all: clean docs linkcheck size publish

clean:
	rm -rf $(BUILD_DIR)

docs:
	sphinx-build $(SOURCE_DIR) $(BUILD_DIR)

linkcheck:
	sphinx-build -b linkcheck $(SOURCE_DIR) $(BUILD_DIR)

livedocs: clean
	sphinx-autobuild $(SOURCE_DIR) $(BUILD_DIR) -a \
		--watch assets \
		--watch templates \
		--watch pages/conf.py \
		--ignore '*.tmp' \
		--port 8181

publish:
	rsync -rlpt --delete --progress _build/html/*  tilde.team:~/public_html/
	rsync -pt assets/dotfiles/tagline.txt          tilde.team:~/public_html/
	rsync -pt assets/images/avatar.png             tilde.team:~/public_html/
	rsync -pt assets/dotfiles/.project             tilde.team:~/
	ssh tilde.team 'cp ~/public_html/tagline.txt ~/.ring'
	ssh tilde.team 'touch ~/public_html/index.html'

size:
	/bin/du -h -d 1 _build/html/ | sort -h
