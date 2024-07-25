SOURCE_DIR := "pages"
BUILD_DIR := "build"
TAGS_DIR := "pages/tags"
LIVE_PORT := "8181"

# List available recipes
default:
    just --list

# Run all steps
all:
    just clean lint build linkcheck size
    just publish-tilde
    just publish

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
    sphinx-autobuild {{SOURCE_DIR}} {{BUILD_DIR}}/html \
        --doctree-dir {{BUILD_DIR}}/doctrees \
        --watch assets \
        --watch templates \
        --watch src/conf.py \
        --ignore '*.tmp' \
        --ignore '**/tags/*' \
        --port {{LIVE_PORT}} \
        -v

# Publish site to Cloudflare Pages (and login first, if needed)
publish:
    just clean
    PUBLISH_ENV='prod' just build
    wrangler whoami | grep -q 'not authenticated' && wrangler login || echo "✅ Logged in"
    wrangler pages deploy {{BUILD_DIR}}/html/

# Publish site to tilde.team
publish-tilde:
    just clean
    PUBLISH_ENV='dev' just build
    rsync -r \
        --perms --times \
        --copy-links \
        --delete \
        --progress \
        {{BUILD_DIR}}/html/* \
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
   /bin/du -h -d 1 {{BUILD_DIR}}/html/ | sort -h
