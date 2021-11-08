# League Quick Data

## O que o programa faz

O programa retorna o resumo dos dados das últimas 10 partidas de até 5 jogadores simultâneamente, juntamente à um resumo do perfil do jogador, como rank, taxa de vitória e kda dos campeões jogados recentemente.

Para que o tempo de busca seja o menor possível, a aplicação baixará continuamente a cada busca ícones e imagens diretamente da API Datadragon da RIOT para o PC em que esteja instalada.

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

### Interação com API externa

Por meio da biblioteca 'requests' são feitas chamadas para receber dados temporários, como nome, kda e Id de determinados objetos e downloads de objetos reutilizáveis, como ícones de spells, campeões e itens.

Para ter acesso à determinadas funções da API é utilizada uma chave pessoal providenciada pela RIOT com requests limitados, sendo então removidas suas limitações apenas após registro formal da aplicação pela empresa em sua plataforma de suporte à desenvolvedores.

### Tempo de busca e build

Para que a execução do programa seja a mais rápida possível são utilizados artifícios como multithreading com limite de 10 threads e armazenamento de dados frequentemente buscados.

## Filosofia de programação

No decorrer do desenvolvimento do programa e de sua refatoração segui alguns princípios, entre eles:

### Simples é melhor do que complicado, podendo ainda sim ser complexo

Prezo pela simplicidade do código para que seja de fácil entendimento ao primeiro olhar, independente do grau de instrução do programador.
Fazer algo complexo parecer simples é mais difícil que fazer algo trivial parecer complicado.

### Essencial é apenas o necessário para o programa funcionar, sendo esse o mínimo possível

Sem que comprometa seu funcionamento, prezo pelo menor código e pelo mínimo de syntax possível no desenvolvimento do programa. Se alguma solução já existe, provavelmente existe uma maneira mais simples e menor de realizá-la.

### Clareza acima de simplicidade, simplicidade acima de 'super-eficiência'

Clareza na estrutura do código, no nome de cada função, de cada várial e classe é mais importante do que a miniaturização do código pois miaturização excessiva pode ofuscar a funcionalidade de determinado elemento. Simplicidade, porém, é mais importante que elaboração de syntax complexas com o intuito de ganhar milésimos em tempo de execução.

### Eficiência e velocidade para apresentar uma experiência satisfatória, não para benchmarks

Para programas com funcionalidade simples, eficiência e velocidade de execução são importantes apenas até onde a percepção humana chega.

### Clareza na estrutura do código remove anotações desnecessárias

Quanto mais clara e limpa é a estrutura de um código e mais nítido são as funções de cada elemento seu, menos anotações são necessárias para seu entendimento. Falar por código é mais díficil do que por palavras, porém mais eficiente.
