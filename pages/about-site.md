(about-this-site)=
# {fas}`code` About this site
```{tags} code, docs
```
A summary of how this site is built.
![](../assets/images/about-site.png)
<br/><br/>

```{admonition} TL;DR
:class: note
My goal is to take some of my favorite technical writing tools and adapt them for
building a personal site.
Source code can be found [On GitHub](https://github.com/JWCook/jwcook.dev).
```

This is a markdown-based static site generated with
[Sphinx](https://www.sphinx-doc.org),
[MyST](https://myst-parser.readthedocs.io),
[Jinja templates](https://jinja.palletsprojects.com), and other tools in the
[Executable Books](https://executablebooks.org) ecosystem. The theme is modified from
[Furo](https://pradyunsg.me/furo) with a palette based on
[gruvbox](https://github.com/morhetz/gruvbox).
Other site features are added via Sphinx extensions, some of which I've made or contributed to
specifically for this site.

Why use this over other [popular static site generators](https://jamstack.org/generators)?
Sphinx and company are not the most convenient tools for the purpose of building a personal site,
but they're currently the most interesting to me. They are mainly geared toward
technical documentation, and are packed with powerful features usually applied in
[software development](https://github.com/readthedocs-examples/awesome-read-the-docs?tab=readme-ov-file#sphinx-projects) and
[scientific domains](https://executablebooks.org/en/latest/gallery/).

But why should they get all the cool toys? I believe there is a lot of potential to apply these
features to personal sites, blogs, and other creative projects.

If you have questions about how this site is built, or are interested in using Sphinx + MyST to build
your own site, you are welcome to [drop me a line](mailto:jwcook@jwcook.dev).
