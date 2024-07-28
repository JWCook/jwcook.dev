---
date: 2024-08-01
---
# Website Setup Part 0: Intro
% TODO: make a custom directive for article header
::::{grid} 1 1 3 3
:::{grid-item}
```{tags} status:draft, web, ramble
```
:::
:::{grid-item}
Posted **2024-08-01**
:::
:::{grid-item}
:::
::::

## *Furious typing noises*
```sh
sudo systemctl start blog
```
_Hmm, that wasn't it, let's try_
```sh
sudo update-rc.d blogd defaults
```
_Maybe I'm missing some headers?_
```sh
./configure && make blog.so
```
_What a mess. What if I just_
```sh
python -c "import blog; blog.run()"
```
_Okay, not that either. How about_
```sh
docker run -it blog:latest
```
_Of course not, that's not going to scale. Let's do_
```sh
kubectl run blog --attach
```

...

...

...!!! OH HI THERE.

`surprised-cat.jpg`

I didn't notice you. Been standing there awhile? Oh, that? It's noth-<br />
`Ctrl-Alt-F2` `sudo shutdown -h now`<br />
-ing important. Just, you know, trying to start a blog. Yes, of course I know what I'm doing.

What do you mean, _just start writing?_ How quaint! What charming naïveté! This is **20xx**, my friend, and you can't
just hurl some text files onto a web server like a _barbarian_ and then expe-

_Overengineered_, you say‽ \*snort\* Well maybe where you come from, but-

...**Web 1.0** is cool again, you say? You really can just throw a static site together without the insani- \*ahem\* _sophistication_ of modern web development? Okay, I'll bite. Pull up a chair, and I'll put on some tea. Let's hear some more about this.


## Let's make a website!
`construction.gif`

For some time I've been interested in making a personal website. And as part of that, I've been wanting to start a blog, essentially as a higher-effort form of the notetaking I already do on a regular basis. I want to practice writing, spend a bit more time organizing my thoughts, and share some things that might be useful or interesting to others.

The thing is, I enjoy writing, but I _really_ enjoy tinkering, sometimes a little too much. Setting up the site just the way I want it has turned into somewhat of a time sink, although not for the reasons I originally expected.

Once I realized this doesn't have to be a fancy production-grade web application, I've found that building a small static website for myself is quite an enjoyable side project for its own sake. I've been able to spend time on fun features instead of infrastructure and scalability and all that. Of course, this also provided a convenient excuse to procrastinate on my original goal of writing.

A few months later, and... hmm, is that right? Just a sec.
```sh
git log --reverse --format="format:%aI" --all | head -n 1
```
Wait, ***what***? A year and a half? Well then. A year and a half of occasional tinkering later, and I _think_ I _kind of maybe_ have enough of a site set up to get back to the writing part. At this cadence, my next post can be expected Q1 2026.

## Blog QC

It's hard to know what level of blog post effort and quality to aim for. For the sake of just getting something on paper(`.md`), here are a few sanity checks:
* My primary audience is myself!
* If I eventually reach an audience in the single, _maybe_ low double digits, that would be kinda neato.
* ...but I'm deciding right now that I can't let that be my main motivator. I loathe the idea of self-promotion, SEO, and crafting a personal brand.
* If, say, I write a terrible cringey low-effort post and a bunch of people see it, that's not actually the end of the world.
* If I pour _oodles_ of thought and effort into an amazing article that I can be truly proud of, and not a single person besides myself sees it, it will probably still be worthwhile.
* Nobody's forcing me to abide by International Blogging Law. I can get away with posting unfinished scribblings and then editing them incrementally, or not at all.

## Up next

Next, I plan to write about how this site is built and some things I've learned along the way. But if you'll excuse me, I think I see some bits over there that need tinkering. I'll be _right_ back, I'm sure.
