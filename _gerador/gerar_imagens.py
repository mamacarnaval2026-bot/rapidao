#!/usr/bin/env python3
"""Gera logotipo, favicons e imagens ILUSTRATIVAS (placeholders) em WebP/JPG.
Substitua as imagens de assets/img/ por fotos reais mantendo o MESMO nome de arquivo
e a mesma proporção (16:9 para serviços/blog, 4:3 para o hero)."""
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "img")
os.makedirs(OUT, exist_ok=True)
AZUL = (11, 37, 64); AZUL2 = (19, 58, 94); VERDE = (14, 122, 90); VERDE_C = (127, 224, 184)
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

LOGO_MARK = '''<g>
  <path d="M20 2 4 8v11c0 9.2 6.6 17 16 19 9.4-2 16-9.8 16-19V8L20 2Z" fill="#0e7a5a"/>
  <path d="M20 9c-5 3-8 7.5-8 12.5 0 3 1.6 5.6 4 7 .2-4.2 1.8-8 4.6-11-2 3.3-3 7-2.9 11.2.7.2 1.5.3 2.3.3 4.4 0 8-3.6 8-8C28 16 24.8 11.6 20 9Z" fill="#fff"/>
</g>'''

def svg_logo(cor_texto, cor_sub):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 168 40" width="168" height="40" role="img" aria-label="Elbatec Controle de Pragas">
{LOGO_MARK}
<text x="44" y="22" font-family="system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif" font-size="21" font-weight="800" fill="{cor_texto}" letter-spacing="-.3">Elbatec</text>
<text x="45" y="34.5" font-family="system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif" font-size="8.6" font-weight="600" fill="{cor_sub}" letter-spacing="1.1">CONTROLE DE PRAGAS</text>
</svg>
'''

def write(name, data):
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(data)

write("logo-elbatec.svg", svg_logo("#0b2540", "#0e7a5a"))
write("logo-elbatec-branco.svg", svg_logo("#ffffff", "#7fe0b8"))
write("favicon.svg", f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="9" fill="#0b2540"/><g transform="translate(4 2) scale(.8)">{LOGO_MARK}</g></svg>\n')

def mark(size, bg=True):
    s = size * 4
    im = Image.new("RGBA", (s, s), AZUL + (255,) if bg else (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    k = s / 40.0
    ox, oy = (4 * k, 2.5 * k) if bg else (0, 0)
    sc = 0.8 if bg else 1.0
    def P(x, y): return (ox + x * k * sc, oy + y * k * sc)
    shield = [P(20, 2), P(36, 8), P(36, 19), P(33, 29), P(27, 35), P(20, 38), P(13, 35), P(7, 29), P(4, 19), P(4, 8)]
    d.polygon(shield, fill=VERDE)
    leaf = [P(20, 9), P(25, 12), P(28, 17), P(28, 22), P(26, 26), P(22, 29), P(18, 29.5), P(16, 28.5), P(13, 25), P(12, 21), P(14, 15)]
    d.polygon(leaf, fill=(255, 255, 255))
    d.line([P(16.3, 28.5), P(19, 21), P(22, 17)], fill=VERDE, width=max(2, int(1.4 * k)))
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

# Logo PNG para schema (fundo branco)
lg = Image.new("RGB", (600, 160), (255, 255, 255))
m = mark(128, bg=False); lg.paste(m, (16, 16), m)
d = ImageDraw.Draw(lg)
d.text((168, 22), "Elbatec", font=ImageFont.truetype(FONT, 72), fill=AZUL)
d.text((172, 108), "CONTROLE DE PRAGAS", font=ImageFont.truetype(FONT, 26), fill=VERDE)
lg.save(os.path.join(OUT, "logo-elbatec.png"), optimize=True)

# ---------- Ilustrações placeholder ----------
def grad(w, h, c1, c2):
    im = Image.new("RGB", (w, h), c1)
    px = ImageDraw.Draw(im)
    for x in range(w):
        t = x / (w - 1)
        px.line([(x, 0), (x, h)], fill=tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3)))
    return im

def casa(d, x, y, s, cor):
    d.polygon([(x, y + s * .45), (x + s * .5, y), (x + s, y + s * .45)], fill=cor)
    d.rectangle([x + s * .12, y + s * .42, x + s * .88, y + s], fill=cor)

def predio(d, x, y, w, h, cor, janela):
    d.rectangle([x, y, x + w, y + h], fill=cor)
    for r in range(int(h // 46)):
        for c in range(int(w // 40)):
            d.rectangle([x + 14 + c * 40, y + 16 + r * 46, x + 32 + c * 40, y + 38 + r * 46], fill=janela)

def ilustracao(nome, w, h, c1, c2, motivo, seed=0):
    S = 2
    im = grad(w * S, h * S, c1, c2).convert("RGBA")
    lay = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for i, (cx, cy, r) in enumerate([(.12, .2, .32), (.9, .85, .42), (.7, .1, .18)]):
        d.ellipse([(cx - r) * w * S, (cy - r) * w * S + 0, (cx + r) * w * S, (cy + r) * w * S], fill=(255, 255, 255, 14 + 6 * i))
    im = Image.alpha_composite(im, lay.filter(ImageFilter.GaussianBlur(30)))
    d = ImageDraw.Draw(im)
    base = h * S * .82
    d.rectangle([0, base, w * S, h * S], fill=(255, 255, 255, 30))
    clara = (255, 255, 255, 235); media = (255, 255, 255, 120)
    if motivo == "casa":
        casa(d, w * S * .18, base - h * S * .42, h * S * .42, media)
        casa(d, w * S * .42, base - h * S * .55, h * S * .55, clara)
    elif motivo == "predio":
        predio(d, w * S * .15, base - h * S * .55, w * S * .2, h * S * .55, media, (255, 255, 255, 60))
        predio(d, w * S * .4, base - h * S * .7, w * S * .24, h * S * .7, clara, (11, 37, 64, 90))
    elif motivo == "galpao":
        d.polygon([(w * S * .12, base - h * S * .32), (w * S * .5, base - h * S * .48), (w * S * .88, base - h * S * .32),
                   (w * S * .88, base), (w * S * .12, base)], fill=clara)
        for i in range(5):
            x = w * S * (.18 + i * .14); d.rectangle([x, base - h * S * .2, x + w * S * .09, base], fill=(11, 37, 64, 90))
    elif motivo == "agua":
        d.ellipse([w * S * .3, base - h * S * .62, w * S * .7, base - h * S * .5], fill=clara)
        d.rectangle([w * S * .3, base - h * S * .56, w * S * .7, base - h * S * .12], fill=clara)
        d.ellipse([w * S * .3, base - h * S * .18, w * S * .7, base - h * S * .06], fill=clara)
        d.rectangle([w * S * .34, base - h * S * .45, w * S * .66, base - h * S * .2], fill=(14, 122, 90, 120))
    elif motivo == "doc":
        d.rounded_rectangle([w * S * .36, h * S * .14, w * S * .64, base], radius=24, fill=clara)
        for i in range(6):
            d.rounded_rectangle([w * S * .4, h * S * (.24 + i * .08), w * S * (.6 - (i % 2) * .06), h * S * (.26 + i * .08)], radius=6, fill=(11, 37, 64, 110))
    # escudo com check (marca de proteção)
    sx, sy, ss = w * S * .7, h * S * .22, h * S * .36
    pts = [(sx, sy), (sx + ss * .45, sy + ss * .14), (sx + ss * .45, sy + ss * .5), (sx, sy + ss), (sx - ss * .45, sy + ss * .5), (sx - ss * .45, sy + ss * .14)]
    d.polygon(pts, fill=VERDE + (255,))
    d.line([(sx - ss * .18, sy + ss * .48), (sx - ss * .03, sy + ss * .63), (sx + ss * .22, sy + ss * .34)], fill=(255, 255, 255, 255), width=int(ss * .08), joint="curve")
    out = im.convert("RGB").resize((w, h), Image.LANCZOS)
    out.save(os.path.join(OUT, nome + ".webp"), "WEBP", quality=78, method=6)
    if w >= 1200:  # versão JPG 1200x630 para Open Graph
        og = out.resize((1200, int(1200 * h / w)), Image.LANCZOS)
        top = max(0, (og.height - 630) // 2)
        og.crop((0, top, 1200, top + 630)).save(os.path.join(OUT, nome + ".jpg"), "JPEG", quality=80, optimize=True, progressive=True)

IMGS = [
    ("hero-controle-de-pragas-cajamar", 1200, 900, AZUL2, VERDE, "casa"),
    ("dedetizacao-cajamar", 1200, 675, AZUL, VERDE, "casa"),
    ("desratizacao-cajamar", 1200, 675, (24, 48, 70), (40, 110, 90), "galpao"),
    ("descupinizacao-cajamar", 1200, 675, (60, 45, 30), VERDE, "casa"),
    ("desinsetizacao-cajamar", 1200, 675, AZUL2, (60, 140, 90), "casa"),
    ("controle-de-escorpioes-cajamar", 1200, 675, (70, 55, 20), (14, 100, 80), "casa"),
    ("controle-de-pombos-cajamar", 1200, 675, (40, 60, 90), (90, 130, 160), "predio"),
    ("sanitizacao-de-ambientes-cajamar", 1200, 675, AZUL, (20, 140, 150), "predio"),
    ("limpeza-caixa-dagua-cajamar", 1200, 675, (14, 70, 120), (30, 150, 190), "agua"),
    ("limpeza-de-fossa-desentupimento-cajamar", 1200, 675, (30, 40, 50), VERDE, "casa"),
    ("produtos-saneantes-cajamar", 1200, 675, AZUL2, (14, 122, 120), "doc"),
    ("equipe-elbatec", 1200, 675, AZUL, VERDE, "predio"),
    ("blog-como-identificar-cupins", 1200, 675, (70, 50, 30), (130, 100, 60), "casa"),
    ("blog-escorpioes-como-prevenir", 1200, 675, (80, 60, 20), VERDE, "casa"),
    ("blog-frequencia-dedetizacao", 1200, 675, AZUL, (40, 120, 140), "doc"),
]
for a in IMGS:
    ilustracao(*a)
# OG padrão
og = Image.open(os.path.join(OUT, "hero-controle-de-pragas-cajamar.jpg")).copy()
d = ImageDraw.Draw(og, "RGBA")
d.rounded_rectangle([40, 430, 760, 590], radius=20, fill=(11, 37, 64, 225))
d.text((70, 450), "Elbatec Controle de Pragas", font=ImageFont.truetype(FONT, 40), fill=(255, 255, 255))
d.text((70, 515), "Cajamar e região · (11) 3232-2206", font=ImageFont.truetype(FONT, 30), fill=VERDE_C)
og.save(os.path.join(OUT, "og-elbatec.jpg"), "JPEG", quality=82, optimize=True, progressive=True)
print("imagens geradas em", OUT)
