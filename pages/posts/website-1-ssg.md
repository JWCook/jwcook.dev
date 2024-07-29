---
date: 2024-09-01
---
# Website Setup Part 1: Core Tools
::::{grid} 1 1 3 3
:::{grid-item}
```{tags} status:draft, web, code
```
:::
:::{grid-item}
Posted **2024-09-01**
:::
:::{grid-item}
:::
::::

For my first few posts here, it seems appropriate to write about how this site is set up.
I put a brief description {ref}`here <about-this-site>`, but I think it would be worth going into
more detail and sharing some things I learned along the way.

## Purpose and audience
This will the first in a series of posts about tools I am using to build this site, and
some tangents exploring how they work in more detail and how they can be applied elsewhere.

I will focus less on _how to do it_ and more on _how it works_.
There are already plenty of great tutorials out there, so I'm not going to write another one of those.
Instead, this series will explain some site-building tools and concepts from the bottom up.

For newer webmasters just starting out, I wouldn't necessarily recommend this specific setup for
your own site, but the concepts involved are widely applicable.

For those already familiar with these tools, some of this info may be review, but you'll likely
find blabalbalbalballbllb
% TODO: finish this seciton


## Summary
For starters, like most personal websites this is a static site made of HTML, CSS, and a bit of JS.
The rest of this post will assume familiarity with
[static site generators](https://en.wikipedia.org/wiki/Static_site_generator) (SSGs),
but the basic idea is:

:::{card}
:text-align: center
plaintext documents (in some markup language)<br/>
{fas}`plus`<br/>
templates (in some template engine)<br/>
{fas}`plus`<br/>
SSG<br/>
{fas}`equals`<br/>
![](../../assets/images/twinkles.gif) ![](../../assets/images/website.gif) ![](../../assets/images/twinkles.gif)
:::

That website can then be hosted anywhere. It's just files on [someone else's computer](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/), not a web application, so there's no need to set up a specialized server.

For this site, the core tools used are **Sphinx** and **MyST**, built on top of the lower-level tools **docutils** and **Jinja**. I'll talk a little bit about each one of them below.

## Sphinx intro
It all starts with [Sphinx](https://www.sphinx-doc.org), which is a static site generator mainly intended for technical documentation. If you've ever read docs for an application or library on [Read the Docs](https://readthedocs.io), you've probably seen sites made with Sphinx. Its original use case was documenting the python language, starting with version [2.6](https://docs.python.org/2.6/) in 2008. Needless to say, it has progressed a lot since then!

Sphinx is also considered a **documentation generator**, meaning it has features for dynamically generating and modifying content. For example, you can point it at some code with comments, and it will use that info to create some nice API documentation (example: `requests` [source code](https://github.com/psf/requests/blob/0e322af87745eff34caffe4df68456ebc20d9068/src/requests/api.py#L14-L53) and [generated docs](https://requests.readthedocs.io/en/latest/api/#requests.request)).

Before getting into more detail, though, I'll breifly introduce two lower-level tools that Sphinx is built on.

## Docutils
[docutils](https://docutils.sourceforge.io) is a document processing engine that takes plaintext markup and converts it into all kinds of useful formats.
* For input, it is mainly built around [reStructuredText](https://docutils.sourceforge.io/rst.html) (rST), but can be
  extended to work with other markup languages.
* For output, we're mainly interested in the HTML output right now, but also supports things like LaTeX and manpages.

% TODO: example of docutils CLI

Importantly, it introduces the concept of **directives**, which are blocks of markup that take arguments as input (sometimes including more markup) and can dynamically generate output.

At its most basic, it can add some extra styling to the output, for example a highlighted warning. In rST, it would look like this:
```rst
.. warning::
   This function is deprecated!
```

Which produces output like this:
```{warning}
This function is deprecated!
```

They can do a lot more than just styling. For example, there are directives to handle structured data like `csv-table`:
```rst
.. csv-table:: Fruits
    :file: data/fruit.csv
    :header-rows: 1
```

That takes an input CSV file [like this](../../assets/data/fruit.csv), and produces output like this:
:::{dropdown} Table output
```{csv-table} Fruits
:file: ../../assets/data/fruit.csv
:header-rows: 1
```
:::

Directives also happen to be one of the main ways docutils can be extended. In other words, you can write **python code that takes markup as input**, and does whatever processing you want. In a future post I'd like to cover how to make custom directives, but that's enough about them for now.

## Sphinx + docutils
% TODO
Sphinx uses docutils under the hood for its core document processing, but as a user you won't typically interact with
docutils directly (except when developing your own extensions).


...


## Jinja
[Jinja](https://jinja.palletsprojects.com) is a **template engine**, in the same category of tool as [Nunjucks](https://mozilla.github.io/nunjucks/) (inspired by jinja), [Pug](https://github.com/pugjs/pug), and [mustache](https://github.com/janl/mustache.js). You're likely already familiar, but **templates** let you insert basic programming logic (variables, conditionals, loops, reusable blocks, etc.) into otherwise static plaintext files.

It can be used to template any kind of text document, but here it is mostly used to template HTML. This is the second main ingredient that enables Sphinx to dynamically generate content. Here is a simple example of a Jinja HTML template:
:::{dropdown} `template.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>{{ content }}</p>
    <ul>
        {% for i in items %}
            <li>{{ i }}</li>
        {% endfor %}
    </ul>
</html>
```
:::

You can then generate a page from this template in python:
:::{dropdown} `render_template.py`
```python
from jinja2 import Template

template = Template(open('template.html').read())
rendered = template.render(
    title='My Page',
    content='Check out this list of items:',
    items=[f'Item {i}' for i in range(5)],
)
with open('output.html', 'w') as f:
    f.write(rendered)
```
:::

Which renders output like this:
:::{dropdown} `output.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>My Page</title>
</head>
<body>
    <h1>My Page</h1>
    <p>Check out this list of items:</p>
    <ul>
        <li>Item 0</li>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
        <li>Item 4</li>
    </ul>
</html>
```
:::

![](../../assets/images/jinja-output.png)


## Sphinx + Jinja
Sphinx adds lots of abstraction on top of Jinja, so you don't typically render pages directly.
Input variables come from Sphinx-specific features and config, and template rendering is run by
Sphinx in one of several build steps.

Sphinx also provides base templates for common page elements and layout, which are extended by
third-party **themes.** However, you are free to modify, extend, or completely replace these
templates.

There is a lot you can do with these templates to customize the structure and style of your site,
so I'll save that for a future post.


## MyST
[MyST](https://myst-parser.readthedocs.io)
