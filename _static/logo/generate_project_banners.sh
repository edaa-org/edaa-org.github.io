#!/usr/bin/env sh

set -e

cd $(dirname "$0")

./edaa.py

for item in ./banners/raw/*.svg; do
  echo "$item"
  inkscape \
    --with-gui \
    --batch-process \
    --actions 'select-all:all;ObjectToPath;FitCanvasToSelectionOrDrawing;export-filename:'./banners/path/$(basename "$item")'; export-do;EditUndo;EditUndo;FileClose;FileQuit' \
    "$item"
  svgo ./banners/path/$(basename "$item") -o ./banners/opt/$(basename "$item")
done
