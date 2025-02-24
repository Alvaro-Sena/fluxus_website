# **CASA FLUXUS** - Website
Este projeto implementa um **website** onde junto conceitos aprendidos no curso de **Introdução à Ciência da Computação** , oferecido pela **Harvard University** e foi apresentado como projeto final, envolvendo diversas tecnologias, como HTML, CSS, JavaScript e AJAX para interação com o usuário, Python com o framework Flask para gerenciamento das rotas e SQLite para gerenciar um banco de dados, este é um excelente exemplo de site dinâmico com controle de acesso granular, onde estar registrado ou não, alterar como o usuário visualiza o site. A sessões, gerenciadas pelo Flask-Session e conteúdo das rotas implementadas com Jinja2, além de sempre se atualizar a medida que os usuários registrados postam comentários, que são armazenados em um banco de dados SQLite. 

### **Descrição:**  

Fluxus é um projeto desenvolvido para **nômades digitais**, pessoas que buscam uma conexão mais profunda com a natureza e interessadas em aprender técnicas de **vida sustentável** e práticas de **preservação ambiental**. Em sua essência, Fluxus é uma iniciativa de preservação cultural e ambiental onde indivíduos podem hospedar-se e contribuir realizando diversos serviços, como cozinhar, ajudar na limpeza do terreno, plantar e outras atividades. Os participantes podem até assumir responsabilidade por um novo projeto e incentivar maior engajamento comunitário.  

O principal objetivo do Fluxus é criar uma plataforma para que as pessoas experimentem o **fluxo da vida**, aprendam, cresçam e contribuam para a preservação do meio ambiente. Esta iniciativa foca em **autossustentabilidade**, **socialização** e **compartilhamento de conhecimento**. O projeto é construído em torno do conceito de uma **"base nômade"**, onde indivíduos de todo o mundo podem se reunir para compartilhar experiências, participar de projetos ambientais práticos e engajar-se ativamente na preservação da natureza. 

---

### **Tecnologias Utilizadas**  

Para dar vida a este projeto, foram utilizadas diversas tecnologias:  
- **Backend**:  
  - **Python** com o framework **Flask** para gerenciamento de rotas e lógica do servidor.  
  - **SQLite** para armazenamento de dados de usuários, projetos e comentários.  
  - **Flask-Session** para gerenciamento de sessões de usuário.  
- **Frontend**:  
  - **HTML**, **CSS** e **JavaScript** para interfaces dinâmicas.  
  - **AJAX** para atualizações em tempo real.  
  - **Jinja2** (motor de templates do Flask) para renderização de páginas dinâmicas.  
- **APIs Externas**:  
  - Integração com API de seleção de países para formulários de registro.  
  - **Google Maps** para exibição da localização física do projeto.  

---
### **Como visualizar o website**###

1. Clone o repositório:  
   ```bash
   git clone https://github.com/Alvaro-Sena/fluxus_website.git  
   ```
2. Navegue até a pasta do projeto:  
   ```bash  
   cd fluxus_website  
   ```  
3. Instale as dependências:  
   ```bash  
   pip install -r requirements.txt  
   ```   
4. Execute Flask:  
   ```bash  
   flask run   
   ```
   
   
### **Estrutura e Funcionalidades do Site**  

#### **Página Inicial**  
- Introdução ao projeto com visão geral das iniciativas.  
- Links para **Sobre Nós**, **Projetos**, **Apoie-nos** e **Contato**.  
- Interface responsiva adaptada para dispositivos móveis.  

#### **Página de Registro**  
- Formulário com validação em tempo real:  
  - Nome, e-mail, país de origem (via API) e senha segura (mínimo 8 caracteres, letras + números).  
  - Feedback imediato para erros de entrada como disponibilidade de username e compatibilidade de senhas usando AJAX.  

#### **Página Sobre Nós**  
- Descrição detalhada do projeto e sua missão.  
- Seção de comentários de usuários onde apenas usuários cadastrado podem adicionar um novo comentário e não cadastrados podem apenas ler.  

#### **Página de Projetos**  
- Exibição de iniciativas em carrossel:  
  - Título, 3 imagens e descrição resumida por projeto.

#### **Página Apoie-nos**  
- Opções de contribuição:  
  - Convite para se registrar e deixar um comentário (para usuários nao logados).  
  - Doações via transferência bancária (detalhes fornecidos).  

#### **Página de Contato**  
- Informações de contato: telefone, e-mail e endereço físico.  
- Mapa interativo do Google Maps integrado.  

---

### **Banco de Dados**  
- **Tabelas Principais**:  
  - `users`: Armazena nome, e-mail, país, senha (hash).  
  - `projects`: Registra título, descrição, imagens.  
  - `comments`: Relaciona usuários a projetos com textos e datas.  

---

#### **Melhorias Futuras**  
- 🔄 **Recuperação de Senha**: Sistema automático via e-mail.  
- 💬 **Chat Interno**: Comunicação direta entre usuários.  
- 🌐 **Integração com Plataformas de Voluntariado**: Ampliar alcance (ex: Workaway, WWOOF).  
- 💳 **Sistema de Doação Online**: Pagamentos via PIX/cartão.  

---

