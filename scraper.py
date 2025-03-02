import requests
import json
import os
import time
import random
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from pathlib import Path

# Configurações
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
}

# Criar diretórios necessários
IMAGES_DIR = Path('imagens/produtos')
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

# Função para fazer download de imagens
def download_image(url, product_id):
    try:
        response = requests.get(url, headers=HEADERS, stream=True)
        if response.status_code == 200:
            # Extrair extensão da imagem
            parsed_url = urlparse(url)
            path = parsed_url.path
            ext = os.path.splitext(path)[1]
            if not ext:
                ext = '.jpg'  # Extensão padrão
            
            # Criar nome do arquivo
            filename = f"{product_id}{ext}"
            filepath = IMAGES_DIR / filename
            
            # Salvar imagem
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            return f"imagens/produtos/{filename}"
        else:
            print(f"Erro ao baixar imagem: {response.status_code}")
            return None
    except Exception as e:
        print(f"Erro ao baixar imagem: {e}")
        return None

# Função para extrair produtos da Kabum
def scrape_kabum(url):
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            print(f"Erro ao acessar a Kabum: {response.status_code}")
            return None
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extrair dados do produto
        product = {}
        
        # ID do produto (extraído da URL)
        product_id = url.split('/')[-1].split('?')[0]
        product['id'] = f"kabum_{product_id}"
        
        # Nome do produto
        title_elem = soup.select_one('h1')
        if title_elem:
            product['nome'] = title_elem.text.strip()
        
        # Preço
        price_elem = soup.select_one('.finalPrice')
        if price_elem:
            price_text = price_elem.text.strip()
            # Remover "R$" e substituir vírgula por ponto
            price_text = price_text.replace('R$', '').replace('.', '').replace(',', '.').strip()
            try:
                product['preco'] = float(price_text)
            except:
                product['preco'] = 0
        
        # Preço original
        original_price_elem = soup.select_one('.oldPrice')
        if original_price_elem:
            price_text = original_price_elem.text.strip()
            price_text = price_text.replace('R$', '').replace('.', '').replace(',', '.').strip()
            try:
                product['preco_original'] = float(price_text)
            except:
                product['preco_original'] = product.get('preco', 0)
        else:
            product['preco_original'] = product.get('preco', 0)
        
        # Descrição
        desc_elem = soup.select_one('.description')
        if desc_elem:
            product['descricao'] = desc_elem.text.strip()
        else:
            # Tentar encontrar a descrição em outra parte da página
            desc_elem = soup.select_one('#description')
            if desc_elem:
                product['descricao'] = desc_elem.text.strip()
            else:
                product['descricao'] = "Descrição não disponível"
        
        # Imagem
        img_elem = soup.select_one('.mainImg img')
        if img_elem and img_elem.get('src'):
            img_url = img_elem.get('src')
            if not img_url.startswith('http'):
                img_url = urljoin(url, img_url)
            
            # Download da imagem
            img_path = download_image(img_url, product['id'])
            if img_path:
                product['imagem'] = img_path
        
        # Especificações
        specs = {}
        specs_elems = soup.select('.specificationTable tr')
        for spec in specs_elems:
            key_elem = spec.select_one('.specificationName')
            value_elem = spec.select_one('.specificationValue')
            if key_elem and value_elem:
                key = key_elem.text.strip()
                value = value_elem.text.strip()
                specs[key] = value
        
        product['especificacoes'] = specs
        
        # Adicionar fonte
        product['fonte'] = 'Kabum'
        product['url'] = url
        
        # Adicionar avaliação aleatória (para fins de demonstração)
        product['avaliacao'] = round(random.uniform(3.5, 5.0), 1)
        
        # Adicionar categoria
        if 'PC Gamer' in product.get('nome', ''):
            product['categoria'] = 'PC Gamer'
        elif 'Notebook' in product.get('nome', ''):
            product['categoria'] = 'Notebooks'
        elif 'Smartphone' in product.get('nome', ''):
            product['categoria'] = 'Smartphones'
        else:
            product['categoria'] = 'Hardware'
        
        return product
    
    except Exception as e:
        print(f"Erro ao extrair produto da Kabum: {e}")
        return None

