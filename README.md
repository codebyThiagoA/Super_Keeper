
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
![Tela de inicio](https://github.com/codebyThiagoA/Super_Keeper/blob/Merge-/designs/Tela_inicial.png?raw=true)

### Jogabilidade
![Jogo](https://github.com/julianatalita/projetoIP/assets/136331050/1d3c6e4f-0ccb-46a3-9f5d-509af66a25e2)

### Tela final do jogo
![Tela Final](https://github.com/julianatalita/projetoIP/assets/136331050/00f035f2-3aba-44fb-8ab1-9fc5562123dd)





## Estrutura do Projeto:


- 
- 
- 
- 
- 
- 
- 
- 
- 
- 


## Ferramentas utilizadas:

### Bibliotecas:

A biblioteca Pygame foi a principal aliada no desenvolvimento da parte gráfica e da dinâmica do jogo. Com ela, foi possível iniciar a interface de exibição, permitindo mostrar elementos como o fundo, sprites e botões na tela. Além disso, ela também cuida das interações do jogador, como detectar quando uma tecla é pressionada ou quando o jogador fecha a janela do jogo. Outro ponto importante é que o Pygame gerencia o tempo do jogo com um relógio interno, que ajuda a manter a taxa de atualização estável — garantindo que tudo rode na velocidade certa.

O uso do Pygame faz todo sentido nesse projeto porque ele oferece um conjunto completo de ferramentas essenciais para criar jogos de forma simples e eficiente. Como o projeto é gráfico e interativo, era fundamental ter uma biblioteca que lidasse bem com imagens, sons e controles do jogador. Por ser uma das bibliotecas mais conhecidas e usadas em Python para esse tipo de tarefa, o Pygame acabou sendo a escolha perfeita — ele é, literalmente, a base que sustenta todo o jogo.


A biblioteca 'time' é uma biblioteca padrão em Python que fornece funções relacionadas ao tempo. Aqui, a função time é necessária para a utilização do crônometro que mede o tempo de sobrevivência do jogador.


### Ferramentas:
Aplicativos e Sites:
Entre as ferramentas utilizadas para o desenvolvimento do projeto, estão: VSCode, Discord, Notion, Libresprite, Canva, The Mushroom Kingdom, TunePocket, YouTube e GitHub. O VSCode, em conjunto com o GitHub, foi utilizado para todo o desenvolvimento do código do jogo, por meio da criação de um repositório ao qual todos os membros da equipe tinham acesso para atualizar o código.

Para o planejamento e acompanhamento do progresso do projeto, foi utilizado um canal no Discord para realizar as reuniões remotas, e o Notion para estruturar o planejamento inicial da base do jogo.

A arte do Super Keeper foi criada por meio do Canva e do Libresprite, plataformas que permitem a criação de pixel art no desenvolvimento das imagens.
No âmbito sonoro, os efeitos foram obtidos a partir de diferentes fontes: o som de defesa, de ganhar vida e de perda de vida foram retirados do The Mushroom Kingdom; o som de derrota e o som ambiente de estádio vieram do TunePocket; e o som da tela inicial foi obtido através do YouTube.





## Conceitos aprendidos durante a disciplina utilizados no jogo
















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


## Como Jogar:
- Execute o arquivo main.py.
- Use as teclas <- e -> para movimentação.
- Colete o máximo de bolas possível para ganhar pontos e evitar a perda de vidas.


## Desafios:
    Na maior parte do tempo, tivemos dificuldade em reunir o que cada integrante havia feito e integrar tudo para que o código começasse a funcionar. Além disso, a organização também foi, de certa forma, um desafio no projeto, já que, conforme cada pessoa ia desenvolvendo sua parte, surgiram divergências sobre como o código deveria funcionar.

    Entre as problemáticas enfrentadas, um dos desafios mais frequentes foi o constante choque entre as diferentes formas que os integrantes usavam para implementar as funções do jogo. Por conta disso, o código precisou passar por manutenções constantes para que tudo se encaixasse em um padrão.


## Requisitos:
- Python 3.x
- Pygame (você pode instalá-lo com 'pip install pygame')


Este projeto foi realizado para disciplina de Introdução à Programação no CIn UFPE

### No Super Keeper, cada defesa é uma vitória e cada segundo conta para se tornar uma lenda do gol.



