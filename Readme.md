
# 🚗 Cars Sale - Seu Principal Destino para Automóveis

Bem-vindo ao **Cars Sale**, uma plataforma inovadora de e-commerce construída com Django, projetada para proporcionar uma experiência fluida na busca, compra e venda de carros. Seja você um comprador em busca do carro dos sonhos ou um vendedor querendo listar seu veículo, o Cars Sale oferece um ambiente moderno, intuitivo e seguro.

## ✨ Funcionalidades

* **Autenticação de Usuário**: Funcionalidades seguras de registro, login e logout de usuários.
* **Listagem de Carros**: Navegue por um catálogo completo de carros com detalhes como modelo, ano, preço, cor e marca.
* **Detalhes do Carro**: Visualize informações detalhadas sobre cada carro, incluindo uma descrição dinâmica gerada por IA e uma imagem.
* **Gerenciamento de Carros (CRUD)**: Usuários autenticados podem criar, atualizar e excluir listagens de carros.
* **Funcionalidade de Busca**: Encontre carros facilmente pesquisando pelo modelo.
* **Upload de Imagens**: Faça upload de fotos de carros para enriquecer as listagens.
* **Monitoramento Dinâmico de Inventário**: Atualizações em tempo real sobre o número total de carros e seu valor coletivo no inventário.
* **Validações de Formulário Personalizadas**: Garante a integridade dos dados, como impedir preços de carros abaixo de um certo limite.
* **Descrições Geradas por IA**: Utilize a API Google Gemini para gerar descrições envolventes e informativas para os carros.

## 🛠️ Tecnologias Utilizadas

* **Backend**: Django
* **Banco de Dados**: PostgreSQL
* **Frontend**: HTML, CSS
* **Integração de API**: Google Gemini API
* **Deployment**: ASGI, WSGI
* **Gerenciamento de Dependências**: `pip` e `requirements.txt`

## 🚀 Primeiros Passos

Siga estas etapas para ter uma cópia do projeto em execução na sua máquina local para fins de desenvolvimento e teste.

### Pré-requisitos

* Python 3.8+
* pip
* PostgreSQL

### Instalação

1.  **Clone o repositório**:

    ```bash
    git clone [https://github.com/MenegussiT/Ecommerce_CarsSale.git](https://github.com/MenegussiT/Ecommerce_CarsSale.git)
    cd Ecommerce_CarsSale
    ```

2.  **Crie um ambiente virtual** e ative-o:

    ```bash
    python -m venv venv
    # No Windows
    venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências**:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure o Banco de Dados**:
    Abra `app/settings.py` e configure suas definições de banco de dados PostgreSQL:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'cars', # Nome do seu banco de dados
            'USER' : 'postgres', # Seu usuário PostgreSQL
            'PASSWORD' : 'YOUR_DB_PASSWORD', # Sua senha PostgreSQL
            'HOST' : 'localhost',
            'PORT' : '5432',
        }
    }
    ```

5.  **Crie um arquivo `.env`** no diretório raiz do projeto e adicione sua Chave de API Google Gemini:

    ```
    GEMINI_API_KEY=SUA_CHAVE_API_GEMINI
    ```

6.  **Execute as migrações do banco de dados**:

    ```bash
    python manage.py makemigrations cars
    python manage.py migrate
    ```

7.  **Crie um superusuário** (para acesso administrativo):

    ```bash
    python manage.py createsuperuser
    ```

8.  **Execute o servidor de desenvolvimento**:

    ```bash
    python manage.py runserver
    ```

    A aplicação estará acessível em `http://127.0.0.1:8000/`.

## 🖥️ Uso

* **Registrar**: Navegue para `http://127.0.0.1:8000/register/` para criar uma nova conta de usuário.
* **Login**: Acesse a página de login em `http://127.0.0.1:8000/login/`.
* **Ver Carros**: Todos os carros disponíveis estão listados em `http://127.0.0.1:8000/cars/`.
* **Adicionar Novo Carro**: Usuários logados podem adicionar novas listagens de carros através de `http://127.0.0.1:8000/new_car/`.
* **Atualizar/Excluir Carro**: Na página de detalhes de um carro, usuários logados verão opções para atualizar ou excluir a listagem.
* **Painel Administrativo**: Acesse a interface de administração do Django em `http://127.0.0.1:8000/admin/` usando suas credenciais de superusuário.

## 🤝 Contribuindo

Contribuições são bem-vindas! Se você tiver alguma sugestão, relatório de bugs ou quiser contribuir para o código, sinta-se à vontade para:

1.  Fazer um fork do repositório.
2.  Criar uma nova branch (`git checkout -b feature/SuaFuncionalidade`).
3.  Fazer suas alterações.
4.  Comitar suas alterações (`git commit -m 'Adiciona alguma funcionalidade'`).
5.  Fazer push para a branch (`git push origin feature/SuaFuncionalidade`).
6.  Abrir um Pull Request.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT.

## 📧 Contato

Para qualquer dúvida ou colaboração, sinta-se à vontade para entrar em contato com:

* **MenegussiT** - [Seu E-mail Aqui] - [Seu Perfil do LinkedIn/GitHub]
