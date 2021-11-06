#!/usr/bin/env sh

set -e

cd $(dirname "$0")

./edaa.py

for item in ./banners/*.svg; do
  echo "$item"
  inkscape \
    --with-gui \
    --batch-process \
    --actions 'select-all:all;ObjectToPath;FitCanvasToSelectionOrDrawing;FileSave;FileClose;FileQuit' \
    "$item"
  svgo "$item"
done
