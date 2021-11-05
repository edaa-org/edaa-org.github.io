#!/usr/bin/env sh

set -e

cd $(dirname "$0")

# TODO: It should be possible to do actions 'select-all:all;ObjectToPath;' and remove the embedded font.

for item in ./banners/*.svg; do
  echo "$item"
  inkscape \
    --with-gui \
    --batch-process \
    --actions 'FitCanvasToSelectionOrDrawing;FileSave;FileClose;FileQuit' \
    "$item"
done
