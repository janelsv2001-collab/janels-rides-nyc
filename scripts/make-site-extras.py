#!/usr/bin/env python3
"""Generate the share/install assets for Janel's Rides NYC (deploy package extras)."""
import json
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.expanduser(
    "~/workspace/goals/taxi-driver-website-setup-answers/hidden_files/netlify-deploy-staging/site-extras"
)
os.makedirs(os.path.join(OUT, "icons"), exist_ok=True)

DARK = (18, 18, 18)        # #121212
PANEL = (26, 26, 26)
AMBER = (245, 158, 11)     # #F59E0B
WHITE = (255, 255, 255)
GRAY = (170, 170, 170)

SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def draw_car(d, cx, cy, scale, color):
    """Simple side-view car glyph centered near (cx, cy)."""
    w, h = 340 * scale, 120 * scale
    x0, y0 = cx - w / 2, cy - h / 2
    # body
    d.rounded_rectangle([x0, y0 + 40 * scale, x0 + w, y0 + 95 * scale], radius=28 * scale, fill=color)
    # cabin
    d.rounded_rectangle([x0 + 70 * scale, y0 + 5 * scale, x0 + 250 * scale, y0 + 55 * scale], radius=24 * scale, fill=color)
    # windows (cut out in dark)
    d.rounded_rectangle([x0 + 88 * scale, y0 + 16 * scale, x0 + 155 * scale, y0 + 48 * scale], radius=8 * scale, fill=DARK)
    d.rounded_rectangle([x0 + 168 * scale, y0 + 16 * scale, x0 + 232 * scale, y0 + 48 * scale], radius=8 * scale, fill=DARK)
    # wheels
    for wx in (x0 + 70 * scale, x0 + 270 * scale):
        d.ellipse([wx - 30 * scale, y0 + 78 * scale, wx + 30 * scale, y0 + 138 * scale], fill=DARK)
        d.ellipse([wx - 13 * scale, y0 + 95 * scale, wx + 13 * scale, y0 + 121 * scale], fill=GRAY)


# ---------- OG cover 1200x630 ----------
img = Image.new("RGB", (1200, 630), DARK)
d = ImageDraw.Draw(img)
d.rectangle([0, 0, 1200, 10], fill=AMBER)
draw_car(d, 600, 165, 1.05, AMBER)
d.text((600, 330), "Janel's Rides NYC", font=font(SANS_BOLD, 92), fill=WHITE, anchor="mm")
d.text((600, 420), "Book a ride with Janel", font=font(SANS, 46), fill=AMBER, anchor="mm")
d.text((600, 505), "Quiet all-electric rides  •  Upfront TLC fares  •  Pay with Apple Pay",
       font=font(SANS, 31), fill=GRAY, anchor="mm")
d.text((600, 570), "janels-rides-nyc.netlify.app", font=font(SANS, 26), fill=(120, 120, 120), anchor="mm")
img.save(os.path.join(OUT, "og-cover.png"))

# ---------- App icons ----------
def make_icon(size, path):
    im = Image.new("RGB", (size, size), AMBER)
    dr = ImageDraw.Draw(im)
    dr.text((size / 2, size / 2 - size * 0.02), "J", font=font(SANS_BOLD, int(size * 0.62)), fill=DARK, anchor="mm")
    im.save(path)

make_icon(192, os.path.join(OUT, "icons", "icon-192.png"))
make_icon(512, os.path.join(OUT, "icons", "icon-512.png"))
make_icon(180, os.path.join(OUT, "icons", "apple-touch-icon.png"))

# ---------- Manifest ----------
manifest = {
    "name": "Janel's Rides NYC",
    "short_name": "Janel's Rides",
    "start_url": "/",
    "scope": "/",
    "display": "standalone",
    "background_color": "#121212",
    "theme_color": "#121212",
    "icons": [
        {"src": "/icons/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
        {"src": "/icons/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
    ],
}
with open(os.path.join(OUT, "manifest.webmanifest"), "w") as f:
    json.dump(manifest, f, indent=2)

print("assets written to", OUT)
for root, _, files in os.walk(OUT):
    for name in sorted(files):
        p = os.path.join(root, name)
        print(os.path.relpath(p, OUT), os.path.getsize(p), "bytes")
