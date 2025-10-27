# API REST Django - Catálogo de Filmes 🎬

Uma API REST completa para gerenciar um catálogo de filmes com sistema de avaliações, desenvolvida com Django e Django REST Framework.

## 📋 Descrição

Este projeto implementa uma API REST para gerenciar filmes e suas avaliações. Oferece duas versões de API (V1 e V2) com diferentes abordagens arquiteturais, permitindo flexibilidade na escolha do endpoint.

## 🚀 Tecnologias

- **Python 3.13**
- **Django 5.2.7**
- **Django REST Framework 3.16.1**
- **DRF Nested Routers 0.93.4**
- **SQLite3** (banco de dados padrão)

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone <seu-repositorio>
cd Api\ Rest\ Django
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute as migrações

```bash
python manage.py migrate
```

### 6. Crie um superusuário (opcional)

```bash
python manage.py createsuperuser
```

### 7. Inicie o servidor

```bash
python manage.py runserver
```

O servidor estará disponível em `http://127.0.0.1:8000`

## 📚 Modelos

### Modelo Base (Abstract)

Todos os modelos herdam de uma classe `Base` que fornece:
- `criacao`: Data/hora de criação (auto_now_add)
- `atualizacao`: Data/hora da última atualização (auto_now)
- `ativo`: Status de atividade (padrão: True)

### Filme

```python
{
    "id": 1,
    "titulo": "Um sonho de liberdade",
    "url": "https://www.youtube.com/watch?v=...",
    "criacao": "2025-10-14T20:09:10.236170-03:00",
    "ativo": true,
    "avaliacoes": [1, 2, 3]
}
```

**Campos:**
- `titulo` (CharField, max_length=255)
- `url` (URLField, única)
- `avaliacoes` (relacionamento reverso)

### Avaliação

```python
{
    "id": 3,
    "filme": 3,
    "nome": "Ramon Valdez",
    "email": "ramon@example.com",
    "comentario": "Filme de comedia",
    "avaliacao": "9.8",
    "criacao": "2025-10-14T20:17:05.262435-03:00",
    "ativo": true
}
```

**Campos:**
- `filme` (ForeignKey para Filme)
- `nome` (CharField, max_length=255)
- `email` (EmailField) - somente escrita (write_only)
- `comentario` (TextField, opcional)
- `avaliacao` (DecimalField, até 3 dígitos com 1 casa decimal)

**Restrições:**
- Combinação única de (email, filme) - um usuário pode avaliar um filme apenas uma vez

## 🔌 Endpoints da API

### API V1 (Views Genéricas)

#### Filmes

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/v1/filmes/` | Lista todos os filmes |
| POST | `/api/v1/filmes/` | Cria um novo filme |
| GET | `/api/v1/filmes/<id>/` | Obtém um filme específico |
| PUT | `/api/v1/filmes/<id>/` | Atualiza um filme |
| PATCH | `/api/v1/filmes/<id>/` | Atualiza parcialmente um filme |
| DELETE | `/api/v1/filmes/<id>/` | Deleta um filme |

#### Avaliações Gerais

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/v1/avaliacoes/` | Lista todas as avaliações |
| POST | `/api/v1/avaliacoes/` | Cria uma nova avaliação |
| GET | `/api/v1/avaliacoes/<id>/` | Obtém uma avaliação específica |
| PUT | `/api/v1/avaliacoes/<id>/` | Atualiza uma avaliação |
| DELETE | `/api/v1/avaliacoes/<id>/` | Deleta uma avaliação |

#### Avaliações por Filme

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/v1/filmes/<filme_id>/avaliacoes/` | Lista avaliações de um filme |
| POST | `/api/v1/filmes/<filme_id>/avaliacoes/` | Cria avaliação para um filme |
| GET | `/api/v1/filmes/<filme_id>/avaliacoes/<avaliacao_id>/` | Obtém avaliação específica de um filme |
| PUT | `/api/v1/filmes/<filme_id>/avaliacoes/<avaliacao_id>/` | Atualiza avaliação de um filme |
| DELETE | `/api/v1/filmes/<filme_id>/avaliacoes/<avaliacao_id>/` | Deleta avaliação de um filme |

### API V2 (ViewSets com Routers)

#### Filmes

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/v2/filmes/` | Lista todos os filmes |
| POST | `/api/v2/filmes/` | Cria um novo filme |
| GET | `/api/v2/filmes/<id>/` | Obtém um filme específico |
| PUT | `/api/v2/filmes/<id>/` | Atualiza um filme |
| DELETE | `/api/v2/filmes/<id>/` | Deleta um filme |
| GET | `/api/v2/filmes/<id>/avaliacoes/` | Ação customizada - lista avaliacoes do filme |

