🛒 Bot Loja de Copos — FastAPI + React + Gemini + SQL

Projeto desenvolvido para o processo seletivo: chatbot integrado a um e-commerce simples.

📌 Resumo do Projeto

Aplicação full-stack composta por:

🔸 Backend (FastAPI, Python)

API REST completa

Integração com Google Gemini (LLM)

Banco de dados SQLite

Rotas para produtos, healthcheck e chatbot

Testes unitários com pytest

Script SQL para popular o banco

Arquitetura organizada em módulos

🔸 Frontend (React + Vite)

Interface simples e funcional

Comunicação com backend via Axios

Campo de pergunta e exibição da resposta do chatbot

🗂️ Arquitetura do Projeto
backend/
│── main.py
│── chat.py
│── models.py
│── db.py
│── seed.sql
│── store.db
│── test/
│     ├── test_health.py
│     └── test_products.py
│
frontend/
│── index.html
│── package.json
│── src/
│     ├── App.jsx
│     └── main.jsx
⚙️ Tecnologias Utilizadas
Backend

Python 3.10+

FastAPI

SQLAlchemy

SQLite

Google Gemini (LLM)

Pytest

Uvicorn

Frontend

React

Vite

Axios

🚀 Como Rodar o Projeto
🔧 1. Ativar o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
📦 2. Instalar dependências
pip install -r requirements.txt
🗄️ 3. Criar/Popular o Banco de Dados
sqlite3 store.db < seed.sql
▶️ 4. Iniciar o backend
uvicorn main:app --reload

A API estará em:
👉 http://127.0.0.1:8000

💻 Rodar o Frontend

No diretório frontend/:

npm install
npm run dev

Frontend disponível em:
👉 http://localhost:5173/

🧪 Testes
Rodar todos os testes
pytest -v
Testes disponíveis:

test_health.py → valida se API está funcionando

test_products.py → valida listagem de produtos

🤖 Como o Chatbot Funciona

O endpoint /chat/ recebe a mensagem do usuário e:

Detecta se a frase é relacionada a produtos de copo

Extrai palavras-chave

Consulta o banco de dados

Se 1 produto é encontrado → retorna preço + estoque

Se vários são encontrados → pede para escolher

Se nenhum é encontrado → oferece sugestões

Usa LLM Gemini para gerar resposta final seguindo regras rígidas

🔐 Variáveis de Ambiente

Criar arquivo .env:

GEMINI_API_KEY=suachaveaqui
📄 Endpoints
GET /health

Retorna status da API.

GET /products/

Lista todos os produtos do banco.

POST /chat/

Recebe { "message": "..." } e retorna resposta do bot.

📘 Script SQL (seed.sql)

Contém todos os produtos iniciais que serão carregados no banco.

📚 Conclusão

Este projeto cumpre todos os requisitos solicitados:

✔ Chatbot funcional
✔ LLM Gemini integrado
✔ Backend FastAPI
✔ Banco SQL
✔ Testes (pytest)
✔ Documentação completa
✔ Frontend React

Pronto para apresentar em processo seletivo.🛒 Bot Loja de Copos — FastAPI + React + Gemini + SQL

Projeto desenvolvido para o processo seletivo: chatbot integrado a um e-commerce simples.

📌 Resumo do Projeto

Aplicação full-stack composta por:

🔸 Backend (FastAPI, Python)

API REST completa

Integração com Google Gemini (LLM)

Banco de dados SQLite

Rotas para produtos, healthcheck e chatbot

Testes unitários com pytest

Script SQL para popular o banco

Arquitetura organizada em módulos

🔸 Frontend (React + Vite)

Interface simples e funcional

Comunicação com backend via Axios

Campo de pergunta e exibição da resposta do chatbot

🗂️ Arquitetura do Projeto
backend/
│── main.py
│── chat.py
│── models.py
│── db.py
│── seed.sql
│── store.db
│── test/
│     ├── test_health.py
│     └── test_products.py
│
frontend/
│── index.html
│── package.json
│── src/
│     ├── App.jsx
│     └── main.jsx
⚙️ Tecnologias Utilizadas
Backend

Python 3.10+

FastAPI

SQLAlchemy

SQLite

Google Gemini (LLM)

Pytest

Uvicorn

Frontend

React

Vite

Axios

🚀 Como Rodar o Projeto
🔧 1. Ativar o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
📦 2. Instalar dependências
pip install -r requirements.txt
🗄️ 3. Criar/Popular o Banco de Dados
sqlite3 store.db < seed.sql
▶️ 4. Iniciar o backend
uvicorn main:app --reload

A API estará em:
👉 http://127.0.0.1:8000

💻 Rodar o Frontend

No diretório frontend/:

npm install
npm run dev

Frontend disponível em:
👉 http://localhost:5173/

🧪 Testes
Rodar todos os testes
pytest -v
Testes disponíveis:

test_health.py → valida se API está funcionando

test_products.py → valida listagem de produtos

🤖 Como o Chatbot Funciona

O endpoint /chat/ recebe a mensagem do usuário e:

Detecta se a frase é relacionada a produtos de copo

Extrai palavras-chave

Consulta o banco de dados

Se 1 produto é encontrado → retorna preço + estoque

Se vários são encontrados → pede para escolher

Se nenhum é encontrado → oferece sugestões

Usa LLM Gemini para gerar resposta final seguindo regras rígidas

🔐 Variáveis de Ambiente

Criar arquivo .env:

GEMINI_API_KEY=suachaveaqui
📄 Endpoints
GET /health

Retorna status da API.

GET /products/

Lista todos os produtos do banco.

POST /chat/

Recebe { "message": "..." } e retorna resposta do bot.

📘 Script SQL (seed.sql)

Contém todos os produtos iniciais que serão carregados no banco.

📚 Conclusão

Este projeto cumpre todos os requisitos solicitados:

✔ Chatbot funcional
✔ LLM Gemini integrado
✔ Backend FastAPI
✔ Banco SQL
✔ Testes (pytest)
✔ Documentação completa
✔ Frontend React

Pronto para apresentar em processo seletivo.
