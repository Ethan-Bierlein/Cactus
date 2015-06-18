---
title: New Version Procedure
site_area: Contributing
layout: default
permalink: /Contrib/NewVersionProcedure/
---

## Major Release (New Docs)

1. Update the changelog with *any* changes and push
2. Create the new docs **(push at the very end),** on the `gh-pages-dev` branch:
    1. Copy the folder containing the current docs, rename it to the release version that you just made
    2. Change all of the permalinks in the front matter to reflect the new location on the site
    3. Do a find and replace (`CTRL + F`) for any instances of the name of the previous release that should be updated (including links)
    4. Change the documentation directory page to include the newest docs you just created
    5. Push
3. Finish writing the docs
4. Create a release on GitHub with the commit created in step 1
5. Update `_config.yml` for the site
  1. Change the `current_release` variable in to the **exact** name of the newest release
  2. Change the `current_release_cycle` variable to the name of the newest release, only changing the last number of the version to a lowercase "x" (e.g. `v.5.8.2` → `v.5.8.x`)
  3. Push
6. Create a pull request from `gh-pages-dev` to `gh-pages`

## Minor Release (No New Docs)

1. Update the changelog with *any* changes and push
2. Create a release on GitHub with the commit created in step 1
3. Change the `current_release` variable in `_config.yml` on the branch `gh-pages-dev` to the **exact** name of the newest release and push
4. Create a pull request from `gh-pages-dev` to `gh-pages`
