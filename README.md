# Sistema de Scraping e Exibição de Produtos

Este projeto consiste em um sistema para extrair (scraping) informações de produtos de sites de e-commerce como Kabum e Pichau, armazenar esses dados em um arquivo JSON e exibi-los em uma interface web moderna usando o padrão Ant Design.

## Funcionalidades

- Scraping de produtos da Kabum e Pichau
- Armazenamento de dados em formato JSON
- Download e armazenamento de imagens dos produtos
- Interface web responsiva para exibição dos produtos
- Página de detalhes para cada produto
- Sistema de filtros por categoria, preço e fonte
- Busca por texto nos produtos
- Design moderno com Ant Design
- Animações e transições suaves
- Layout responsivo para todos os dispositivos

## Evolução do Design

O projeto passou por uma significativa evolução visual, adotando o framework Ant Design para criar uma interface mais moderna e profissional.

### Comparação das Versões

#### Página Inicial
- **Versão Antiga**: Design básico com layout simples
- **Nova Versão**: Interface moderna com Ant Design, animações suaves e melhor organização do conteúdo
- *Veja as imagens em: `versaoantiga/inicio.png` e `screenshots/inicio.png`*

#### Página de Produtos
- **Versão Antiga**: Lista simples de produtos
- **Nova Versão**: 
  - Cards modernos com efeitos de hover
  - Sistema de filtros avançado
  - Exibição de especificações técnicas
  - Indicadores de desconto
  - Sistema de avaliação com estrelas
  - Ordenação por preço, avaliação e nome
- *Veja as imagens em: `versaoantiga/produtos.png` e `screenshots/produtos.png`*

#### Página de Serviços
- **Versão Antiga**: Layout básico com texto simples
- **Nova Versão**: 
  - Cards interativos para cada serviço
  - Seção de benefícios
  - FAQ expansível
  - Chamadas para ação destacadas
  - Ícones e elementos visuais modernos
- *Veja as imagens em: `versaoantiga/servicos.png` e `screenshots/servicos.png`*

#### Página de Contato
- **Versão Antiga**: Formulário simples
- **Nova Versão**: 
  - Design moderno com gradientes
  - Validação de campos em tempo real
  - Mapa interativo
  - Ícones informativos
  - Melhor organização das informações de contato
- *Veja as imagens em: `versaoantiga/contato.png` e `screenshots/contato.png`*

## Requisitos

- Python 3.6+
- Bibliotecas Python (listadas em `requirements.txt`)
- Navegador web moderno

## Instalação

1. Clone este repositório:
```
git clone https://github.com/seu-usuario/ecommerce.git
cd ecommerce
```

2. Instale as dependências:
```
pip install -r requirements.txt
```

3. Execute o script de scraping para coletar produtos:
```
python scraper.py
```

4. Gere a imagem de fallback para produtos sem imagem:
```
python gerar_imagem_fallback.py
```

5. Abra o arquivo `index.html` em seu navegador ou use um servidor web local.

## Estrutura do Projeto

- `scraper.py` - Script para extrair produtos dos sites
- `gerar_imagem_fallback.py` - Script para criar imagem padrão para produtos sem imagem
- `db.json` - Banco de dados JSON com informações dos produtos
- `index.html` - Página inicial do site
- `paginas/` - Diretório com as páginas do site
  - `produtos.html` - Página de listagem de produtos
  - `produto-detalhes.html` - Página de detalhes do produto
  - `servicos.html` - Página de serviços
  - `faleconosco.html` - Página de contato
- `imagens/` - Diretório para armazenar imagens
  - `produtos/` - Diretório para imagens dos produtos
- `screenshots/` - Capturas de tela da nova versão
- `versaoantiga/` - Capturas de tela da versão anterior

## Melhorias Implementadas

### Design e UX
- Adoção do framework Ant Design
- Animações e transições suaves
- Layout totalmente responsivo
- Melhor hierarquia visual
- Feedback visual para interações

### Funcionalidades
- Sistema de filtros avançado
- Busca em tempo real
- Ordenação flexível
- Exibição de especificações técnicas
- Sistema de avaliações
- Indicadores de desconto
- FAQ interativo

### Performance
- Carregamento otimizado de imagens
- Código JavaScript modularizado
- CSS otimizado
- Animações eficientes

## Como Usar

### Adicionando Novos Sites para Scraping

Para adicionar um novo site para scraping, você precisa:

1. Criar uma nova função no arquivo `scraper.py` seguindo o padrão das funções existentes
2. Adicionar as URLs do novo site na função `main()`
3. Executar o script novamente para coletar os novos produtos

### Personalizando a Exibição

Você pode personalizar a aparência do site editando os arquivos HTML e CSS. O projeto utiliza o framework Ant Design para a interface, então você pode consultar a [documentação do Ant Design](https://ant.design/) para mais opções de componentes e estilos.

## Limitações e Considerações

- O scraping de sites pode ser afetado por mudanças na estrutura HTML dos sites alvo
- Respeite os termos de serviço dos sites que você está extraindo dados
- Adicione pausas entre requisições para não sobrecarregar os servidores alvo
- Este projeto é apenas para fins educacionais

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.
