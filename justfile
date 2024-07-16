SOURCE_DIR := "pages"
BUILD_DIR := "_build"
TAGS_DIR := "pages/tags"
LIVE_PORT := "8181"

# List available recipes
default:
    just --list

# Run all steps
all:
    just clean lint build linkcheck size publish-site publish-tilde

# Clean build and tags directories
clean:
    rm -rf {{BUILD_DIR}} {{TAGS_DIR}}

# Build documentation
build:
    sphinx-build -v --doctree-dir {{BUILD_DIR}}/doctrees {{SOURCE_DIR}} {{BUILD_DIR}}/html

# Run linters
lint:
    -pre-commit run --all

# Check for broken links
linkcheck:
    -sphinx-build -b linkcheck {{SOURCE_DIR}} {{BUILD_DIR}}/html

# Serve site with live reloading
live:
    just clean
    sphinx-autobuild {{SOURCE_DIR}} {{BUILD_DIR}}/html -a \
        --doctree-dir {{BUILD_DIR}}/doctrees \
        --watch assets \
        --watch templates \
        --watch pages/conf.py \
        --ignore '*.tmp' \
        --ignore '**/tags/*' \
        --port {{LIVE_PORT}} \
        --open-browser \
        --delay 1 \
        -v

# Publish all files
publish:
    just publish-site publish-tilde

# Publish site to tilde.team
publish-site:
    rsync -r \
        --perms --times \
        --copy-links \
        --delete \
        --progress \
        _build/html/* \
        tilde.team:~/public_html/

# Publish tilde-specific files
publish-tilde:
    rsync \
        --perms --times \
        assets/dotfiles/tagline.txt \
        assets/images/avatar.png \
        tilde.team:~/public_html/
    rsync \
        --perms --times \
        assets/dotfiles/.project \
        tilde.team:~/
    ssh tilde.team 'cp ~/public_html/tagline.txt ~/.ring'
    ssh tilde.team 'touch ~/public_html/index.html'


# Get total site size
size:
   /bin/du -h -d 1 _build/html/ | sort -h
