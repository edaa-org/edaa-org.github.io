#!/usr/bin/env python3

from pathlib import Path
import svgwrite


ROOT = Path(__file__).resolve().parent

backgrounds = [
    "#ffffff", # white
    "#fcfcfc", # BTD body
    "#333333", # BTD sidebar
    "#383e46",
    "#0d1117", # GitHub dark
    "#000000", # black
]

projects = [
    ("py", "OSVDE", 0),
    ("py", "HWS", 0),
    ("pyEDAA.", "ProjectModel", 1),
    ("py", "CAPI", 1),
    ("py", "VHDLModel", 2),
    ("py", "SVModel", 2),
    ("pyEDAA.", "UCIS", 2),
    ("pyEDAA.", "Reports", 2),
    ("pyEDAA.", "VUnit", 3),
    ("py", "FPGA", 3),
    ("pyEDAA.", "SymbiFlow", 3),
    ("pyEDAA.", "Edalize", 3),
    ("pyTooling.", "CLIAbstraction", 4),
    ("pyEDAA.", "CLITool", 4),
    ("pyEDAA.", "OutputFilter", 4),
    ("pyEDAA.", "Containers", 5),
    ("pyEDAA.", "LocalInstallations", 5),
]

# https://www.materialpalette.com/colors
materialpalette = {
    # Red, Pink, Purple, Light Blue, Light Green, Amber, Deep Orange, Blue Grey
    "light_on_light": ["#ef5350", "#ec407a", "#ba68c8", "#29b6f6", "#9ccc65", "#ffca28", "#ff7043", "#78909c"],
    "dark_on_light": ["#c62828", "#ad1457", "#8e24aa", "#0277bd", "#558b2f", "#ff8f00", "#d84315", "#37474f"],
    "light_on_dark": ["#ef5350", "#ec407a", "#ba68c8", "#29b6f6", "#9ccc65", "#ffca28", "#ff7043", "#b0bec5"],
    "dark_on_dark": ["#c62828", "#ad1457", "#8e24aa", "#0277bd", "#558b2f", "#ff8f00", "#d84315", "#78909c"],
}

red_gray = [0, 2, 3, 4, 5, 7]
sedaa = ["dark_on_light", "light_on_light"]
sedaa_on_dark = ["dark_on_dark", "light_on_dark"]

#---

def _draw(dwg, colors, shades, offset=(0, 0), unit=50):
    """
    Draw the default multi-coloured EDAA logo without strokes.
    """
    for x in range(6):
        for params in [
            [
                2 * unit,
                materialpalette[shades[0]][colors[x]]
            ],
            [
                4 * unit * (x % 2),
                materialpalette[shades[1]][colors[x]]
            ]
        ]:
            dwg.add(
                dwg.rect(
                    insert=(offset[0] + params[0], offset[1] + x * unit),
                    size=(2 * unit, unit),
                    fill=params[1],
                )
            )

def generate_edaa_svg():
    """
    Generate and save the default logo to file 'edaa.svg'
    """
    dwg = svgwrite.Drawing(str(ROOT / '../_static/logo/edaa.svg'), (300, 300), debug=True)
    _draw(dwg, red_gray, sedaa)
    dwg.save(pretty=True)

#---

def _draw_highlighted(dwg, row, color, shades, offset=(0, 0), unit=50):
    """
    Draw the per-project one-highlighted-layer EDAA logo, with strokes matching the dark colour of the tuple.
    """
    for x in range(6):
        for params in [
            [
                2 * unit,
                materialpalette[shades[0]][color] if x == row else None
            ],
            [
                4 * unit * (x % 2),
                materialpalette[shades[1]][color] if x == row else None
            ]
        ]:
            dwg.add(
                dwg.rect(
                    insert=(offset[0] + params[0], offset[1] + x * unit),
                    size=(2 * unit, unit),
                    fill="#ffffff" if params[1] is None else params[1],
                    fill_opacity=0.0 if params[1] is None else 1.0,
                    stroke=materialpalette[shades[0]][color] if x != row else "",
                    stroke_width="4px"
                )
            )

