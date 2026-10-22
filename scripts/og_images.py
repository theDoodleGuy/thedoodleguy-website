"""Make the social share images (the picture Facebook, LinkedIn etc. show).

Runs automatically after every build (see .github/workflows/deploy.yml).
One 1200x630 PNG per post at _site/og/<post-file-name>.png, plus
_site/og/default.png for the home and blog pages. No need to touch this
when adding posts.
"""

import math
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "scripts" / "fonts"
OUT = ROOT / "_site" / "og"
W, H = 1200, 630

PAPER, INK, GRID = "#FFFEF8", "#17161A", (43, 78, 255, 22)
RED, BLUE = "#FF5C4D", "#2B4EFF"
TAGS = {"Adaptation": "#FFE94A", "Tech Advances": "#D6E0FF", "Past Experience": "#FFDAD6"}


def font(name, size, weight=None):
    f = ImageFont.truetype(str(FONTS / name), size)
    if weight:
        try:
            f.set_variation_by_axes([weight])
        except Exception:
            pass
    return f


def wrap(draw, text, fnt, width):
    lines, line = [], ""
    for word in text.split():
        trial = f"{line} {word}".strip()
        if draw.textlength(trial, font=fnt) <= width:
            line = trial
        else:
            lines.append(line)
            line = word
    lines.append(line)
    return lines


def fit_title(draw, title, width, max_h):
    for size in range(76, 34, -2):
        fnt = font("ArchivoBlack-Regular.ttf", size)
        lines = wrap(draw, title, fnt, width)
        if len(lines) * size * 1.18 <= max_h:
            return fnt, lines, size
    return fnt, lines, size


def squiggle(draw, x, y, length):
    pts = [(x + t, y + 7 * math.sin(t / 26)) for t in range(0, length, 3)]
    draw.line(pts, fill=RED, width=9, joint="curve")


def card(title, pillar, path):
    img = Image.new("RGB", (W, H), PAPER)
    grid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    g = ImageDraw.Draw(grid)
    for x in range(0, W, 32):
        g.line([(x, 0), (x, H)], fill=GRID, width=1)
    for y in range(0, H, 32):
        g.line([(0, y), (W, y)], fill=GRID, width=1)
    img.paste(grid, (0, 0), grid)
    d = ImageDraw.Draw(img)

    # Card with the site's hard offset shadow
    d.rounded_rectangle([58, 54, W - 42, H - 38], 26, fill=BLUE)
    d.rounded_rectangle([44, 40, W - 56, H - 52], 26, fill="#FFFFFF", outline=INK, width=5)

    x, top = 96, 88
    if pillar:
        tf = font("SpaceMono-Regular.ttf", 26)
        tw = d.textlength(pillar, font=tf)
        d.rounded_rectangle([x, top, x + tw + 40, top + 50], 25, fill=TAGS.get(pillar, "#FFE94A"), outline=INK, width=3)
        d.text((x + 20, top + 25), pillar, font=tf, fill=INK, anchor="lm")
        top += 82
    else:
        top += 70

    fnt, lines, size = fit_title(d, title, W - 2 * x - 40, 300)
    y = top
    for line in lines:
        d.text((x, y), line, font=fnt, fill=INK)
        y += int(size * 1.18)
    squiggle(d, x + 4, y + 22, 300)

    d.text((x, H - 102), "theDoodleGuy", font=font("Caveat.ttf", 58, 700), fill=INK, anchor="ls")
    d.text((W - x, H - 108), "thedoodleguy.com", font=font("SpaceMono-Regular.ttf", 26), fill=BLUE, anchor="rs")
    img.save(path, optimize=True)


def front_matter(md):
    m = re.match(r"---\n(.*?)\n---", md.read_text(encoding="utf-8"), re.S)
    data = {}
    for line in (m.group(1) if m else "").splitlines():
        k, _, v = line.partition(":")
        data[k.strip()] = v.strip().strip('"').strip("'")
    return data


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    card("AI learned to draw. So what happens to us?", "", OUT / "default.png")
    count = 1
    for md in sorted((ROOT / "src" / "posts").glob("*.md")):
        fm = front_matter(md)
        if fm.get("title"):
            card(fm["title"], fm.get("pillar", ""), OUT / f"{md.stem}.png")
            count += 1
    print(f"og images: {count} written to {OUT}")


if __name__ == "__main__":
    sys.exit(main())
