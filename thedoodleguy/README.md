# theDoodleGuy.com

Field notes on designers adapting to AI. Built with [Eleventy](https://www.11ty.dev/), hosted free on GitHub Pages, published by writing markdown files — no code required.

## One-time setup (about 15 minutes)

**1. Put the code on GitHub**

- Create a new repository on github.com (e.g. `thedoodleguy`)
- Upload this folder's contents to it (drag and drop works on the GitHub website, or use git)

**2. Turn on GitHub Pages**

- In the repo: Settings → Pages → under "Build and deployment", set **Source** to **GitHub Actions**
- That's it — the included workflow (`.github/workflows/deploy.yml`) builds and publishes the site automatically on every push to `main`

**3. Point your domain at it**

- In Settings → Pages → Custom domain, enter `thedoodleguy.com` (the `src/CNAME` file already matches)
- At your domain registrar, add these DNS records:
  - `A` records for `@` pointing to: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
  - `CNAME` record for `www` pointing to `YOUR-GITHUB-USERNAME.github.io`
- Back in GitHub Pages settings, tick **Enforce HTTPS** once the domain verifies (can take up to an hour)

## Publishing a new blog post (no code)

1. On GitHub, open the `src/posts/` folder
2. Click **Add file → Create new file**
3. Name it with the URL you want: `my-post-title.md` → publishes at `/blog/my-post-title/`
4. Paste this template at the top, then write your post below it in plain markdown:

```markdown
---
title: Your headline as it appears on the page
metaTitle: "Search-friendly title with your target keyword (under 60 chars)"
description: "The snippet Google shows — include the keyword, make it clickable (under 155 chars)."
excerpt: "The teaser shown on the blog cards."
date: 2026-07-06
pillar: Adaptation
readTime: 6 min
---

Your post starts here. Use ## for subheadings, blank lines between paragraphs,
and normal markdown for **bold**, *italics*, [links](https://example.com) and lists.
```

5. Click **Commit changes** — the site rebuilds and publishes itself in ~1 minute

`pillar` must be one of: `Adaptation`, `Tech Advances`, `Past Experience` (it drives the coloured tag and the blog filters).

You can do all of this from your phone via the GitHub website or app.

## Connecting the newsletter form

The signup form is a placeholder. To make it live, edit `src/_includes/newsletter.njk` and replace the `<form>` line:

**Buttondown** (simplest):
```html
<form class="signup" action="https://buttondown.com/api/emails/embed-subscribe/YOUR_USERNAME" method="post">
```

**Kit (ConvertKit)**: create a form in Kit, then use its action URL:
```html
<form class="signup" action="https://app.kit.com/forms/YOUR_FORM_ID/subscriptions" method="post">
```
(Kit also needs the input to have `name="email_address"` instead of `name="email"`.)

**Mailchimp**: create an embedded form in Mailchimp, copy the `action="https://...list-manage.com/subscribe/post?u=...&id=..."` URL into the form, and change the input to `name="EMAIL"`.

## SEO checklist for every post

- `metaTitle`: lead with the phrase people actually search ("will AI replace designers", "AI tools for designers")
- `description`: under 155 characters, includes the keyword, reads like an invitation
- Filename = URL slug: short, hyphenated, keyword included
- Use `##` subheadings that match related searches
- Aim for 1,200+ words on "pillar" posts you want to rank; personal stories can be any length
- Link between your own posts where relevant

The site handles the rest automatically: canonical URLs, Open Graph/social tags, Article structured data, sitemap.xml and robots.txt.

## Working locally (optional)

```bash
npm install
npm start        # dev server at http://localhost:8080
npm run build    # output in _site/
```

## Where things live

```
src/
  posts/            ← your blog posts (one .md file each)
  index.njk         ← homepage
  blog.njk          ← blog index with filters
  _includes/        ← page templates (base, post, newsletter)
  _data/site.json   ← site name, URL, default description
  css/style.css     ← all styling
```
