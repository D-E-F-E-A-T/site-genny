#!/usr/bin/env python3

import os
os.system("rsync -rv --exclude=README.md _site/* ../../noahbroyles.github.io/.")