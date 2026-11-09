#!/usr/bin/env python3
"""Gera logotipo, favicons e imagens ILUSTRATIVAS (placeholders) em WebP/JPG.
Substitua as imagens de assets/img/ por fotos reais mantendo o MESMO nome de arquivo
e a mesma proporção (16:9 para serviços/blog, 4:3 para o hero)."""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "img")
os.makedirs(OUT, exist_ok=True)
AZUL = (31, 15, 51); AZUL2 = (59, 26, 99); VERDE = (194, 24, 91); VERDE_C = (255, 211, 107); ROXO = (123, 31, 162)
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

LOGO_MARK = '''<g>
  <circle cx="20" cy="20" r="18" fill="#7b1fa2"/>
  <path d="M6 16c4-1.6 9-1.4 14 1.2 5-2.6 10-2.8 14-1.2-.5 7-3.8 10.5-8 10.5-2.6 0-4.4-1.8-6-4-1.6 2.2-3.4 4-6 4-4.2 0-7.5-3.5-8-10.5Z" fill="#fff"/>
  <ellipse cx="13" cy="20" rx="2.6" ry="1.8" fill="#7b1fa2"/><ellipse cx="27" cy="20" rx="2.6" ry="1.8" fill="#7b1fa2"/>
  <path d="M27 14c1-4 4-7 8-8-1 3-3 5-5.5 6.5" fill="#ffd36b"/><circle cx="9" cy="9" r="1.6" fill="#ffd36b"/><circle cx="31" cy="31" r="1.3" fill="#ffd36b"/>
</g>'''

