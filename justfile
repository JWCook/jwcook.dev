SOURCE_DIR := "pages"
BUILD_DIR := "_build/html"
TAGS_DIR := "pages/tags"

# List available recipes
default:
    just --list

# Run all steps
all:
    just clean lint build linkcheck size publish

# Clean build and tags directories
clean:
    rm -rf {{BUILD_DIR}} {{TAGS_DIR}}

# Build documentation
build:
    sphinx-build {{SOURCE_DIR}} {{BUILD_DIR}}

# Run linters
lint:
    -pre-commit run --all

# Check for broken links
linkcheck:
    sphinx-build -b linkcheck {{SOURCE_DIR}} {{BUILD_DIR}}

# Serve site with live reloading
live:
    just clean
    ( sleep 2; python -m webbrowser http://localhost:8181 ) &  # Open browser after delay
    sphinx-autobuild {{SOURCE_DIR}} {{BUILD_DIR}} -a \
        --watch assets \
        --watch templates \
        --watch pages/conf.py \
        --ignore '*.tmp' \
        --ignore '**/tags/*' \
        --port 8181

# Publish site to tilde.team
publish:
    rsync -rlpt --delete --progress _build/html/*  tilde.team:~/public_html/
    rsync -pt assets/dotfiles/tagline.txt          tilde.team:~/public_html/
    rsync -pt assets/images/avatar.png             tilde.team:~/public_html/
    rsync -pt assets/dotfiles/.project             tilde.team:~/
    ssh tilde.team 'cp ~/public_html/tagline.txt ~/.ring'
    ssh tilde.team 'touch ~/public_html/index.html'

# Get total site size
size:
   /bin/du -h -d 1 _build/html/ | sort -h
