#!/usr/bin/env sh

set -e

cd $(dirname "$0")

mkdir -p banners/raw
mkdir -p banners/path

./edaa.py

for item in ./banners/raw/*.svg; do
  echo "$item"
  inkscape \
    --with-gui \
    --batch-process \
    --actions 'select-all:all;ObjectToPath;FitCanvasToSelectionOrDrawing;export-filename:'./banners/path/$(basename "$item")'; export-do;EditUndo;EditUndo;FileClose;FileQuit' \
    "$item"
  svgo ./banners/path/$(basename "$item") -o ../_static/logo/$(basename "$item")
done
