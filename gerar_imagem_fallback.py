from PIL import Image, ImageDraw, ImageFont
import os
from pathlib import Path

# Criar diretório de imagens se não existir
imagens_dir = Path('imagens')
imagens_dir.mkdir(exist_ok=True)

# Configurações da imagem
width, height = 400, 400
background_color = (240, 240, 240)
text_color = (120, 120, 120)
text = "Imagem não disponível"

# Criar imagem
img = Image.new('RGB', (width, height), background_color)
draw = ImageDraw.Draw(img)

# Tentar carregar uma fonte, se não conseguir, usar a fonte padrão
try:
    # Tentar encontrar uma fonte no sistema
    font_size = 24
    font = ImageFont.truetype("arial.ttf", font_size)
except IOError:
    # Se não encontrar, usar a fonte padrão
    font = ImageFont.load_default()

# Calcular posição do texto para centralizar
text_width, text_height = draw.textsize(text, font=font) if hasattr(draw, 'textsize') else (200, 20)
position = ((width - text_width) // 2, (height - text_height) // 2)

# Desenhar texto
draw.text(position, text, font=font, fill=text_color)

# Desenhar um ícone de imagem (representado por um retângulo com uma "montanha")
rect_width, rect_height = 100, 80
rect_left = (width - rect_width) // 2
rect_top = position[1] - rect_height - 20
rect_right = rect_left + rect_width
rect_bottom = rect_top + rect_height

# Desenhar retângulo
draw.rectangle([rect_left, rect_top, rect_right, rect_bottom], outline=text_color, width=2)

# Desenhar "montanha" dentro do retângulo
draw.polygon([
    (rect_left + 20, rect_bottom - 20),  # Esquerda
    (rect_left + 40, rect_top + 30),     # Meio esquerda
    (rect_left + 60, rect_bottom - 40),  # Meio direita
    (rect_right - 20, rect_bottom - 10)  # Direita
], fill=text_color)

# Desenhar "sol" no canto superior direito do retângulo
sun_radius = 10
sun_position = (rect_right - 25, rect_top + 20)
draw.ellipse(
    (sun_position[0] - sun_radius, sun_position[1] - sun_radius,
     sun_position[0] + sun_radius, sun_position[1] + sun_radius),
    fill=text_color
)

# Salvar imagem
output_path = imagens_dir / 'produto-sem-imagem.jpg'
img.save(output_path)

print(f"Imagem de fallback criada em: {output_path}")