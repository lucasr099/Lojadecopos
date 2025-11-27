# 🛒 Chatbot Loja de Copos — FastAPI + React + Gemini + SQLite

Este projeto é um **chatbot integrado a um mini e-commerce de copos**, capaz de responder perguntas sobre **estoque, preço e descrição dos produtos**, utilizando **Google Gemini** como LLM.

O sistema é composto por:

* **Backend**: FastAPI + SQLite + SQLAlchemy + Gemini
* **Frontend**: React + Vite + Axios
* **Chatbot**: responde com base nos dados reais do banco
* **Banco de Dados**: tabela simples com produtos (copos)

---

# 📦 1. Estrutura do Projeto

```
backend/
│── main.py
│── chat.py
│── db.py
│── models.py
│── seed.sql
│── store.db
│── test/
│     ├── test_health.py
│     └── test_products.py

frontend/
│── index.html
│── package.json
│── vite.config.js
│── src/
│     ├── App.jsx
│     └── main.jsx
```

---

# 🗄️ 2. Banco de Dados

O banco usado é **SQLite**, localizado em:

```
backend/store.db
```

## 🏷️ Tabela: `products`

| Campo       | Tipo       | Descrição                        |
| ----------- | ---------- | -------------------------------- |
| id          | INTEGER PK | Identificador único do produto   |
| name        | TEXT       | Nome do copo                     |
| description | TEXT       | Descrição simples do produto     |
| price       | REAL       | Preço do copo                    |
| stock       | INTEGER    | Quantidade disponível no estoque |

## 📌 Dados usados no projeto (seed.sql)

```sql
INSERT INTO products (name, description, price, stock) VALUES
('Copo Azul', 'Copo de plástico azul', 12.90, 30),
('Copo Vermelho', 'Copo vermelho decorado', 11.90, 25),
('Copo Amarelo', 'Copo amarelo fosco', 10.50, 20),
('Copo Verde', 'Copo verde translúcido', 12.00, 18),
('Copo Roxo', 'Copo roxo premium', 13.50, 15),
('Copo Lilás', 'Copo lilás suave', 12.20, 22),
('Copo Preto', 'Copo preto elegante', 14.50, 30),
('Copo Laranja', 'Copo laranja resistente', 12.90, 16),
('Copo Branco', 'Copo branco clássico', 9.90, 50),
('Copo Cinza', 'Copo cinza minimalista', 11.90, 27);
```

Esses dados são exatamente os que o chatbot usa para responder.

---

# 🤖 3. Como o Chatbot Funciona

Quando o usuário faz perguntas como:

> “Quantas unidades do copo azul tem?”
> “Qual o preço do copo lilás?”
> “Tem copo preto disponível?”

O backend executa:

1. Extrai palavras-chave da pergunta
2. Pesquisa no banco de dados
3. Envia para o Gemini informações como:

   * Nome
   * Descrição
   * Preço
   * Estoque
4. O Gemini gera uma resposta amigável baseada somente nesses dados reais

✔ O chatbot **não inventa produtos**
✔ O chatbot **não responde sobre itens que não estão na tabela**
✔ O chatbot **usa somente os copos cadastrados no banco**

---

# ⚙️ 4. Como Rodar o Backend (FastAPI)

### 1️⃣ Ative o ambiente virtual

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 2️⃣ Instale as dependências

```
pip install -r requirements.txt
```

### 3️⃣ Popular o banco de dados

```
sqlite3 store.db < seed.sql
```

### 4️⃣ Crie o arquivo `.env` na pasta backend

```
GEMINI_API_KEY=SUA_CHAVE_AQUI
```

### 5️⃣ Execute a API

```
uvicorn main:app --reload
```

A API estará disponível em:

```
http://localhost:8000
```

Documentação automática FastAPI:

```
http://localhost:8000/docs
```

---

# 💻 5. Como Rodar o Frontend (React)

Entre na pasta **frontend/**:

### 1️⃣ Instalar dependências

```
npm install
```

### 2️⃣ Rodar projeto

```
npm run dev
```

A aplicação abre em:

```
http://localhost:5173
```

---

# 🧪 6. Testes Automatizados

Rodar testes:

```
pytest -v
```

Inclui testes de:

* healthcheck (`/health`)
* listagem de produtos

---

# 📡 7. Endpoints do Backend

### ✔ Listar produtos

```
GET /products
```

### ✔ Buscar produto por ID

```
GET /products/{id}
```

### ✔ Chatbot

```
POST /chat
{
  "question": "quantos copos azuis tem?"
}
```

### ✔ Healthcheck

```
GET /health
```

---

# 🧠 8. Fluxo Completo do Chatbot

```
Usuário → Frontend React → Backend FastAPI → Banco SQLite
       → Gemini → Resposta inteligente → Frontend
```

---

# 📚 9. Tecnologias Utilizadas

### Backend

* FastAPI
* SQLAlchemy
* SQLite
* Google Gemini
* Pytest
* Python 3.10+

### Frontend

* React
* Vite
* Axios

---

# 🏁 10. Conclusão

Este projeto demonstra:

✔ Integração entre frontend, backend e IA
✔ Consulta real a banco de dados
✔ Chatbot especializado em produtos (copos)
✔ Totalmente funcional e pronto para produção

---Se quiser, gero **README com imagens**, **diagramas**, ou **versão em inglês** também!
