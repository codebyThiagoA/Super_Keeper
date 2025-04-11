
# Super Keeper - Jogo 2D em Python com Pygame

## Membros da Equipe:
- Davi Peixoto Freire Falcao
- Pedro Francisco da Costa Cavalcanti
- Hugo Kauan Leal Crasto
- Felipe Costa Coutinho
- Thiago Bernardo de Paula Alves
- Arthur de Sá Tenório



## Descrição do Jogo
Super Keeper é um jogo 2D feito em Python usando a biblioteca Pygame. A missão aqui é simples (pelo menos na teoria): você controla um goleiro que precisa defender o gol de uma chuva de bolas. E não são bolas qualquer, não — tem a bola normal, a bola da Argentina e a bola da Alemanha, também conhecidas como bola1, bola2 e bola3. Se alguma delas passar direto pelo goleiro sem ser pega, você perde vida. Pra defender, é só encostar nelas — se a bola bater no goleiro, tá valendo!




## Capturas de Tela
### Tela inicial do jogo
![Tela de inicio](https://github.com/codebyThiagoA/Super_Keeper/blob/Merge-/designs/Demonstra%C3%A7%C3%A3o_tela_inicial.png?raw=true)

### Jogabilidade
![Jogo](https://github.com/codebyThiagoA/Super_Keeper/blob/Merge-/designs/Demonstra%C3%A7%C3%A3o_tela_de_jogo.png?raw=true)

### Tela final do jogo
![Tela Final](https://github.com/codebyThiagoA/Super_Keeper/blob/Merge-/designs/Demonstra%C3%A7%C3%A3o_tela_gameover.png?raw=true)





## Estrutura do Projeto:


- main.py: É o arquivo principal, responsável por importar a função principal e executar a inicialização do jogo.
- objtetos.py: Este parte do projeto engloba os botões de jogar, sair, reiniciar e o de Game Over, onde é especificado as disposição dos objetos na tela.
- designs.py: Módulo responsável por comportar todas as imagens utilizadas no fundo, tela inicial, tela de Game Over, contadores e objetos do jogo. Além disso, comporta a função carregar_imagem, principal função para o desenvolvimento da parte gráfica do jogo.
- configs.py: Representa a disposição dos objetos e contadores na tela, também como o tamanho da tela e das fontes.
- audio.py: Parte responsável por comportar tudo que envolve a parte sonora do projeto e suas funções.
- designs: Diretório que armazena tudo envolvendo parte gráfica.
- codigo: É o diretório responsável pela parte "bruta" do projeto. Basicamente, nele está concentrado o funcionamento de todas as funções, classes, contadores e objetos criados. Ele reúne, por exemplo, a classe BolaBase, responsável pelo spawn e velocidade das bolas; a classe Goalkeeper, que gerencia a movimentação do goleiro e as colisões; a classe RecuperarCoracao, além de outras funções importantes, como tela_intermediaria, tela_gameover, tela_jogo e tela_inicial.
- audio: Diretório responsável por armazenar todos os áudios utilizados no projeto.




## Ferramentas utilizadas:

### Bibliotecas:

A biblioteca Pygame foi a principal aliada no desenvolvimento da parte gráfica e da dinâmica do jogo. Com ela, foi possível iniciar a interface de exibição, permitindo mostrar elementos como o fundo, sprites e botões na tela. Além disso, ela também cuida das interações do jogador, como detectar quando uma tecla é pressionada ou quando o jogador fecha a janela do jogo. Outro ponto importante é que o Pygame gerencia o tempo do jogo com um relógio interno, que ajuda a manter a taxa de atualização estável — garantindo que tudo rode na velocidade certa.

O uso do Pygame faz todo sentido nesse projeto porque ele oferece um conjunto completo de ferramentas essenciais para criar jogos de forma simples e eficiente. Como o projeto é gráfico e interativo, era fundamental ter uma biblioteca que lidasse bem com imagens, sons e controles do jogador. Por ser uma das bibliotecas mais conhecidas e usadas em Python para esse tipo de tarefa, o Pygame acabou sendo a escolha perfeita — ele é, literalmente, a base que sustenta todo o jogo.


A biblioteca 'time' é uma biblioteca padrão em Python que fornece funções relacionadas ao tempo. Aqui, a função time é necessária para a utilização do crônometro que mede o tempo de sobrevivência do jogador.

A biblioteca 'random' também foi importada para o projeto, pois se mostrou extremamente eficiente no spawn de objetos e ajudou a tornar o jogo mais desafiador ao longo do tempo de partida.


### Ferramentas:
Aplicativos e Sites:
Entre as ferramentas utilizadas para o desenvolvimento do projeto, estão: VSCode, Discord, Notion, Libresprite, Canva, The Mushroom Kingdom, TunePocket, YouTube e GitHub. O VSCode, em conjunto com o GitHub, foi utilizado para todo o desenvolvimento do código do jogo, por meio da criação de um repositório ao qual todos os membros da equipe tinham acesso para atualizar o código.

Para o planejamento e acompanhamento do progresso do projeto, foi utilizado um canal no Discord para realizar as reuniões remotas, e o Notion para estruturar o planejamento inicial da base do jogo.

A arte do Super Keeper foi criada por meio do Canva e do Libresprite, plataformas que permitem a criação de pixel art no desenvolvimento das imagens.
No âmbito sonoro, os efeitos foram obtidos a partir de diferentes fontes: o som de defesa, de ganhar vida e de perda de vida foram retirados do The Mushroom Kingdom; o som de derrota e o som ambiente de estádio vieram do TunePocket; e o som da tela inicial foi obtido através do YouTube.





## Conceitos aprendidos durante a disciplina utilizados no jogo

- laços de repetição: Os laços de repetição foram um recurso essencial na construção do projeto de software interativo. Eles foram especialmente úteis para automatizar tarefas repetitivas, como a criação de animações e a definição das coordenadas dos elementos coletáveis. Com o uso dos loops while e for, conseguimos desenvolver estruturas mais enxutas e eficientes.
- Funções: As funções foram fundamentais para a organização e eficiência do nosso projeto em Pygame. Elas nos permitiram dividir o código em blocos reutilizáveis, facilitando tanto a leitura quanto a manutenção do programa. Com funções bem definidas, conseguimos isolar comportamentos específicos, como a exibição de telas, verificação de colisões ou atualização da pontuação, evitando repetições desnecessárias e deixando o código mais limpo . Essa estrutura tornou o desenvolvimento mais ágil e colaborativo, permitindo que cada membro da equipe contribuísse em partes distintas do projeto com mais facilidade.
- Dicionário: O uso de dicionários foi uma ferramenta extremamente útil para organizar e exibir os elementos visuais do nosso projeto em Pygame. Um exemplo disso é a estrutura elementos, onde cada dicionário armazena informações específicas sobre um item da interface, como o texto a ser exibido, a fonte utilizada, a posição na tela e a cor. Essa abordagem nos permitiu centralizar os dados de forma clara e acessível, facilitando tanto a renderização dos elementos quanto a manutenção do código. Além disso, ao trabalhar com listas de dicionários, conseguimos iterar sobre todos os elementos de forma dinâmica e eficiente, sem a necessidade de repetir blocos de código para cada item.
- Classes: O uso de classes foi essencial para estruturar nosso projeto de forma organizada e eficiente. Com elas, conseguimos representar os elementos do jogo como o goleiro, as bolas e a recuperação de corações de maneira clara. Cada classe agrupava dados e comportamentos específicos, facilitando tanto a reutilização quanto a manutenção do código. Além disso, a utilização de classes tornou o desenvolvimento mais intuitivo, permitindo que cada parte do jogo tivesse uma lógica bem definida e separada das demais, o que foi fundamental para o bom funcionamento e evolução do projeto.
- Orientação a Objetos: A programação orientada a objetos foi um dos conceitos mais presentes ao longo de todo o desenvolvimento do projeto. Como qualquer jogo depende da criação e manipulação de objetos na tela, essa abordagem se mostrou a forma mais prática e intuitiva de estruturar o código, permitindo representar elementos como goleiro, tipos de bolas e item de cura.
- Importar módulos: A importação de módulos foi essencial para manter nosso projeto organizado e funcional. Ao dividir o código em partes específicas e reutilizáveis, conseguimos trabalhar de forma mais clara e eficiente, além de facilitar a colaboração entre os membros da equipe.













## Divisão de Trabalhos:
As decisões relacionadas à dinâmica do jogo, como a escolha do tema, da interface, da lógica, das regras, ideias, funcionalidades, personagens, entre outros elementos, foram tomadas de forma conjunta, com a participação ativa de todos os membros da equipe. Cada integrante pôde opinar, votar e teve suas ideias consideradas ao longo de todo o processo de idealização e criação do projeto.

Detalhes técnicos:

- Davi Peixoto Freire Falcao:
    Desenvolver a interface gráfica do jogo;
    Criou o design da tela inicial;
    Criou o design dos botões;
    Criou o design da tela Game Over;
    Auxiliou nas correções do código.

- Pedro Francisco da Costa Cavalcanti:
    Coordenar as decisões gerais;
    Participar e gerenciar o código de todos integrantes;
    Criação do Notion;
    Responsável pelo relatório;
    Correções de código.

- Hugo Kauan Leal Crasto:
    Ajustes do Recursos;
    Monitoramento do projeto;
    Otimização do código sobre as colisões;
    Revisão e otimização de algumas funções;
    Comunicação do projeto.
    

- Felipe Costa Coutinho:
    Criar as classes dos objetos;
    Implementar a lógica de queda dos objetos;
    Implementar a lógica de coleta dos objetos;
    Desenvolver os contadores de coleta;
    Criar a lógica de gerenciamento de vidas.

- Thiago Bernardo de Paula Alves:
    Desenvolver a classe do goleiro;
    Desenvolver as movimentações;
    Aplicar as animações básicas;
    Auxilio no design da tela do jogo;
    fez a arte do fundo do jogo.

- Arthur de Sá Tenório:
    Implementou o efeito sonoro de coleta;
    Implementou o efeito sonoro de perda de vida;
    Aplicou a trilha sonora de fundo;
    Auxiliou no design das bolas;
    Implemtou o efeito sonoro de Game Over.


## Controles
Pressione a tecla <- para que o goleiro se desloque para esquerda
Pressione a tecla -> para que o goleiro se desloque para direita

## Regras do Jogo:
- O jogador inicia a partida com uma quantidade definida de vidas;
- A partida se estende até que todas as vidas sejam esgotadas;
- Pontos são acumulados ao conseguir bloquear as bolas antes que elas avancem sem defesa;
- Os diferentes tipos de bola são registrados individualmente em contadores próprios;
- Sempre que uma bola passa sem ser defendida, o jogador perde vida;
- O desafio é somar o maior número de pontos possível antes de ficar sem vidas.





## Desafios:
Na maior parte do tempo, tivemos dificuldade em reunir o que cada integrante havia feito e integrar tudo para que o código começasse a funcionar. Além disso, a organização também foi, de certa forma, um desafio no projeto, já que, conforme cada pessoa ia desenvolvendo sua parte, surgiram divergências sobre como o código deveria funcionar.

Entre as problemáticas enfrentadas, um dos desafios mais frequentes foi o constante choque entre as diferentes formas que os integrantes usavam para implementar as funções do jogo. Por conta disso, o código precisou passar por manutenções constantes para que tudo se encaixasse em um padrão.





Este projeto foi realizado para disciplina de Introdução à Programação no CIn UFPE

# No Super Keeper, cada defesa é uma vitória e cada segundo conta para se tornar uma lenda do gol!!!!




