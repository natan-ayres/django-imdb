

---

# django-imdb

Projeto em **Django** para um sistema de avaliação de **Filmes** e **Séries**, utilizando mecânicas de **Grupos**.

## Versão de Desenvolvimento

**1.0**

## Observações

A maioria das ações de gerenciamento de imagens serão realizadas pelo **Administrador**, que terá acesso aos botões de **"+"** em todas as páginas (exceto Grupos) e opções de **Delete** e **Update** para **Filmes**, **Séries** e **Notícias**.

Já os botões de **Delete** e **Update** para **Reviews**, **Grupos** e **Usuários** aparecerão apenas para o **Dono** da respectiva Review, Grupo ou Usuário.

## URL para Acessar o Site

**N/A**

## Passo a Passo para Utilizar as Funções do Site (Usuário Comum)

### Página Inicial

![Página Inicial](https://github.com/user-attachments/assets/79413d6b-12dd-4d9e-9985-ad9d44c24ef8)

Você será direcionado para a **Página Inicial**, onde encontrará as **notícias** da semana (clicáveis para visualizar mais informações). No canto superior, há opções para **Login** e **Cadastro**.

### Página de Cadastro e Login

![Página de Cadastro](https://github.com/user-attachments/assets/0d878d89-b70e-43ef-bfd0-1b6702884dc9)  
![Página de Login](https://github.com/user-attachments/assets/b888e797-4d4e-4aa5-b4d8-7b501180a377)

Você pode navegar entre as páginas de **Cadastro** e **Login** através dos redirecionamentos. Lembre-se de que as senhas devem ser diferentes do nome de usuário e ter um comprimento adequado, conforme as políticas do Django.

### Página de Filmes

![Página de Filmes](https://github.com/user-attachments/assets/f5621286-6c32-4773-8580-4465fdd5cad0)

Ao clicar em **Filmes** no cabeçalho, você chegará a esta página. Tanto logado quanto não logado, é possível visualizar os filmes cadastrados, ver a nota média baseada nas avaliações de todos os usuários e clicar em um filme para ver mais informações.

### Página de Informação do Filme

![Informação do Filme 1](https://github.com/user-attachments/assets/bd16edb7-2dd8-4fa8-ac09-62c8903bc47c)  
![Informação do Filme 2](https://github.com/user-attachments/assets/bdd30485-c908-4b9a-865d-0a27b833ee99)

Nesta página, você pode ver informações detalhadas do filme, como diretor, atores e escritores. É possível criar uma análise para o filme clicando no **"+"** e visualizar as análises feitas por outros usuários. Clicando em uma análise, você verá o conteúdo completo da mesma.

### Página de Informação das Reviews

![Informação das Reviews](https://github.com/user-attachments/assets/8555021b-ec30-4cdd-8b03-8685651aa619)

Aqui você pode ver as informações completas da review, além de ter a opção de visitar a página do usuário que a criou.

### Página do Usuário

![Página do Usuário](https://github.com/user-attachments/assets/a4e45cf4-a45f-4f2d-ba3d-10a821974434)

Existem duas maneiras de acessar a página do usuário:

1. Pelo cabeçalho (se estiver logado), clicando no seu nome de usuário.
2. Através de redirecionamentos ao clicar em **Reviews** ou **Membros**.

### Página de Séries

![Página de Séries](https://github.com/user-attachments/assets/a63ed33c-330a-43c7-9a28-3ec24a7c11ee)

Ao clicar em **Séries** no cabeçalho, você será direcionado a esta página. Tanto logado quanto não logado, é possível visualizar as séries cadastradas, ver a nota média baseada nas avaliações de todos os usuários e clicar em uma série para ver mais informações.

### Página de Informação da Série

![Informação da Série 1](https://github.com/user-attachments/assets/4f1b0dc2-6bd1-416d-a27c-0212ac3afd93)  
![Informação da Série 2](https://github.com/user-attachments/assets/9e0b4e9d-6d38-49bd-98ab-7a36d80b3d8d)

Nesta página, você pode ver informações detalhadas da série, como diretor, atores e escritores. É possível criar uma análise para a série clicando no **"+"** e visualizar as análises feitas por outros usuários. Clicando em uma análise, você verá o conteúdo completo da mesma.

### Página de Criação de Reviews

![Criação de Reviews](https://github.com/user-attachments/assets/e1c7599f-bd9d-4b32-8139-9affc54264c8)

Ao clicar no **"+"** em uma página de informação (Filme ou Série), você poderá criar uma **Review**. Preencha o formulário e clique em **Enviar**. **Observação:** A review não será exibida automaticamente no site, somente após aprovação de um administrador.

### Página de Grupos

![Página de Grupos](https://github.com/user-attachments/assets/f13fa022-8e08-431e-a455-f14129d59c32)

Ao clicar em **Grupos** no cabeçalho, você chegará a esta página. Tanto logado quanto não logado, é possível visualizar os grupos existentes. Apenas usuários logados terão a opção de criar novos grupos. Nesta página, você também verá a quantidade de membros de cada grupo e, ao clicar, poderá acessar as informações detalhadas do grupo.

### Página de Informação do Grupo

![Informação do Grupo](https://github.com/user-attachments/assets/f4d9ecc6-9077-47ef-a937-50551b8244e6)

Nesta página, você pode ver as informações do grupo, solicitar entrada e, se for o **Dono** do grupo, aceitar ou negar solicitações de novos membros.

#### Visão do Usuário Comum

![Visão do Usuário Comum](https://github.com/user-attachments/assets/060484ea-3cf2-4aa4-8830-6912b8382f2c)

O usuário comum pode ver quem é o dono do grupo, a quantidade de membros e pode solicitar para entrar no grupo.

#### Visão do Membro

![Visão do Membro](https://github.com/user-attachments/assets/b9882acc-0f84-4f50-8572-7669a640fa90)

Além das funcionalidades do usuário comum, o membro pode acessar uma rota "escondida" que mostra as avaliações de Filmes/Séries feitas pelos membros, ao invés de uma nota geral.

#### Visão do Dono do Grupo

![Visão do Dono do Grupo](https://github.com/user-attachments/assets/1df45c91-010f-4f62-a59a-f373a9a5e9f1)

O dono do grupo possui todas as permissões dos membros, além de poder:

- Atualizar informações do grupo.
- Deletar o grupo.
- Gerenciar a lista de membros (adicionar/remover).
- Ver e administrar solicitações de entrada de novos membros.

### Página de Administrar Membros

![Administrar Membros](https://github.com/user-attachments/assets/54362756-2086-4211-9d6c-1bc6fc0a0ae3)

Acessada somente pelo dono do grupo, esta página permite visualizar os membros atuais e remover usuários do grupo, se necessário.

### Página de Filmes (Grupos)

![Filmes dos Grupos](https://github.com/user-attachments/assets/1abf030a-78a0-45da-a802-9d5c0fadda1a)

Nesta rota específica para grupos, a nota exibida para um filme (por exemplo, **Interstellar**) será baseada apenas nas avaliações dos membros do grupo "Game/Movie Community". Isso permite que a média reflita a opinião dos membros do grupo. A página de informações funciona de forma semelhante à rota comum, mas com notas e reviews filtradas para os membros existentes.

### Página de Séries (Grupos)

Funciona de maneira similar à página de **Filmes (Grupos)**, mas focada nas séries.

### Página de Informação de Séries/Filmes (Grupos)

Semelhante às páginas de informação comuns, mas com notas e reviews filtradas para os membros do grupo.

## Funções do Site (Usuário Administrador)

![Funções do Administrador](https://github.com/user-attachments/assets/259160e2-e43d-4039-9a22-c28f4c4051d7)

Diferentemente das páginas acessadas por membros comuns, todas as páginas exibem um botão **"+"** para a criação de **Filmes**, **Séries** e **Notícias**. Além disso, administradores têm opções para **Atualizar** e **Deletar** cada um desses itens. No caso das **Notícias**, elas precisam ser aprovadas por um administrador superior antes de serem exibidas no site.

### Página de Consulta

![Página de Consulta](https://github.com/user-attachments/assets/67e03d82-74d5-4c24-ab63-58906ef75ecc)

O administrador, ao clicar no **"+"** na página de listagem de filmes ou séries, será direcionado para esta página. Aqui, é possível inserir o nome do **Filme** (se estiver na rota de filmes) ou o nome da **Série** (se estiver na rota de séries). O campo **Ano** é opcional e serve para filtrar melhor os resultados em caso de ambiguidades.

![Resultado da Consulta](https://github.com/user-attachments/assets/0ed665e8-7048-4927-991f-d6b41ae33af0)

Caso o resultado não seja o esperado, o administrador pode optar por criar o **Filme/Série** manualmente, preenchendo as informações necessárias nas páginas de criação correspondentes. Também é possível voltar para a página de busca ou confirmar a adição do item encontrado.

### Páginas de Criação

![Criação de Filme/Série](https://github.com/user-attachments/assets/a8a70c53-9d2b-45f2-88cf-52cca112c04b)  
![Criação de Grupo](https://github.com/user-attachments/assets/878ad649-9b71-4e9d-8940-9c2d3939bd17)

As páginas de criação seguem um padrão consistente para **Filmes**, **Séries** e **Grupos**, contendo formulários com campos específicos e um botão **Enviar** no final.

---




