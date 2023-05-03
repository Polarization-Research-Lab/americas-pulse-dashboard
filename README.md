---
title: Polarization Research Lab - America's Pulse Dashboard
---

# Overview


# Update

```bash
cd .build/
python3 pipeline.py
```

# Run

Just push changes to github (if using pages).

## Run Locally

```bash
bundle exec jekyll server
```

# Organization

This repo is built off a typical [jekyll](https://jekyllrb.com/) static website builder, particularly using the [chirpy theme](https://github.com/cotes2020/jekyll-theme-chirpy).

The relevant things to know about the directory organization are:

- `_site/`: where jekyll actually puts the rendered website; this is what a public user has access to
- `_data/`: contains all the data files used during liquid html formatting
- `_includes/`: contains any core html files used for the website infrastructure
- `_layouts/`: contains the html pages that any markdown files are templated around
  - `home.html` is the landing page; it doesn't have a markdown file in `_tabs/` like the other pages do
- `_tabs/`: where all the key pages are located; these are what you edit if you want to mess with the data display pages (affpol, norms, violence, trustval, download, about)
- `assets/`: where the css, javascript, imgs, etc are located
  - `data/`: a collection of json files that contain summary data used by [chart.js](https://www.chartjs.org/)
  - `js/`: various utilies used throughout the website
    - `js/charts/`: holds the scripts used to generate all of the charts; chart scripts are never stored directly in the html pages where they sit (for security rules compliance)
- `misc/`: where any other pages
- `_posts/`: where blog-style posts can be stored (assuming we ever add those)
- `.build/`: a collection of python and R scripts used to update the various data files in `assets/data/` and `_data/`

## Chirpy Template Modifications

The key files from the original chirpy theme that have been edited are:

- `_includes/head.html`
- `_includes/sidebar.html`
- `_layouts/default.html`
- `_layouts/home.html`
- `_layouts/page.html`
- `assets/css/style.scss` (heavily)

The primary additions are:

- a new set of files in `_layouts/`
  - `datatab.html`: for each data display page
  - `downloads.html`: downloads page (used by `_tabs/download.md`)
  - `blank.html`: for just showing an empty page

# Dependencies

- javascript
  - chartjs
  - chartjs-geo
  - chartjs-sankey
  - chartjs-annotate
  - guage.js
- python3
  - numpy
  - pandas
  - scipy
  - sqlalchemy
- r
  - 