def svg_logo(cor_texto, cor_sub):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 168 40" width="168" height="40" role="img" aria-label="Tango Fantasias">
{LOGO_MARK}
<text x="44" y="22" font-family="system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif" font-size="21" font-weight="800" fill="{cor_texto}" letter-spacing="-.3">Tango</text>
<text x="45" y="34.5" font-family="system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif" font-size="8.6" font-weight="600" fill="{cor_sub}" letter-spacing="3.2">FANTASIAS</text>
</svg>
'''

def write(name, data):
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(data)

write("logo-tango-fantasias.svg", svg_logo("#1f0f33", "#c2185b"))
write("logo-tango-fantasias-branco.svg", svg_logo("#ffffff", "#ffd36b"))
write("favicon.svg", f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="9" fill="#1f0f33"/><g transform="translate(4 2) scale(.8)">{LOGO_MARK}</g></svg>\n')

def mark(size, bg=True):
    s = size * 4
    im = Image.new("RGBA", (s, s), AZUL + (255,) if bg else (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    k = s / 40.0
    ox, oy = (4 * k, 4 * k) if bg else (0, 0)
    sc = 0.8 if bg else 1.0
    def P(x, y): return (ox + x * k * sc, oy + y * k * sc)
    d.ellipse([P(2, 2), P(38, 38)], fill=ROXO)
    pts = [P(6, 16), P(10, 15.2), P(15, 15.6), P(20, 17.2), P(25, 15.6), P(30, 15.2), P(34, 16), P(33, 21), P(30, 25.5), P(26, 26.5),
           P(23, 25), P(20, 22.5), P(17, 25), P(14, 26.5), P(10, 25.5), P(7, 21)]
    d.polygon(pts, fill=(255, 255, 255))
    d.ellipse([P(10.4, 18.2), P(15.6, 21.8)], fill=ROXO); d.ellipse([P(24.4, 18.2), P(29.6, 21.8)], fill=ROXO)
    d.polygon([P(27, 14), P(30, 9), P(35, 6), P(33, 10), P(29.5, 12.5)], fill=VERDE_C)
    d.ellipse([P(7.4, 7.4), P(10.6, 10.6)], fill=VERDE_C)
    if bg:
        m = Image.new("L", (s, s), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, s, s], radius=int(9 * k), fill=255)
        im.putalpha(m)
    return im.resize((size, size), Image.LANCZOS)

for n, sz in (("icon-192.png", 192), ("icon-512.png", 512), ("apple-touch-icon.png", 180)):
    img = mark(sz)
    if n == "apple-touch-icon.png":
        bgi = Image.new("RGB", (sz, sz), AZUL); bgi.paste(img, (0, 0), img); img = bgi
    img.save(os.path.join(OUT, n), optimize=True)
mark(64).save(os.path.join(os.path.dirname(OUT), "..", "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])

lg = Image.new("RGB", (600, 160), (255, 255, 255))
m = mark(128, bg=False); lg.paste(m, (16, 16), m)
d = ImageDraw.Draw(lg)
d.text((168, 22), "Tango", font=ImageFont.truetype(FONT, 72), fill=AZUL)
d.text((172, 108), "FANTASIAS", font=ImageFont.truetype(FONT, 26), fill=VERDE)
lg.save(os.path.join(OUT, "logo-tango-fantasias.png"), optimize=True)

import random
def grad(w, h, c1, c2):
    im = Image.new("RGB", (w, h), c1); px = ImageDraw.Draw(im)
    for x in range(w):
        t = x / (w - 1)
        px.line([(x, 0), (x, h)], fill=tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3)))
    return im

CORES = [(255, 211, 107), (255, 255, 255), (240, 98, 146), (129, 212, 250), (174, 213, 129), (206, 147, 216)]

def vestido(d, cx, top, h, cor):
    w = h * .55
    d.line([(cx, top - h * .1), (cx, top)], fill=(255, 255, 255, 220), width=max(3, int(h * .015)))
    d.line([(cx - w * .45, top + h * .04), (cx, top - h * .02), (cx + w * .45, top + h * .04)], fill=(255, 255, 255, 220), width=max(3, int(h * .015)))
    d.polygon([(cx - w * .18, top + h * .04), (cx + w * .18, top + h * .04), (cx + w * .16, top + h * .38), (cx - w * .16, top + h * .38)], fill=cor)
    d.polygon([(cx - w * .16, top + h * .36), (cx + w * .16, top + h * .36), (cx + w * .5, top + h * .9), (cx - w * .5, top + h * .9)], fill=cor)

def mascara(d, cx, cy, w, cor, olho):
    h = w * .32
    pts = [(cx - w / 2, cy - h * .3), (cx - w * .3, cy - h * .5), (cx, cy - h * .2), (cx + w * .3, cy - h * .5), (cx + w / 2, cy - h * .3),
           (cx + w * .42, cy + h * .4), (cx + w * .2, cy + h * .55), (cx, cy + h * .2), (cx - w * .2, cy + h * .55), (cx - w * .42, cy + h * .4)]
    d.polygon(pts, fill=cor)
    d.ellipse([cx - w * .32, cy - h * .15, cx - w * .1, cy + h * .2], fill=olho)
    d.ellipse([cx + w * .1, cy - h * .15, cx + w * .32, cy + h * .2], fill=olho)
    d.polygon([(cx + w * .3, cy - h * .45), (cx + w * .45, cy - h * 1.6), (cx + w * .55, cy - h * 1.5), (cx + w * .4, cy - h * .35)], fill=(255, 211, 107, 255))

def abobora(d, cx, cy, r):
    for dx in (-.45, .45, 0):
        d.ellipse([cx + dx * r - r * .6, cy - r * .75, cx + dx * r + r * .6, cy + r * .75], fill=(245, 124, 0, 255))
    d.rectangle([cx - r * .07, cy - r, cx + r * .07, cy - r * .7], fill=(85, 139, 47, 255))
    d.polygon([(cx - r * .45, cy - r * .2), (cx - r * .2, cy - r * .2), (cx - r * .32, cy - r * .45)], fill=(31, 15, 51, 255))
    d.polygon([(cx + r * .45, cy - r * .2), (cx + r * .2, cy - r * .2), (cx + r * .32, cy - r * .45)], fill=(31, 15, 51, 255))
    d.chord([cx - r * .45, cy - r * .2, cx + r * .45, cy + r * .45], 0, 180, fill=(31, 15, 51, 255))

def bandeirinhas(d, w, y, n):
    d.line([(0, y), (w, y + 20)], fill=(255, 255, 255, 200), width=4)
    for i in range(n):
        x = w * (i + .5) / n; yy = y + 20 * (x / w)
        d.polygon([(x - w / n * .35, yy), (x + w / n * .35, yy), (x + w / n * .35, yy + w / n * .7), (x, yy + w / n * .5), (x - w / n * .35, yy + w / n * .7)], fill=CORES[i % len(CORES)] + (255,))

def ilustracao(nome, w, h, c1, c2, motivo, seed=0):
    random.seed(nome)
    S = 2; W, H = w * S, h * S
    im = grad(W, H, c1, c2).convert("RGBA")
    lay = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for cx, cy, r in [(.12, .2, .32), (.9, .85, .42), (.7, .1, .18)]:
        d.ellipse([(cx - r) * W, (cy - r) * W, (cx + r) * W, (cy + r) * W], fill=(255, 255, 255, 18))
    im = Image.alpha_composite(im, lay.filter(ImageFilter.GaussianBlur(30)))
    d = ImageDraw.Draw(im)
    for _ in range(70):  # confete
        x, y, r = random.random() * W, random.random() * H, random.uniform(4, 11) * S
        c = random.choice(CORES) + (random.randint(120, 220),)
        if random.random() < .5: d.ellipse([x - r, y - r, x + r, y + r], fill=c)
        else: d.rectangle([x - r, y - r / 2, x + r, y + r / 2], fill=c)
    if motivo in ("arara", "infantil", "junina"):
        d.line([(W * .12, H * .2), (W * .88, H * .2)], fill=(255, 255, 255, 230), width=10 * S)
        n = 4 if motivo != "infantil" else 5
        for i in range(n):
            cx = W * (.2 + i * (.6 / (n - 1)))
            vestido(d, cx, H * .3, H * (.62 if motivo != "infantil" else .5), CORES[(i + len(nome)) % len(CORES)] + (255,))
        if motivo == "junina": bandeirinhas(d, W, H * .04, 10)
    elif motivo == "mascara":
        mascara(d, W * .5, H * .52, W * .55, (255, 255, 255, 240), c1 + (255,))
    elif motivo == "halloween":
        abobora(d, W * .38, H * .62, H * .26)
        d.polygon([(W * .62, H * .7), (W * .78, H * .7), (W * .7, H * .22)], fill=(20, 10, 30, 255))
        d.ellipse([W * .56, H * .66, W * .84, H * .76], fill=(20, 10, 30, 255))
    elif motivo == "acessorios":
        d.polygon([(W * .2, H * .62), (W * .22, H * .36), (W * .28, H * .5), (W * .33, H * .3), (W * .38, H * .5), (W * .44, H * .36), (W * .46, H * .62)], fill=(255, 211, 107, 255))
        mascara(d, W * .7, H * .5, W * .32, (255, 255, 255, 240), c1 + (255,))
    elif motivo == "costura":
        for i, c in enumerate(CORES[:5]):
            d.rounded_rectangle([W * (.12 + i * .08), H * .55, W * (.12 + i * .08) + W * .07, H * .9], radius=10 * S, fill=c + (255,))
        d.rounded_rectangle([W * .58, H * .4, W * .88, H * .62], radius=16 * S, fill=(255, 255, 255, 235))
        d.rectangle([W * .6, H * .62, W * .86, H * .66], fill=(255, 255, 255, 235))
        d.rounded_rectangle([W * .6, H * .3, W * .66, H * .42], radius=6 * S, fill=(255, 255, 255, 235))
        d.line([(W * .63, H * .42), (W * .63, H * .55)], fill=c1 + (255,), width=4 * S)
    elif motivo == "doc":
        d.rounded_rectangle([W * .36, H * .14, W * .64, H * .86], radius=24, fill=(255, 255, 255, 235))
        for i in range(6):
            d.rounded_rectangle([W * .4, H * (.24 + i * .09), W * (.6 - (i % 2) * .06), H * (.26 + i * .09)], radius=6, fill=c1 + (140,))
    out = im.convert("RGB").resize((w, h), Image.LANCZOS)
    out.save(os.path.join(OUT, nome + ".webp"), "WEBP", quality=78, method=6)
    og = out.resize((1200, int(1200 * h / w)), Image.LANCZOS)
    top = max(0, (og.height - 630) // 2)
    og.crop((0, top, 1200, top + 630)).save(os.path.join(OUT, nome + ".jpg"), "JPEG", quality=80, optimize=True, progressive=True)

R1, R2, MAG = (59, 26, 99), (123, 31, 162), (194, 24, 91)
IMGS = [
    ("hero-fabrica-de-fantasias-bras", 1200, 900, R1, MAG, "arara"),
    ("fantasias-infantis-atacado", 1200, 675, (40, 90, 160), R2, "infantil"),
    ("fantasias-adultas-atacado", 1200, 675, (31, 15, 51), MAG, "arara"),
    ("fantasias-de-carnaval-atacado", 1200, 675, R2, (230, 120, 30), "mascara"),
    ("fantasias-de-halloween-atacado", 1200, 675, (25, 12, 40), (90, 30, 110), "halloween"),
    ("roupas-festa-junina-atacado", 1200, 675, (150, 60, 20), (200, 120, 30), "junina"),
    ("figurinos-escolas-apresentacoes", 1200, 675, (20, 100, 120), R2, "infantil"),
    ("acessorios-para-fantasias", 1200, 675, MAG, R1, "acessorios"),
    ("fabrica-de-fantasias-producao", 1200, 675, R1, (20, 100, 120), "costura"),
    ("equipe-tango-fantasias", 1200, 675, R2, MAG, "costura"),
    ("blog-tamanho-fantasia-infantil", 1200, 675, (40, 90, 160), (20, 130, 120), "doc"),
    ("blog-estoque-carnaval", 1200, 675, MAG, (230, 120, 30), "arara"),
    ("blog-conservar-fantasias", 1200, 675, R1, (90, 130, 200), "arara"),
]
for a in IMGS:
    ilustracao(*a)
og = Image.open(os.path.join(OUT, "hero-fabrica-de-fantasias-bras.jpg")).copy()
d = ImageDraw.Draw(og, "RGBA")
d.rounded_rectangle([40, 430, 780, 590], radius=20, fill=(31, 15, 51, 230))
d.text((70, 450), "Tango Fantasias", font=ImageFont.truetype(FONT, 44), fill=(255, 255, 255))
d.text((70, 515), "Fábrica no Brás · (11) 99238-2902", font=ImageFont.truetype(FONT, 30), fill=VERDE_C)
og.save(os.path.join(OUT, "og-tango-fantasias.jpg"), "JPEG", quality=82, optimize=True, progressive=True)
print("imagens geradas em", OUT)
