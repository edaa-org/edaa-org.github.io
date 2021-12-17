# EDA² logos and banners

The font used in the EDA² logos and banners is [Teko](https://fonts.google.com/specimen/Teko), designed by [Indian Type Foundry](http://www.indiantypefoundry.com/).
That is distributed under the [Open Font License](https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL).

The EDA² logo was inspired by [flaticon.com/free-icon/blocks_5375762](https://www.flaticon.com/free-icon/blocks_5375762)
and the colours from [materialpalette.com](https://www.materialpalette.com/colors).
However, the logo is generated from scratch using a Python script (see [edaa.py](edaa.py)).

"Work in progress" sign images are based on [flaticon.com/free-icon/work-in-progress_5578703](https://www.flaticon.com/free-icon/work-in-progress_5578703).

## Development

Python script [edaa.py](edaa.py) uses [mozman/svgwrite](https://github.com/mozman/svgwrite/) for generating the logo and
banners in SVG format with embedded fonts (see [svgwrite.rtfd.io](https://svgwrite.rtfd.io) and [https://github.com/mozman/svgwrite/blob/master/examples/using_fonts.py](mozman/svgwrite: examples/using_fonts.py)).
Per project banners are saved to [banners/raw](banners/raw).

Unfortunately, when using fonts in SVGs, it is not possible to programmatically compute the size that text needs.
Therefore, the canvas sizes of the SVGs generated with Python do not match the content.
[Inkscape](https://inkscape.org/) supports fitting the canvas to a selection or to the drawing.
Moreover, inkscape can be used on the command-line (see [wiki.inkscape.org: Using the Command Line](https://wiki.inkscape.org/wiki/Using_the_Command_Line)).
Script [generate_project_banners.sh](generate_project_banners.sh) calls inkscape in order to fit the canvas size of
project banners.
At the same time, text is converted to paths, so that the font is not required.
The converted files are saved to [banners/path](banners/path).

After converting the text to paths, the styles in the sources of the SVGs are not required anymore.
Script [generate_project_banners.sh](generate_project_banners.sh) calls [svg/svgo](https://github.com/svg/svgo) right
after inkscape, in order to clean/optimise the SVGs.
The optimised files are saved to [../_static/logo](../_static/logo).

As a result, generating project banners requires three tools: Python, Inkscape and NodeJS.
It would be desirable to find an alternative solution using Python only, or JavaScript only.

### Container image edaa/svg

In order to avoid contributors having to set up all the tools locally, a container image is built in this repository and
it is made available through the [ghcr.io/edaa-org](https://github.com/orgs/edaa-org/packages) registry.
The container image includes svgwrite (Python), Inkscape, svgo (NodeJS) and Teko (from [google/fonts: ofl/teko](https://github.com/google/fonts/tree/main/ofl/teko)).
See [../.github/edaa--svg.dockerfile](../.github/edaa--svg.dockerfile) for further details.

### Make targets

The Makefile in the root of this repository includes targets `logo-build` and `logo-run` to, respectively, build the
container image and to generate the logos using the image.
