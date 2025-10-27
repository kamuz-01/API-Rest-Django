# API REST Django - Catálogo de Filmes 🎬

API REST para gerenciar um catálogo de filmes com sistema de avaliações, desenvolvida com Django e Django REST Framework.

## 📋 Descrição

Este projeto implementa uma API REST para gerenciar filmes e suas avaliações. Oferece duas versões de API (V1 e V2) que permite flexibilidade na escolha do endpoint.

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

## 🔌 Endpoints da API

### API V1 (Views Genéricas)

#### Filmes

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/v1/filmes/` | Lista todos os filmes |
| POST | `/api/v1/filmes/` | Cria um novo filme |
| GET | `/api/v1/filmes/<id>/` | Obtém um filme específico |
| PUT | `/api/v1/filmes/<id>/` | Atualiza um filme |
| DELETE | `/api/v1/filmes/<id>/` | Deleta um filme |

#### Avaliações

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

Desenvolvido como um projeto de API REST com Django com fins acadêmicos para a disciplina Programação Web II no Instituto Federal Catarinense - Campus Fraiburgo.

## 📞 Suporte

Para dúvidas ou problemas, verifique:
- Documentação do Django: https://docs.djangoproject.com/
- Documentação do DRF: https://www.django-rest-framework.org/
- Documentação do DRF Nested Routers: https://github.com/alanjds/drf-nested-routers
