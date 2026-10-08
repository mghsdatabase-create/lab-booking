# Draws the Lab Booking app icons (run during publishing).
import os
from PIL import Image, ImageDraw
TEAL = (31, 111, 107); WHITE = (255, 255, 255); AMBER = (242, 177, 52); SOFT = (206, 231, 228); RING = (20, 70, 67)

def glyph(d, cx, cy, w):
    h = w * 0.86; x0 = cx - w / 2; y0 = cy - h / 2 + w * 0.04; x1 = cx + w / 2; y1 = y0 + h; r = w * 0.12
    d.rounded_rectangle([x0, y0, x1, y1], radius=r, fill=WHITE)
    d.rounded_rectangle([x0, y0, x1, y0 + h * 0.26], radius=r, fill=SOFT)
    d.rectangle([x0, y0 + h * 0.14, x1, y0 + h * 0.26], fill=SOFT)
    rw = w * 0.07; rh = w * 0.2
    for fx in (0.3, 0.7):
        rx = x0 + w * fx
        d.rounded_rectangle([rx - rw / 2, y0 - rh * 0.45, rx + rw / 2, y0 + rh * 0.55], radius=rw / 2, fill=RING)
    gx0 = x0 + w * 0.12; gy0 = y0 + h * 0.36; cw = (w * 0.76) / 3; ch = (h * 0.54) / 2; pad = w * 0.035
    for row in range(2):
        for col in range(3):
            bx = gx0 + col * cw + pad; by = gy0 + row * ch + pad
            d.rounded_rectangle([bx, by, bx + cw - 2 * pad, by + ch - 2 * pad], radius=w * 0.03,
                                fill=AMBER if (row, col) == (1, 1) else SOFT)

def make(size, maskable, path):
    S = size * 4
    im = Image.new('RGBA', (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    if maskable:
        d.rectangle([0, 0, S, S], fill=TEAL); gw = S * 0.46
    else:
        d.rounded_rectangle([0, 0, S - 1, S - 1], radius=S * 0.22, fill=TEAL); gw = S * 0.58
    glyph(d, S / 2, S / 2, gw)
    im.resize((size, size), Image.LANCZOS).save(path, optimize=True)

out = os.environ.get('OUT', '_site/icons'); os.makedirs(out, exist_ok=True)
make(192, False, out + '/icon-192.png'); make(512, False, out + '/icon-512.png')
make(192, True, out + '/maskable-192.png'); make(512, True, out + '/maskable-512.png')
