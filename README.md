# 🎬 Rede de Cinemas

Sistema de informação para gerenciamento de uma rede de cinemas, desenvolvido como estudo de caso da disciplina de Engenharia de Software.

## 📋 Sobre o Projeto

O sistema centraliza o gerenciamento de cinemas, filmes, sessões e registro de público, aplicando conceitos de UML, arquitetura em camadas e persistência de dados.

## 🏗️ Arquitetura

project/
├── model/          → Entidades do domínio
├── repository/     → Acesso ao banco de dados
├── service/        → Regras de negócio
├── controller/     → Intermediário entre View e Service
├── view/           → Interface terminal e web (Flask)
├── db/             → Conexão e criação do banco SQLite
├── main.py         → Execução via terminal
├── app.py          → Execução via navegador (Flask)
└── requirements.txt

## ⚙️ Funcionalidades

- Cadastrar e listar cinemas
- Cadastrar e listar filmes
- Cadastrar e listar sessões
- Registrar público de uma sessão
- Consultar totalização de público por sessão, filme e cinema

## 🚀 Como Executar

### Pré-requisitos

- Python 3.x
- pip

### Instalação

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio/project
pip install -r requirements.txt
```

### Modo Web

```bash
python app.py
```

Acesse **http://localhost:5000** no navegador.

### Modo Terminal

```bash
python main.py
```

## 🗄️ Banco de Dados

Utiliza **SQLite** — o arquivo `cinema.db` é criado automaticamente na primeira execução. Nenhuma configuração adicional é necessária.

## 🛠️ Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3 | Linguagem principal |
| Flask | Interface web |
| SQLite | Banco de dados |
| PlantUML | Diagramas UML |

## 📚 Disciplina

> Engenharia de Software — Estudo de Caso: Rede de Cinemas
> Arquitetura MVC · UML · SQLite