#### Avaliações Gerais

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/v2/avaliacoes/` | Lista todas as avaliações |
| POST | `/api/v2/avaliacoes/` | Cria uma nova avaliação |
| GET | `/api/v2/avaliacoes/<id>/` | Obtém uma avaliação específica |
| PUT | `/api/v2/avaliacoes/<id>/` | Atualiza uma avaliação |
| DELETE | `/api/v2/avaliacoes/<id>/` | Deleta uma avaliação |

#### Avaliações Aninhadas por Filme (Nested Router)

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/v2/filmes/<filme_id>/avaliacoes/` | Lista avaliações de um filme |
| POST | `/api/v2/filmes/<filme_id>/avaliacoes/` | Cria avaliação para um filme |
| GET | `/api/v2/filmes/<filme_id>/avaliacoes/<avaliacao_id>/` | Obtém avaliação específica de um filme |
| PUT | `/api/v2/filmes/<filme_id>/avaliacoes/<avaliacao_id>/` | Atualiza avaliação de um filme |
| DELETE | `/api/v2/filmes/<filme_id>/avaliacoes/<avaliacao_id>/` | Deleta avaliação de um filme |

## 📝 Exemplos de Uso

### Criar um Filme

```bash
curl -X POST http://127.0.0.1:8000/api/v1/filmes/ \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Matrix",
    "url": "https://www.youtube.com/watch?v=example"
  }'
```

### Criar uma Avaliação

```bash
curl -X POST http://127.0.0.1:8000/api/v1/filmes/1/avaliacoes/ \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "João Silva",
    "email": "joao@example.com",
    "comentario": "Ótimo filme!",
    "avaliacao": "9.5"
  }'
```

### Obter Avaliação Específica de um Filme

```bash
curl http://127.0.0.1:8000/api/v1/filmes/1/avaliacoes/1/
```

### Atualizar uma Avaliação

```bash
curl -X PUT http://127.0.0.1:8000/api/v1/filmes/1/avaliacoes/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "comentario": "Filme incrível!",
    "avaliacao": "10.0"
  }'
```

### Deletar uma Avaliação

```bash
curl -X DELETE http://127.0.0.1:8000/api/v1/filmes/1/avaliacoes/1/
```

## 🔐 Autenticação e Permissões

A API utiliza as seguintes configurações de segurança:

- **Autenticação**: SessionAuthentication + TokenAuthentication
- **Permissões**: IsAuthenticatedOrReadOnly (leitura pública, escrita requer autenticação)
- **Paginação**: PageNumberPagination com 1 item por página

Para autenticar, inclua o token no header:
```bash
curl -H "Authorization: Token seu_token_aqui" http://127.0.0.1:8000/api/v1/filmes/
```

## 🗄️ Admin Panel

Acesse o painel administrativo em `http://127.0.0.1:8000/admin/`

**Modelos disponíveis:**
- **Filme**: Exibe título, URL, data de criação, atualização e status
- **Avaliação**: Exibe filme, nome, email, nota, data de criação, atualização e status

## 📁 Estrutura do Projeto

```
Api Rest Django/
├── catalogo/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── views_old.py
├── filmes/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```

## ⚙️ Configurações Importantes

### settings.py

```python
# Idioma e Timezone
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

# DEBUG (desativar em produção)
DEBUG = True

# Aplicativos instalados
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'catalogo',
]
```

## 🔧 Desenvolvimento

### Criar migrações após alterações nos modelos

```bash
python manage.py makemigrations
python manage.py migrate
```

### Executar testes

```bash
python manage.py test
```

### Shell interativo

```bash
python manage.py shell
```

## 🚨 Tratamento de Erros

A API retorna respostas HTTP apropriadas:

- **200 OK**: Requisição bem-sucedida
- **201 Created**: Recurso criado com sucesso
- **204 No Content**: Recurso deletado com sucesso
- **400 Bad Request**: Dados inválidos
- **404 Not Found**: Recurso não encontrado
- **409 Conflict**: Violação de constraint (ex: email já avaliou o filme)

## 📄 Licença

Este projeto está disponível sob a licença MIT.

## 👨‍💻 Autor

Desenvolvido como um projeto de API REST com Django.

## 📞 Suporte

Para dúvidas ou problemas, verifique:
- Documentação do Django: https://docs.djangoproject.com/
- Documentação do DRF: https://www.django-rest-framework.org/
- Documentação do DRF Nested Routers: https://github.com/alanjds/drf-nested-routers
