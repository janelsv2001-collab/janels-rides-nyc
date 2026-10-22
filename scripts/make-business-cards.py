#!/usr/bin/env python3
"""Mini business cards for Janel's Rides NYC — 3.5x2in + 0.125in bleed at 300dpi = 1125x675."""
import os
from PIL import Image, ImageDraw, ImageFont

HOME = os.path.expanduser("~")
QR_PATH = os.path.join(HOME, "workspace/your_files/janel-s-rides-nyc/janels-rides-nyc-qr.png")
OUT_DIR = os.path.join(HOME, "workspace/your_files/janel-s-rides-nyc")

W, H = 1125, 675
DARK = (18, 18, 18)
AMBER = (245, 158, 11)
WHITE = (255, 255, 255)
GRAY = (175, 175, 175)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def f(p, s):
    return ImageFont.truetype(p, s)


# ---------------- FRONT ----------------
img = Image.new("RGB", (W, H), DARK)
d = ImageDraw.Draw(img)
d.rectangle([0, 0, W, 30], fill=AMBER)
CX = W // 2
d.text((CX, 78), "JANEL'S RIDES NYC", font=f(BOLD, 66), fill=AMBER, anchor="ma")
d.text((CX, 168), "Janel Santos  ★ 5.0", font=f(BOLD, 46), fill=WHITE, anchor="ma")
d.text((CX, 232), "2023 Hyundai Kona Electric — quiet, clean, all-electric", font=f(REG, 35), fill=GRAY, anchor="ma")
d.text((CX, 322), "Private rides  •  Airport trips  •  Upfront fares  •  Apple Pay", font=f(REG, 33), fill=(225, 225, 225), anchor="ma")
d.text((CX, 386), "Servicio en inglés y español", font=f(BOLD, 34), fill=AMBER, anchor="ma")
d.text((CX, 486), "janels-rides-nyc.netlify.app", font=f(BOLD, 52), fill=WHITE, anchor="ma")
d.text((CX, 566), "Mon–Fri 4 AM – 7 PM  •  Airport rides any day by appointment", font=f(REG, 31), fill=GRAY, anchor="ma")
front = os.path.join(OUT_DIR, "business-card-front.png")
img.save(front)

# ---------------- BACK ----------------
img = Image.new("RGB", (W, H), DARK)
d = ImageDraw.Draw(img)
d.rectangle([0, 0, W, 30], fill=AMBER)
d.text((CX, 62), "SCAN TO BOOK YOUR NEXT RIDE", font=f(BOLD, 54), fill=AMBER, anchor="ma")
card = 400
x0, y0 = CX - card // 2, 150
d.rounded_rectangle([x0, y0, x0 + card, y0 + card], radius=28, fill=WHITE)
qr = Image.open(QR_PATH).convert("RGB").resize((340, 340), Image.NEAREST)
img.paste(qr, (CX - 170, y0 + 30))
d.text((CX, 578), "janels-rides-nyc.netlify.app", font=f(BOLD, 38), fill=WHITE, anchor="ma")
back = os.path.join(OUT_DIR, "business-card-back.png")
img.save(back)

# ---------------- PRINT PDF (front page, back page) ----------------
pdf = os.path.join(OUT_DIR, "business-cards.pdf")
front_img = Image.open(front)
back_img = Image.open(back)
front_img.save(pdf, save_all=True, append_images=[back_img], resolution=300.0)

print("saved", front, os.path.getsize(front))
print("saved", back, os.path.getsize(back))
print("saved", pdf, os.path.getsize(pdf))
