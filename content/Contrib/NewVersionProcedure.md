---
title: New Version Procedure
site_area: Contributing
layout: default
permalink: /Contrib/NewVersionProcedure/
---

1. Update the changelog with *any* changes and push
2. Create the new docs **(push at the very end):**
    1. Copy the folder containing the current docs, rename it to the release version that you just made
    2. Change all of the permalinks in the front matter to reflect the new location on the site
    3. Do a find and replace (`CTRL + F`) for any instances of the name of the previous release that should be updated (including links)
    4. Change the documentation directory page to include the newest docs you just created
    5. Push
3. Finish writing the docs
4. Create a release on GitHub with the commit created in step 1
5. Change the `latest_release` variable in `_config.yml` on the branch `gh-pages` to the **exact** name of the newest release and push