# Função para extrair produtos da Pichau
def scrape_pichau(url):
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            print(f"Erro ao acessar a Pichau: {response.status_code}")
            return None
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extrair dados do produto
        product = {}
        
        # ID do produto (extraído da URL)
        product_id = url.split('/')[-1].split('?')[0]
        product['id'] = f"pichau_{product_id}"
        
        # Nome do produto
        title_elem = soup.select_one('.product-title')
        if title_elem:
            product['nome'] = title_elem.text.strip()
        
        # Preço
        price_elem = soup.select_one('.price-boleto .price')
        if price_elem:
            price_text = price_elem.text.strip()
            # Remover "R$" e substituir vírgula por ponto
            price_text = price_text.replace('R$', '').replace('.', '').replace(',', '.').strip()
            try:
                product['preco'] = float(price_text)
            except:
                product['preco'] = 0
        
        # Preço original
        original_price_elem = soup.select_one('.price-old')
        if original_price_elem:
            price_text = original_price_elem.text.strip()
            price_text = price_text.replace('R$', '').replace('.', '').replace(',', '.').strip()
            try:
                product['preco_original'] = float(price_text)
            except:
                product['preco_original'] = product.get('preco', 0)
        else:
            product['preco_original'] = product.get('preco', 0)
        
        # Descrição
        desc_elem = soup.select_one('.product-description')
        if desc_elem:
            product['descricao'] = desc_elem.text.strip()
        else:
            product['descricao'] = "Descrição não disponível"
        
        # Imagem
        img_elem = soup.select_one('.product-image-gallery img')
        if img_elem and img_elem.get('src'):
            img_url = img_elem.get('src')
            if not img_url.startswith('http'):
                img_url = urljoin(url, img_url)
            
            # Download da imagem
            img_path = download_image(img_url, product['id'])
            if img_path:
                product['imagem'] = img_path
        
        # Especificações
        specs = {}
        specs_elems = soup.select('.product-attributes .attribute')
        for spec in specs_elems:
            key_elem = spec.select_one('.attribute-name')
            value_elem = spec.select_one('.attribute-value')
            if key_elem and value_elem:
                key = key_elem.text.strip()
                value = value_elem.text.strip()
                specs[key] = value
        
        product['especificacoes'] = specs
        
        # Adicionar fonte
        product['fonte'] = 'Pichau'
        product['url'] = url
        
        # Adicionar avaliação aleatória (para fins de demonstração)
        product['avaliacao'] = round(random.uniform(3.5, 5.0), 1)
        
        # Adicionar categoria
        if 'PC Gamer' in product.get('nome', ''):
            product['categoria'] = 'PC Gamer'
        elif 'Notebook' in product.get('nome', ''):
            product['categoria'] = 'Notebooks'
        elif 'Smartphone' in product.get('nome', ''):
            product['categoria'] = 'Smartphones'
        else:
            product['categoria'] = 'Hardware'
        
        return product
    
    except Exception as e:
        print(f"Erro ao extrair produto da Pichau: {e}")
        return None

