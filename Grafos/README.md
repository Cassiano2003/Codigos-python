# Area de Grafos
Bom como visto lá no começo, aqui ira conter codigos para criação e manipulação de grafos.

## Requisitos
Para poder compilar esses codigos e necesatio ter algumas bibliotecas, como:
* matplotlib.pyplot
* networkx
* random

## Modificaçoes
Caso queira modificar alguma coisa, sera necesario mecher nas bibliotecas proprias desse projeto.\
Para poder colocar mais arquivos nas bibliotecas do projeto é bem simples é só colocar eles na onde você quer, e depois use o comando **pip install .** para compilar a nova biblioteca e assim podera chamar a nova função do mesmo jeito que as outras.

### Biblioteca Geral
Ira conter funçoes mais genericas que a biblioteca **Busca** e **Caminos Minimos** vai usar, nessa biblioteca ira conter:
* desenha
* Cor_Caminho
* Cria_Grafo
* Gera_arestas
* Gera_Dicionarios
Essas funlções vão ser bem intuitivas, para facilitar o entendimento e a posivel modificação.

### Busca
Essa biblioteca vai conter arquivos separados de cada tipo de busca.
* BFS(Busca em Largura)
* DFS(Busca em Profundidade)

### Caminhos Minimos
Essa biblioteca esta implementando a busca de caminhos minimos com o foco em dois algoritomos.
* Bellman Ford
* Dijkstra

### Main
É um arquivo que deve ser esecutado pelo comando **python3 main.py**, pois ele age como um menu que vai ter opções para poder decidir qual sera o tipo da manipulação.(OBS: Tentarei deixar o mais modificavel posivel)


## Criador
OBS: Estou criando esse repositorio, pois queria ver os algoritimos funcionado e queria algo mais maleavel e que eu pudese fazer experimentos a vontade tendo o maximo de liberdade.
* **Cassiano Carvalho de Souza.**