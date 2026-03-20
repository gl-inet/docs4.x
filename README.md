# GL.iNet Documentation

This repository contains the source files for GL.iNet router firmware 4.x documentation.

It is now a multilingual documentation repository. The current language sites in this repo are:

- English: `docs/en/`
- German: `docs/de/`
- Spanish: `docs/es/`
- Japanese: `docs/jp/`

Each language has its own `mkdocs.yml`, `docs/`, and `overrides/` directory.

## Environment

The documentation is built with [MkDocs](https://www.mkdocs.org/) 1.5.3 and the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme 9.4.6.

## Installation

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment, then install dependencies:

```bash
pip install -r requirements.txt
```

You can also install Material for MkDocs directly:

```bash
pip install mkdocs-material
```

Reference: [https://squidfunk.github.io/mkdocs-material/getting-started/#with-pip](https://squidfunk.github.io/mkdocs-material/getting-started/#with-pip)

## Repository Structure

The root `docs/` folder contains one MkDocs project per language:

```text
docs/
  en/
    mkdocs.yml
    docs/
    overrides/
  de/
    mkdocs.yml
    docs/
    overrides/
  es/
    mkdocs.yml
    docs/
    overrides/
  jp/
    mkdocs.yml
    docs/
    overrides/
```

In most cases, localized pages should mirror the corresponding English page path under `docs/en/docs/`.

## Local Preview

Run MkDocs against the language you want to preview.

Examples:

```bash
mkdocs serve -f docs/en/mkdocs.yml
mkdocs serve -f docs/de/mkdocs.yml
mkdocs serve -f docs/es/mkdocs.yml
mkdocs serve -f docs/jp/mkdocs.yml
```

If you are reviewing or translating localized content, open the English source page and the matching localized page side by side in VS Code.

## Online View

Published documentation:

- English: [https://docs.gl-inet.com/router/en/4/](https://docs.gl-inet.com/router/en/4/)
- German: [https://docs.gl-inet.com/router/de/4/](https://docs.gl-inet.com/router/de/4/)
- Spanish: [https://docs.gl-inet.com/router/es/4/](https://docs.gl-inet.com/router/es/4/)
- Japanese: [https://docs.gl-inet.com/router/jp/4/](https://docs.gl-inet.com/router/jp/4/)

## Writing Guide

### Markdown Syntax

All pages are written in Markdown. For basic syntax, see [Markdown Guide](https://www.markdownguide.org/basic-syntax/).

### Open a Link in a New Tab

To open a link in a new tab, add `{target="_blank"}` at the end of the link.

### Image File Type

Prefer PNG unless there is a clear reason to use another format.

### Image Lightbox

If an image is large, use PhotoSwipe. See [About PhotoSwipe](#about-photoswipe).

### Image Size

Use `gl-50-desktop`, `gl-60-desktop`, `gl-70-desktop`, `gl-80-desktop`, or `gl-90-desktop` to control image width on desktop.

Example:

`![gl.inet enable vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/enable_vpn_cascading.png){class="gl-50-desktop"}`

### Image Shadow Effect

Use `{class="glboxshadow"}` to add a shadow to an image.

Example:

`![tap block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-block.jpeg){class="glboxshadow"}`

### Image Captions

```html
<figure>
  <img src="https://dummyimage.com/600x400/eee/aaa" width="300" />
  <figcaption>Image caption</figcaption>
</figure>
```

### Internal Links

Use relative paths for internal links.

```md
[easytethering](../../../tutorials/tether)
```

## About PhotoSwipe

This project currently uses PhotoSwipe v4. Version 5 looks better, but it requires loading JavaScript modules and is not integrated here.

Use PhotoSwipe when the image width is larger than 1021 px.

```html
<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure
    itemprop="associatedMedia"
    itemscope
    itemtype="http://schema.org/ImageObject"
  >
    <a
      href="https://static.gl-inet.com/docs/router/en/3/setup/gl-b2200/hardware/hardware_1.jpg"
      itemprop="contentUrl"
      data-size="3167x2480"
    >
      <img
        src="https://static.gl-inet.com/docs/router/en/3/setup/gl-b2200/hardware/hardware_1.jpg"
        itemprop="thumbnail"
        alt="gl-b2200 pcb pinout"
      />
    </a>
  </figure>
</div>
```

Reference:

- [https://photoswipe.com/documentation/getting-started.html](https://photoswipe.com/documentation/getting-started.html)
- [https://codepen.io/dimsemenov/pen/ZYbPJM](https://codepen.io/dimsemenov/pen/ZYbPJM)

## About Versioning

The `mike` plugin is designed for versioned MkDocs deployments, usually with GitHub Pages. This repository does not deploy with GitHub Pages, but it follows a similar output structure.

Reference:

- [Setting up versioning](https://squidfunk.github.io/mkdocs-material/setup/setting-up-versioning/)
- [mkdocs-material-example-versioning](https://github.com/squidfunk/mkdocs-material-example-versioning)