def _draw_per_color(dwg, offset=(0,0)):
    """
    Draw all the per-project EDAA logos, both all-coloured and one-highlighted-layer variants, on all background test colours.
    """
    # Single color, two shades
    for idx, col in enumerate(red_gray):
        _draw(
            dwg,
            colors=[col] * 6,
            shades=sedaa,
            offset=(offset[0] + 200*idx, offset[1]),
            unit=20
        )

    # Highlight color, two shades
    for idx, col in enumerate(red_gray):
        _draw_highlighted(
            dwg,
            row=idx,
            color=col,
            shades=sedaa,
            offset=(offset[0] + 200*idx, offset[1] + 150),
            unit=20
        )

#---

def generate_backgrounds_svg():
    """
    Generate and save the backgrounds and per-project logo demo to 'backgrounds.svg'.
    """
    dwg = svgwrite.Drawing(str(ROOT / 'backgrounds.svg'), (1170, 1920), debug=True)
    for idx, background in enumerate(backgrounds):
        baseoffset=(0, idx*320)
        dwg.add(
            dwg.rect(
                insert=baseoffset,
                size=(1170, 320),
                fill=background
            )
        )
        _draw_per_color(dwg, offset=(baseoffset[0]+25, baseoffset[1]+25))
    dwg.save(pretty=True)

#---

def _draw_project_banner(dwg, project, color, shades, offset=(0, 0), unit=50):
    """
    Draw a project banner (logo and text).
    """
    def web_font_embedded(dwg, text, color, offset):
        dwg.embed_google_web_font(name="Teko", uri='http://fonts.googleapis.com/css?family=Teko')
        #@import url(http://fonts.googleapis.com/css?family=Teko);
        dwg.embed_stylesheet("""
        .TekoFont {
            font-family: "Teko";
            font-size: 260pt;
        }
        """)
        # This should work stand alone and embedded in a website!
        dwg.add(dwg.g(class_="TekoFont", )).add(dwg.text(text, insert=offset, fill=color))

    #_draw(dwg, [red_gray[project[2]]]*6, shades, offset)
    _draw_highlighted(
        dwg,
        row=project[2],
        color=color[project[2]],
        shades=shades,
        offset=offset,
        unit=50
    )

    toffset=(360, 235)
    web_font_embedded(
        dwg,
        text=project[0],
        color=materialpalette[shades[0]][color[project[2]]],
        offset=(offset[0] + toffset[0], offset[1] + toffset[1])
    )
    plen=len(project[0])
    web_font_embedded(
        dwg,
        text=project[1],
        color=materialpalette[shades[1]][color[project[2]]],
        offset=(offset[0] + toffset[0] + plen*(124 if plen==2 else 117), offset[1] + toffset[1])
    )

#---

def generate_projects_svg():
    """
    Generate and save the background and per-project banner demo to 'projects.svg'.
    """
    dwg = svgwrite.Drawing(str(ROOT / 'projects.svg'), (14000, 5700), debug=True)

    shades = sedaa
    color = red_gray

    for idx, background in enumerate(backgrounds):

        isDarkBackground = idx > 1

        baseoffset=(idx*2300, 0)
        dwg.add(
            dwg.rect(
                insert=baseoffset,
                size=(2300, 6000),
                fill=background
            )
        )

        for pid, project in enumerate(projects):
            _draw_project_banner(
                dwg,
                project=project,
                color=color,
                shades=sedaa_on_dark if isDarkBackground else shades,
                offset=(baseoffset[0]+50, 50+ pid*350)
            )

    dwg.save(pretty=True)

#---

for project in projects:

    def _draw_banner(fname, project, isDarkBackground):
        """
        Generate and save per-project banners to independent files.

        The size of the canvas matches the size of the logo only.
        Hence, these files need to be post-processed.
        """
        print(project, isDarkBackground)
        dwg = svgwrite.Drawing(str(ROOT / fname), (304, 304), debug=True)
        _draw_project_banner(
            dwg,
            project=project,
            color=red_gray,
            shades=sedaa_on_dark if isDarkBackground else sedaa,
            offset=(2, 2)
        )
        dwg.save(pretty=True)

    if project[2] in [1, 5]:
        for isDarkBackground in [False, True]:
            fname = f"banners/raw/{project[0]}{project[1]}_{'dark' if isDarkBackground else 'light'}.svg"
            _draw_banner(fname, project, isDarkBackground)
    else:
        _draw_banner(f"banners/raw/{project[0]}{project[1]}.svg", project, False)

#---

generate_edaa_svg()
generate_backgrounds_svg()
generate_projects_svg()
