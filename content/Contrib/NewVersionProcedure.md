---
title: New Version Procedure
site_area: Contributing
layout: default
permalink: /Contrib/NewVersionProcedure/
---

1. Update the changelog with *any* changes and push
2. Update the docs with *any* changes and push
3. Create a release on GitHub
4. Do the following changes to the site:
  1. Change the `latest_release` variable in `_config.yml` on the branch `gh-pages` to the **exact** name of the newest release
  2. Copy the current docs version, rename it to the next version that you're going to make (so you can start working on it), and change all of the permalinks in the front matter
  3. Do a find and replace (`CTRL + F` in most editors) for any instances of the name of the previous release that should be updated (including in links)
  4. Change the documentation directory page to include the newest (dev) docs you just created
  5. Push
