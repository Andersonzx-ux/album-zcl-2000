"""Gera o recorte real do nome da capa (assets/cover.jpg) como máscara alfa e as capas pequenas.
Uso: python3 -I tools/gerar_recortes.py <pasta-do-projeto>"""
import sys, numpy as np
from PIL import Image
from scipy import ndimage as ndi
P = sys.argv[1]
im = Image.open(f'{P}/assets/cover.jpg').convert('RGB')
a = np.asarray(im).astype(float)
L = 0.2126*a[..., 0] + 0.7152*a[..., 1] + 0.0722*a[..., 2]
x0, y0, x1, y1 = 56, 294, 584, 336            # caixa do nome na capa (640x640)
l = L[y0:y1, x0:x1]
bg = ndi.gaussian_filter(ndi.maximum_filter(l, size=13), 1.2)   # luz local ao redor das letras
alpha = np.clip((bg - l - 22) / np.maximum(bg - 80 - 22, 1), 0, 1)   # só letras escuras ficam opacas
alpha[alpha < 0.12] = 0
out = np.zeros((y1 - y0, x1 - x0, 4), np.uint8)
out[..., :3] = 255
out[..., 3] = (alpha * 255).astype(np.uint8)
Image.fromarray(out, 'RGBA').save(f'{P}/assets/nome-mask.webp', quality=95, method=4)
im.resize((256, 256), Image.LANCZOS).save(f'{P}/assets/cover-256.jpg', quality=90)
im.resize((512, 512), Image.LANCZOS).save(f'{P}/assets/cover-512.jpg', quality=90)
print('caixa', x0, y0, x1, y1, 'cobertura', round(float((alpha > .5).mean()), 3))
