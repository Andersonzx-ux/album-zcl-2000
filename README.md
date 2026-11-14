# 2000 — Zezé Di Camargo & Luciano

Player estático (HTML/CSS/JS puro) para GitHub Pages. Tudo é dirigido por `data/album.js`.

## Visual
A capa real é o centro da página. O **nome na capa é a barra de progresso**: conforme a faixa toca, as letras ainda não tocadas ficam pálidas e uma linha vermelha marca o ponto atual. Clique ou arraste sobre o nome para buscar na faixa. O recorte do nome é gerado a partir da própria capa (`assets/nome-mask.webp`).
A página ganha luz da capa desfocada. Pausado, a foto fica um pouco mais apagada; tocando, volta à cor plena e "respira" devagar.

## Paleta (medida em assets/cover.jpg; scripts em tools/)
| Papel | Cor | Onde |
|---|---|---|
| ink | #00259B | azul das letras do nome |
| red | #E20106 | vermelho do "di" e do "&" |
| night | #0A1811 | preto-esverdeado (cabelos e sombras) |
| forest | #72872C | verde escuro (folhagem em sombra) |
| lime | #ECEF80 | verde-limão da folhagem |
| sun | #F8E459 | amarelo do suéter |
| mint | #D5F8C3 | verde-água do suéter |
| paper | #F4F9E9 | o tom mais claro da foto |

Dois temas, só com essas cores (botão **Dia/Noite**, lembrado no navegador):
- **Dia:** fundo paper, texto e botões em ink, destaques em red.
- **Noite:** fundo night, botões e títulos em sun, traduções em lime.

A paleta fica em `album.palette` e é aplicada nas variáveis CSS ao abrir a página.

## Recursos
- Letras sincronizadas (LRC), esconder/mostrar letra, tela cheia (Esc sai), botão PT de tradução (campo opcional `translation` por faixa).
- Tela bloqueada / central de mídia (Media Session): capa, faixa anterior/próxima, posição.
- Atalhos: Espaço = tocar/pausar; Shift+← / Shift+→ = faixa anterior/próxima.

## Regenerar o recorte do nome
`python3 -I tools/gerar_recortes.py .` (a partir de `assets/cover.jpg`).

Áudios em `audio/01.flac … 15.flac`. Fonte: Jost (OFL), licença em `assets/fonts/`.
