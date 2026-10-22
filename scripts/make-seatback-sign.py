#!/usr/bin/env python3
"""Seatback sign for Janel's Rides NYC — 8.5x11in portrait at 300dpi."""
import os
from PIL import Image, ImageDraw, ImageFont

HOME = os.path.expanduser("~")
QR_PATH = os.path.join(HOME, "workspace/your_files/janel-s-rides-nyc/janels-rides-nyc-qr.png")
OUT_DIR = os.path.join(HOME, "workspace/your_files/janel-s-rides-nyc")
PNG_OUT = os.path.join(OUT_DIR, "seatback-sign.png")
PDF_OUT = os.path.join(OUT_DIR, "seatback-sign.pdf")

W, H = 2550, 3300
DARK = (18, 18, 18)
PANEL = (32, 32, 32)
AMBER = (245, 158, 11)
WHITE = (255, 255, 255)
GRAY = (175, 175, 175)
BORDER = (60, 60, 60)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def f(path, size):
    return ImageFont.truetype(path, size)


def centered(d, cx, y, text, font, fill):
    d.text((cx, y), text, font=font, fill=fill, anchor="ma")
    return y + font.size


def wrap(d, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if d.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


img = Image.new("RGB", (W, H), DARK)
d = ImageDraw.Draw(img)
CX = W // 2

# --- top amber band ---
d.rectangle([0, 0, W, 235], fill=AMBER)
d.text((CX, 52), "JANEL'S RIDES  NYC", font=f(BOLD, 118), fill=DARK, anchor="ma")

y = 300
# --- headline ---
d.text((CX, y), "ENJOYED THIS RIDE?", font=f(BOLD, 140), fill=WHITE, anchor="ma")
y += 185
d.text((CX, y), "BOOK ME DIRECT", font=f(BOLD, 205), fill=AMBER, anchor="ma")
y += 275

# --- sub copy ---
sub = ("Skip the surge. Pre-book your next trip with the driver you already "
       "trust — upfront fare, no surprises.")
for line in wrap(d, sub, f(REG, 86), W - 360):
    d.text((CX, y), line, font=f(REG, 86), fill=(225, 225, 225), anchor="ma")
    y += 110
y += 30

# --- benefit chips ---
chips = ["Upfront fares", "Airport trips", "Apple Pay", "English • Español"]
chip_font = f(BOLD, 64)
gap = 30
widths = [d.textlength(c, font=chip_font) + 76 for c in chips]
total = sum(widths) + gap * (len(chips) - 1)
x = (W - total) / 2
for c, wch in zip(chips, widths):
    d.rounded_rectangle([x, y, x + wch, y + 118], radius=59, outline=AMBER, width=5, fill=PANEL)
    d.text((x + wch / 2, y + 22), c, font=chip_font, fill=WHITE, anchor="ma")
    x += wch + gap
y += 118 + 64

# --- scan CTA + QR card ---
d.text((CX, y), "SCAN TO BOOK", font=f(BOLD, 118), fill=AMBER, anchor="ma")
y += 165
card = 1120
x0, y0 = CX - card // 2, y
d.rounded_rectangle([x0, y0, x0 + card, y0 + card], radius=56, fill=WHITE)
qr = Image.open(QR_PATH).convert("RGB")
qr = qr.resize((980, 980), Image.NEAREST)
img.paste(qr, (CX - 490, y0 + 70))
y += card + 40
d.text((CX, y), "Point your camera — no app needed", font=f(REG, 82), fill=GRAY, anchor="ma")
y += 120

# --- URL + driver + hours ---
d.text((CX, y), "janels-rides-nyc.netlify.app", font=f(BOLD, 90), fill=WHITE, anchor="ma")
y += 125
d.text((CX, y), "Janel Santos  ★ 5.0  •  2023 Hyundai Kona Electric", font=f(REG, 76), fill=(225, 225, 225), anchor="ma")
y += 105
d.text((CX, y), "Mon–Fri  4 AM – 7 PM  •  Airport rides any day by appointment", font=f(REG, 70), fill=GRAY, anchor="ma")
y += 115

# --- Spanish line + footer ---
d.text((CX, y), "¿Te gustó el viaje? La próxima vez, reserva directo conmigo.", font=f(BOLD, 64), fill=AMBER, anchor="ma")
y += 105
d.text((CX, y), "Pre-arranged rides only — please book ahead through the site.", font=f(REG, 62), fill=(130, 130, 130), anchor="ma")

img.save(PNG_OUT)
img.save(PDF_OUT, resolution=300.0)
print("saved", PNG_OUT, os.path.getsize(PNG_OUT), "bytes")
print("saved", PDF_OUT, os.path.getsize(PDF_OUT), "bytes")
print("content ends at y =", y + 80, "of", H)
