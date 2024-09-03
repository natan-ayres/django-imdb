# django-imdb
Projeto em Django para um sistema de avaliação de Filmes e Séries, utilizando de mécanicas de Grupos.
# Versão de Desenvolvimento
1.0
# Observações
A Maioria das Imagens serão vistas pelo ponto de vista de um Administrador, os "+" para todas as páginas (menos Grupos), e o delete,update para Filmes, Séries, Notícias.

Já os Deletes, Updates para Reviews,Grupos,Usuário apenas aparecem para o Dono da Review,Grupo,Usuário.
# URL para Acessar o Site
N/A
# Passo a Passo para utilizar as funções do site(Usuário Comum)
# Página Inicial
![image](https://github.com/user-attachments/assets/79413d6b-12dd-4d9e-9985-ad9d44c24ef8)
Você vai se deparar com a página inicial, aonde tem as <b>notícias</b>(clicável para ver as informações) da semana e no canto superior vai ter a opção de <b>Login</b> e <b>Cadastro</b>.
# Página de Cadastro e Login
![image](https://github.com/user-attachments/assets/d96bc9a2-ea9b-4705-9e49-d673aedac81e)
![image](https://github.com/user-attachments/assets/b888e797-4d4e-4aa5-b4d8-7b501180a377)
Você pode navegar entre as duas páginas com os redirecionamentos, e <b>Cadastrar/Logar</b> o seu usuário, lembrando que as senhas que o Django permite não podem ser similares ao nome de usuário e tem que ter um comprimento decente.
# Página de Filmes
<img width="1402" alt="image" src="https://github.com/user-attachments/assets/f5621286-6c32-4773-8580-4465fdd5cad0">
Ao clicar em <b>Filmes</b> no cabeçalho você chegará nessa página, Logado ou não você pode visualizar os <b>Filmes</b> cadastrados no Site, ver a nota media deles(baseado em todos os usuários) e se clicar poderá ver as informações dos <b>Filmes</b>.
# Página de Informação do Filme
![image](https://github.com/user-attachments/assets/bd16edb7-2dd8-4fa8-ac09-62c8903bc47c)
![image](https://github.com/user-attachments/assets/bdd30485-c908-4b9a-865d-0a27b833ee99)
Você pode ver as informações do Filme, como diretor, atores, escritores... Você vai poder criar uma ánalise para o filme(se apertar no +) e também pode ver as ánalises dadas ao filme por outros usuários e se clicar você vai ver a ánalise por completo do usuário.
# Página de Informação da Reviews
<img width="1409" alt="image" src="https://github.com/user-attachments/assets/8555021b-ec30-4cdd-8b03-8685651aa619">
Você pode ver as informações e a ánalise por completo da Review, além de se quiser poderá ir para a página do usuário.
# Página do Usuário
<img width="1415" alt="image" src="https://github.com/user-attachments/assets/a4e45cf4-a45f-4f2d-ba3d-10a821974434">
Tem duas maneiras de chegar a página do usuário, uma delas é pelo cabeçalho (se estiver logado) você vai clicar no seu username e entrar na sua página, já as outras maneiras são redirecionamentos ao clicar em Reviews ou Membros.
# Página de Séries
<img width="1416" alt="image" src="https://github.com/user-attachments/assets/a63ed33c-330a-43c7-9a28-3ec24a7c11ee">
Ao clicar em <b>Series</b> no cabeçalho você chegará nessa página, Logado ou não você pode visualizar as <b>Séries</b> cadastradas no Site, ver a nota media delas(baseado em todos os usuários) e se clicar poderá ver as informações das <b>Séries</b>.
# Página de Informação da Série
<img width="1402" alt="image" src="https://github.com/user-attachments/assets/4f1b0dc2-6bd1-416d-a27c-0212ac3afd93">
<img width="1407" alt="image" src="https://github.com/user-attachments/assets/9e0b4e9d-6d38-49bd-98ab-7a36d80b3d8d">
Você pode ver as informações da Série, como diretor, atores, escritores... Você vai poder criar uma ánalise para a Série(se apertar no +) e também pode ver as ánalises dadas a Série por outros usuários e se clicar você vai ver a ánalise por completo do usuário.
# Página de Criação de Reviews 
<img width="1415" alt="image" src="https://github.com/user-attachments/assets/e1c7599f-bd9d-4b32-8139-9affc54264c8">
Ao Clicar on "+" em uma página de Informação, sendo ela de Filme ou Série, você vai criar uma <b>Review</b> para esse Filme/Série, sendo um formulário com um botão de enviar no final. Obs: A Review não é automaticamente mostrada no site, apenas se algum Administrador aceitar a Review.
# Página de Grupos
<img width="1409" alt="image" src="https://github.com/user-attachments/assets/f13fa022-8e08-431e-a455-f14129d59c32">
Ao clicar em <b>Grupos</b> no cabeçalho você chegará nessa página, Logado ou não você poderá visualizar os <b>Grupos</b> criados no Site, porém apenas logado terá a opção de criar <b>Grupos</b>! Nessa página você também verá a quantidade de membros que cada <b>Grupo</b> tem e ao clicar, você entrará nas informações dos <b>Grupos</b>.
# Página de Informação do Grupo
![image](https://github.com/user-attachments/assets/f4d9ecc6-9077-47ef-a937-50551b8244e6)
A página de Informação do <b>Grupo</b> além de ver as informações do <b>Grupo</b> serve para usuários entrarem e o Dono do grupo aceitar ou negar a entrada.
# Visão do Usuário Comum
![image](https://github.com/user-attachments/assets/060484ea-3cf2-4aa4-8830-6912b8382f2c)
O Usuário Comum pode ver quem é o Dono, a quantidade de membros que o Grupo tem e também pode pedir pra entrar no grupo.
# Visão do Membro
<img width="1411" alt="image" src="https://github.com/user-attachments/assets/b9882acc-0f84-4f50-8572-7669a640fa90">
O Usuário Membro pode ver tudo que o usuário comum, porém ele pode ver uma rota "escondida", que é mostrando os Filmes/Séries que foram avaliados pelos Membros invês de uma nota geral.
# Visão do Dono do Grupo
![image](https://github.com/user-attachments/assets/1df45c91-010f-4f62-a59a-f373a9a5e9f1)
O Dono do Grupo consegue ver tudo que o usuário comum e o membro vêem porém com permissões a mais, podendo atualizar informações do grupo, deletar o grupo, ver a lista de membros(e poder administrar eles), ver a lista de usuários que querem entrar.
# Página de Administrar Membros
![image](https://github.com/user-attachments/assets/54362756-2086-4211-9d6c-1bc6fc0a0ae3)
Nessa página apenas acessada pelo Dono do Grupo, ele terá acesso a quem está no grupo e poder remover esse usuário.
# Página de Filmes(Grupos)
<img width="1405" alt="image" src="https://github.com/user-attachments/assets/1abf030a-78a0-45da-a802-9d5c0fadda1a">
Supondo que na rota comum de Filmes, a nota que apareça pra Interstellar seja 10! Porém os membros do Grupo "Game/Movie Community", achem que é um Filme ruim, e nessa rota é apenas a nota dos membros que importa! Mostrando a média buscando os membros existentes, ela também possui uma página de informação igual a rota comum, porém com a nota e reviews filtradas para os membros existentes.
# Página de Séries(Grupos)
Ela funciona igual a página de Filmes(Grupos) porém mostrando apenas as séries.
# Página de Informação de Séries/Filmes(Grupos)
Ela funciona igual as de informação porém com notas e reviews filtradas.


# Funções do site(Usuário Administrador)
![image](https://github.com/user-attachments/assets/259160e2-e43d-4039-9a22-c28f4c4051d7)
Diferentemente da página dos Membros Comuns, todas as páginas vão ter um "+" para criação de Filmes/Séries/Notícias, além da opção de Atualizar e Deletar cada um desses três, No caso das Notícias elas teram que ser aprovadas por um Administrador superior.
# Página de Consulta
![image](https://github.com/user-attachments/assets/67e03d82-74d5-4c24-ab63-58906ef75ecc)
O Usuário Administrador ao clicar no + na página de listagem de filmes ou na página de listagem de séries, virá para essa página, podendo colocar o nome do Filme(se clicou no + na página de filmes) ou o nome da Série(se clicou no + na página de séries), e o Ano é opcional, servindo para filtrar ainda melhor caso a Consulta tenha falhas, após colocar e clicar em Buscar, vai ser mostrado o botão de Confirmar e as informações do Filme/Série buscada.
![image](https://github.com/user-attachments/assets/0ed665e8-7048-4927-991f-d6b41ae33af0)
Caso não seja o que você esperava, você pode criar o Filme/Série manualmente, colocando as informações que precisa em uma das páginas de Criação, já caso queira voltar para a página de Busca, clique em Voltar, caso queira confirmar, aperte em Confirmar.
# Páginas de Criação
![image](https://github.com/user-attachments/assets/a8a70c53-9d2b-45f2-88cf-52cca112c04b)
![image](https://github.com/user-attachments/assets/878ad649-9b71-4e9d-8940-9c2d3939bd17)
As Páginas de Criação seguem um padrão para Filmes, Séries e Grupos, sendo os campos de um formulário e no final um botão de Enviar.




