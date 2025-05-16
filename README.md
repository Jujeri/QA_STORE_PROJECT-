  # 🧪 QA_STORE_PROJECT — Estrutura de Projeto de Testes Automatizados

Este repositório contém um projeto de testes automatizados utilizando **Behave (BDD)**, **Robot Framework**, **Selenium**, e integração com **banco de dados**. Abaixo está a descrição de cada pasta para facilitar o entendimento da arquitetura.

---

## 📂 `_fixtures/` — Dados de Apoio

Armazena arquivos e dados usados como suporte para os testes.

- `data/` 📁 — Massas de teste (ex: `.json`, `.csv`, etc).

- `database/` 📁 — Scripts e configurações de banco de dados:

  - `sql/` 📁 — Scripts SQL de insert, delete, reset etc.

  - `database.yaml` 📄 — Arquivo com as configurações de conexão (ex: host, usuário, senha).

---

## 📂 `_support/` — Suporte Técnico

Contém arquivos auxiliares que dão suporte à automação.

- `python_files/` 🐍 — Utilitários Python usados por testes ou steps:

  - `environment_hooks.py` — Hooks globais do Behave.

  - `mongo_connection.py` — Conexão com banco MongoDB.

  - `helpers.py` — Funções reutilizáveis para os testes.

- `robot_files/` 🤖 — Keywords customizadas ou módulos reutilizáveis em `.robot`.

---

## 📂 `elements/` — Elementos da Interface

Contém os seletores e identificadores dos elementos das páginas (UI), organizados por contexto. Segue o padrão Page Elements.

---

## 📂 `environment/` — Configurações por Ambiente

Define variáveis específicas por ambiente (ex: `dev`, `staging`, `prod`) como URLs, tokens e credenciais.

---

## 📂 `features/` — Cenários BDD com Behave

Organização dos arquivos Gherkin e seus respectivos steps.

- `login.feature` — Cenário de teste escrito em Gherkin.

- `steps/` 📁 — Implementações Python dos passos (`Given`, `When`, `Then`):

  - `login_steps.py` — Implementa os passos do login.

- `environment.py` — Hook global do Behave (pode importar funções do `_support`).

---

## 📂 `pages/` — Page Object Model

Scripts que encapsulam a lógica de interação com as páginas.

- `login_page.py` — Ações e elementos da página de login.

---

## 📂 `test_plan/` — Planejamento de Testes

Arquivos usados para planejamento e documentação dos testes.

- `casos_de_teste.xlsx` 📊 — Planilha com casos de teste manuais.

- `plano_de_teste.md` 📄 — Estratégia de testes, ferramentas utilizadas, critérios de entrada e saída.

---

## 📂 `tests/` — Testes Automatizados com Robot Framework

Organizados por tipo de teste:

- `Api/auth/login.robot` 🔐 — Testes de autenticação via API.

- `Frontend/login/login.robot` 🖥️ — Testes de login na interface web.

---

## 📂 `.github/workflows/` — Integração Contínua (CI)

Configuração dos workflows de CI no GitHub Actions.

- `run_tests.yaml` ⚙️ — Pipeline para execução automática dos testes.

---

## 📄 Arquivos Raiz

- `README.md` 📝 — Documentação geral do projeto.

- `requirements.txt` 📦 — Lista de dependências Python necessárias para o projeto.

---

### ✅ Tecnologias Utilizadas

- `Python`

- `Behave` (BDD)

- `Robot Framework`

- `Selenium`

- `MongoDB` / `SQL`

- `GitHub Actions` (CI/CD)

---

### 🚀 Sugestão de Comandos

```bash

# Executar testes com Behave

behave features/

# Executar testes com Robot

robot tests/

# Ativar virtualenv e instalar dependências

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt



    🗂️ Estrutura geral
QA_STORE_PROJECT/
├── _fixtures/
│   ├── data/                      # Dados de massa (JSON, CSV, etc)
│   └── database/                 # Arquivos relacionados a conexão com banco
│       ├── sql/                  # Scripts SQL de mock ou verificação
│       └── database.yaml         # Configurações de conexão (host, porta, etc.)
│
├── elements/                     # Mapeamento de elementos (caso use Selenium com RF)
│
├── environment/                  # Configurações de ambiente de execução
│
├── _support/
│   ├── python_files/             # Utilitários e hooks Python
│   │   ├── environment_hooks.py
│   │   ├── mongo_connection.py
│   │   └── helpers.py
│   └── robot_files/              # Keywords customizadas em RF (separadas por contexto)
│
├── features/                     # Diretório principal do Behave
│   ├── steps/
│   │   └── login_steps.py
│   ├── login.feature
│   └── environment.py            # Aponta para os hooks de _support
│
├── tests/                        # Casos de teste Robot Framework
│   ├── Api/
│   │   └── auth/
│   │       └── login.robot
│   ├── Frontend/
│   │   └── login/
│   │       └── login.robot
│
├── pages/                        # Page Objects, usados se necessário
│   └── login_page.py
│
├── test_plan/
│   ├── casos_de_teste.xlsx
│   └── plano_de_teste.md
│
├── .github/workflows/
│   └── run_tests.yaml            # CI com GitHub Actions
│
├── README.md
└── requirements.txt