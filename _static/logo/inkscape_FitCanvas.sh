#!/usr/bin/env sh

set -e

cd $(dirname "$0")

# TODO: Since we convert texts to paths through 'ObjectToPath' it should be possible to remove the embedded font.

for item in ./banners/*.svg; do
  echo "$item"
  inkscape \
    --with-gui \
    --batch-process \
    --actions 'select-all:all;ObjectToPath;FitCanvasToSelectionOrDrawing;FileSave;FileClose;FileQuit' \
    "$item"
done
