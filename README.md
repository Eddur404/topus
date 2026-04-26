# Topus 


## 🧾 Descrição

Olá! Somos alunos do 3º ano de Informática para Internet e estamos desenvolvendo um sistema para a disciplina de PDSI, ministrada pelo professor Pedro Baesse.

O projeto consiste no desenvolvimento de uma aplicação web focada no mapeamento de locais para a prática de atividades físicas, como academias, praças e ciclovias. A plataforma utilizará recursos como imagens e avaliações para ajudar os usuários a encontrar espaços acessíveis, seguros e adequados para a prática de exercícios. Além disso, contará com elementos de gamificação, criando desafios e metas para usuários individualmente ou em grupos com amigos.


## ⚙️ Funcionalidades

* Cadastro de Usuário
* Mapeamento em tempo real
* Relatórios de progresso
* Desafios personalizados
* Rotas personalizadas
* Criar equipes de treino
* Busca de locais
* Filtrar Pesquisa por tipo de exercício
* Avaliações dos usuários 
* Relatar problema
* Criar, editar e validar pontos de atividade física


## 👥 Equipe

| Nome | Função |
|------|--------|
| AUGUSTO MAUX | Frontend, Backend, Design, Documentação |
| EDUARDO FELIPE | Frontend, Backend, Design, Documentação |
| GABRIEL RIAN | Documentação, Pesquisa, Frontend |
| PEDRO VINÍCIOS | Frontend, Design, Documentação e Pesquisa |


## 🚀 Como rodar o projeto

### 🔽 1. Clonar o repositório
```bash
git clone https://gitlab.com/froggers1/topus.git
cd topus
```

### 🔽 2. Criar e acessar a branch
```bash
git checkout -b dev
```

### 🔽 3. Instalar dependências
```bash
npm install Flask
# ou
pip install -r requirements.txt
```

### 🔽 4. Rodar o projeto
```bash
python -m venv venv
. venv/bin/activate
flask run --debug
# ou 
npm run "branch"
```

## 🧠 Estrutura do projeto

```
topus/
├── app/
├── instance/
├── templates/
└── README.md
```


## 📌 Boas práticas de contribuição

* Sempre criar uma branch (dev ou feature)
* Não commitar direto na main
* Fazer commits com mensagens claras
* Abrir merge request para revisão