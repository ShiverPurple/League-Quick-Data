<p align=”center”>
<a href=https://www.linkedin.com/in/wandersongasco/>
<img src=https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin&labelColor=blue>
</a>
<a href=https://github.com/WandersonKnight/League-Quick-Data/blob/main/README.en.md/>
<img src=https://img.shields.io/badge/lang-eng-red>
</a>
</a>
<a href=https://github.com/WandersonKnight/League-Quick-Data/blob/main/README.md/>
<img src=https://img.shields.io/badge/lang-pt--br-success>
</a>
</p>

# League Quick Data

## O que o programa faz

O programa retorna o resumo dos dados das últimas 10 partidas de até 5 jogadores simultâneamente, juntamente à um resumo do perfil do jogador, como rank, taxa de vitória e kda dos campeões jogados recentemente.

Para que o tempo de busca seja o menor possível, a aplicação baixará continuamente, a cada busca, ícones e imagens diretamente da API Datadragon da RIOT para o PC.

### Elementos retornados pelo programa

Resumo do perfil:

* Nome do jogador
* Rank do jogador
* Taxa de vitória das últimas 10 partidas
* KDA médio das últimas 10 partidas
* Campeões mais jogados recentemente
* Taxa de vítoria dos campeões mais jogados recentemente
* KDA médio dos campeões mais jogados recentementes

Resumo da partida:

* Campeão jogado
* Modo de jogo
* Spells
* Level
* Items comprados
* KDA
* Total de gold recebido
* Mapa
* Tempo de jogo
* Data do jogo


## Funcionamento

### GUI

A interface de usuário do programa consiste em uma combinação entre a biblioteca de interface padrão de Python, chamada 'Tkinter', elementos visuais elaborados individualmente - como bordas e ícones - e arquivos de imagem retirados da API Datadragon da RIOT.

#### Antes da pesquisa

<img src="https://user-images.githubusercontent.com/39245594/147681869-c59ad6be-af8b-4488-a0de-de9c3dd6fcfa.png" alt="Janela padrão" width="600"/>

#### Depois da pesquisa

<img src="https://user-images.githubusercontent.com/39245594/147681961-d7c06b38-addf-4c80-a9b2-a74a59aa5854.png" alt="Janela com as informações" width="600"/>

### Interação com API externa

Por meio da biblioteca 'requests' são feitas chamadas para receber dados temporários, como nome, kda e Id de determinados objetos e downloads de objetos reutilizáveis, como ícones de spells, campeões e itens.

Para ter acesso à determinadas funções da API é utilizada uma chave pessoal providenciada pela RIOT com requests limitados, sendo então removidas suas limitações apenas após registro formal da aplicação pela empresa em sua plataforma de suporte à desenvolvedores.


# Observações

Quaisquer alterações feitas pela RIOT após 08/11/21 estarão fora do escopo deste programa.

É necessária a chave fornecida em sua Conta de Desenvolvedor da Riot. Chave não comercial fará apenas um máximo de 3 buscas simultâneas devido o limite de chamadas imposto pela própria Riot.