# Função para adicionar produtos manualmente (para demonstração)
def add_demo_products():
    products = []
    
    # Produto 1: Notebook
    products.append({
        'id': 'demo_notebook1',
        'nome': 'Notebook Quantum X1 Pro',
        'preco': 4999.00,
        'preco_original': 5499.00,
        'descricao': 'Notebook ultrafino com processador de última geração, 16GB RAM e 512GB SSD. Ideal para trabalho e jogos leves.',
        'imagem': 'imagens/notebook.jpg',
        'especificacoes': {
            'Processador': 'Intel Core i7 11ª Geração',
            'Memória RAM': '16GB DDR4',
            'Armazenamento': '512GB SSD NVMe',
            'Tela': '15.6" Full HD IPS',
            'Placa de Vídeo': 'NVIDIA GeForce GTX 1650 4GB',
            'Sistema Operacional': 'Windows 11'
        },
        'fonte': 'ASIMOV TECH',
        'url': '#',
        'avaliacao': 4.7,
        'categoria': 'Notebooks'
    })
    
    # Produto 2: Smartphone
    products.append({
        'id': 'demo_smartphone1',
        'nome': 'Smartphone Nexus Pro Max',
        'preco': 3499.00,
        'preco_original': 3999.00,
        'descricao': 'Smartphone com câmera de 108MP, tela AMOLED de 6.7" e bateria de 5000mAh. Desempenho excepcional para todas as tarefas.',
        'imagem': 'imagens/smartphone.jpg',
        'especificacoes': {
            'Processador': 'Snapdragon 8 Gen 1',
            'Memória RAM': '12GB',
            'Armazenamento': '256GB',
            'Tela': '6.7" AMOLED 120Hz',
            'Câmera Principal': '108MP + 12MP + 8MP',
            'Bateria': '5000mAh',
            'Sistema Operacional': 'Android 12'
        },
        'fonte': 'ASIMOV TECH',
        'url': '#',
        'avaliacao': 4.9,
        'categoria': 'Smartphones'
    })
    
    # Produto 3: Smart TV
    products.append({
        'id': 'demo_tv1',
        'nome': 'Smart TV Crystal 4K UHD',
        'preco': 2799.00,
        'preco_original': 3299.00,
        'descricao': 'Smart TV 55" com resolução 4K, HDR10+ e sistema operacional inteligente. Imagem cristalina e recursos avançados.',
        'imagem': 'imagens/smarttv.jpg',
        'especificacoes': {
            'Tamanho': '55"',
            'Resolução': '4K UHD (3840 x 2160)',
            'Taxa de Atualização': '60Hz',
            'HDR': 'HDR10+',
            'Sistema Operacional': 'Smart TV OS',
            'Conexões': 'HDMI x3, USB x2, Wi-Fi, Bluetooth'
        },
        'fonte': 'ASIMOV TECH',
        'url': '#',
        'avaliacao': 4.5,
        'categoria': 'Smart TVs'
    })
    
    return products

# Função principal
def main():
    # Lista para armazenar todos os produtos
    all_products = []
    
    # URLs para scraping
    kabum_urls = [
        'https://www.kabum.com.br/produto/691709/pc-gamer-ryzen-5-5600gt-16gb-3200mhz-radeon-vega-7-integrado-a520m-dx-ssd-480gb-m-2-500w-80-plus-3-fans-rgb-neologic-nli89039'
    ]
    
    pichau_urls = [
        # Adicione URLs da Pichau aqui
    ]
    
    # Extrair produtos da Kabum
    for url in kabum_urls:
        print(f"Extraindo produto da Kabum: {url}")
        product = scrape_kabum(url)
        if product:
            all_products.append(product)
        # Pausa para evitar sobrecarga no servidor
        time.sleep(2)
    
    # Extrair produtos da Pichau
    for url in pichau_urls:
        print(f"Extraindo produto da Pichau: {url}")
        product = scrape_pichau(url)
        if product:
            all_products.append(product)
        # Pausa para evitar sobrecarga no servidor
        time.sleep(2)
    
    # Adicionar produtos de demonstração
    demo_products = add_demo_products()
    all_products.extend(demo_products)
    
    # Salvar produtos em db.json
    with open('db.json', 'w', encoding='utf-8') as f:
        json.dump({'produtos': all_products}, f, ensure_ascii=False, indent=2)
    
    print(f"Total de produtos extraídos: {len(all_products)}")
    print("Dados salvos em db.json")

if __name__ == "__main__":
    main() 