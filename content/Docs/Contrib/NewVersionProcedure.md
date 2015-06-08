---
title: New Version Procedure
site_area: Docs
layout: default
permalink: /Docs/Contrib/NewVersionProcedure/
---

1. The `CHANGELOG.txt` needs the following changes:
  1. Add a header to show which changes are linked to this release.
2. Create a release on GitHub.
3. Change the `latest_release` variable in `_config.yml` on the branch `gh-pages` to the **exact** name of the newest release.
