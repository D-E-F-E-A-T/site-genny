#!/usr/bin/env python3
import os
os.system("bundle exec jekyll build")
os.system("rsync -rv --exclude=README.md _site/* ../../noahbroyles.github.io/.")