# ASIMOV - Site Institucional

## Visão Geral

**ASIMOV** é um site institucional desenvolvido para apresentar informações sobre a organização, seus produtos, serviços e facilitar o contato com clientes. O projeto utiliza uma estrutura básica de HTML, CSS e JavaScript para criar uma navegação interativa e intuitiva.

## Funcionalidades

- **Navegação por Menu:**
  - **Página Inicial:** Introdução à organização e visão geral.
  - **Produtos:** Detalhes sobre os produtos oferecidos.
  - **Serviços:** Descrição dos serviços disponibilizados.
  - **Fale Conosco:** Formulário para contato com a equipe.

- **Integração com Iframe:**
  - As páginas são carregadas dinamicamente dentro de um iframe para manter a navegação fluida.

- **Efeitos Interativos:**
  - Destaque do menu ativo utilizando **jQuery**.

## Tecnologias Utilizadas

- **HTML5:** Estrutura da aplicação.
- **CSS3:** Estilização personalizada.
- **JavaScript:** Funcionalidade do menu.
- **jQuery:** Manipulação de DOM e interatividade.

## Estrutura do Projeto

```
ASIMOV/
├── index.html            # Página principal
├── css/
│   └── style.css         # Estilos CSS
├── js/
│   └── jquery.min.js     # Biblioteca jQuery
├── paginas/
│   ├── inicio.html       # Página Inicial
│   ├── produtos.html     # Página de Produtos
│   ├── servicos.html     # Página de Serviços
│   └── faleconosco.html  # Página de Contato
├── README.md             # Documentação do projeto
```

## Instalação

1. **Clone o Repositório**

   ```bash
   git clone https://github.com/dougdotcon/ASIMOV.git
   ```

2. **Navegue até o Diretório do Projeto**

   ```bash
   cd ASIMOV
   ```

3. **Abra o Arquivo `index.html` no Navegador**

   Você pode abrir o arquivo diretamente no seu navegador preferido clicando duas vezes sobre ele ou utilizando um servidor local.

   **Usando um Servidor Local com Python:**

   ```bash
   # Para Python 3.x
   python -m http.server 8000

   # Acesse http://localhost:8000 no seu navegador
   ```

## Uso

1. **Navegação**
   - Utilize o menu à esquerda para acessar diferentes páginas: Página Inicial, Produtos, Serviços e Fale Conosco.
   - O conteúdo será exibido no painel direito sem recarregar a página.

2. **Interatividade**
   - O item do menu ativo é destacado dinamicamente ao clicar.

3. **Personalização**
   - Edite as páginas HTML em `paginas/` para adicionar ou atualizar informações.

## Contribuição

Contribuições são bem-vindas! Para colaborar, siga os passos abaixo:

1. **Fork este Repositório**
2. **Crie uma Branch para sua Contribuição**

   ```bash
   git checkout -b feature/nova-feature
   ```

3. **Commit suas Alterações**

   ```bash
   git commit -m "Adiciona nova feature"
   ```

4. **Push para a Branch**

   ```bash
   git push origin feature/nova-feature
   ```

5. **Abra um Pull Request**

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

- **Autor:** Douglas H. Machado
- **Email:** [dougdotcon@gmail.om](mailto:dougdotcon@gmail.om)
- **LinkedIn:** [dougdoton](https://www.linkedin.com/in/dougdoton/)
- **GitHub:** [dougdotcon](https://github.com/dougdotcon)

---

*ASIMOV é um projeto criado para facilitar a apresentação de informações institucionais e o contato com clientes, oferecendo uma interface simples e eficiente.*
