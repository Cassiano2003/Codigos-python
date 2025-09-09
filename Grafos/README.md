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
Ira conter funçoes mais genericas que a biblioteca **Busca** vai usar, nessa biblioteca ira conter:
* desenha
* Cor_Caminho
* Cria_Grafo
* Gera_arestas
* Gera_Dicionarios
Essas funlções vão ser bem intuitivas, para facilitar o entendimento e a posivel modificação.

### Busca
Essa biblioteca vai conter arquivos separados de cada tipo de busca. Futuramente ira conter mais tipos de buscas e tambem ira conter caminhos minimos e arvore geradora minima.
* BFS(Busca em Largura)
* DFS(Busca em Profundidade)

### Main
É um arquivo que deve ser esecutado pelo comando **python3 main.py**, pois ele age como um menu que vai ter opções para poder decidir qual sera o tipo da manipulação.(OBS: Tentarei deixar o mais modificavel posivel)


## Criador
* **Cassiano Carvalho de Souza.**