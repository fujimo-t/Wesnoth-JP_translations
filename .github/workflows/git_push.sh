#!/bin/bash

git config --global user.name "fujimo-t"
git config --global user.email "10286050+fujimo-t@users.noreply.github.com"
git add **/ja.po
if git diff --exit-code --quiet; then
    echo "No changes to commit."
else
    echo "test"
    git commit -a -m "Pulled from Transifex"
    git push origin main
fi