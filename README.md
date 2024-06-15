# Boas-vindas ao repositório do TING (Trybe is not Google)!

<details>
  <summary><strong>👨‍💻 O que deverá ser desenvolvido</strong></summary><br />


Neste projeto você deverá implementar um programa que simule um algoritmo de indexação de documentos similar ao do Google. Seu programa deverá ser capaz de identificar ocorrências de termos em arquivos _TXT_.
  
Para isso, o programa desenvolvido por você deverá ter dois módulos:
- **Módulo de gerenciamento de arquivos** que permite anexar arquivos de texto (formato _TXT_) e;
- **Módulo de buscas** que permite operar funções de busca sobre os arquivos anexados.

:eyes: **Neste projeto não iremos focar na análise de significados ou busca por sinônimos.**


🚵 Habilidades exercitadas:

 - Manipular Pilhas;

 - Manipular Deque;

 - Manipular Nó & Listas Ligadas e;

 - Manipular Listas Duplamente Ligadas.

</details>

# Orientações
<details>
  <summary><strong>⚠ Antes de começar a desenvolver</strong></summary><br />

  1. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`

  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`
</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado ambiente virtual que permite sua máquina rodar, sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas. Para utilizar este recurso siga os passos a seguir:

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo as dependências serão instaladas neste ambiente.
  
  :eyes: Caso precise desativar o ambiente virtual execute o comando _"deactivate"_.
  
  :warning: Lembre-se de ativar o ambiente virtual novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

# Requisitos Obrigatórios

## Pacote `ting_file_management`

### 1 - Implemente uma fila para armazenar os arquivos que serão lidos.

- Preencha a classe `Queue`, presente no arquivo `queue.py` utilizando as estruturas vistas no módulo.

- A fila (Queue) deve ser uma estrutura `FIFO`, ou seja, o primeiro item a entrar, deve ser o primeiro a sair. Utilize seus conhecimentos de estruturas de dados para otimizar as operações implementadas.

- A fila deve implementar os métodos de inserção (`enqueue`), remoção (`dequeue`) e busca (`search`).

- O tamanho da fila deverá ser exposto utilizando o método `__len__` que permitirá, após implementado, o uso do comando `len(instancia_da_fila)` para se obter o tamanho da fila.

- Na busca uma exceção do tipo `IndexError` com a seguinte mensagem: `"Índice Inválido ou Inexistente"` deve ser lançada caso um índice inválido seja passado. Para uma fila com `N` elementos, índices válidos são inteiros entre `0` e `N-1`.

### 2 - Implemente uma função `txt_importer` dentro do módulo `file_management` capaz de importar notícias a partir de um arquivo TXT, utilizando "\n" como separador.

- Caso o arquivo TXT não exista, deve ser exibida a mensagem `Arquivo {path_file} não encontrado` na `stderr`, em que `{path_file}` é o caminho do arquivo;

- Caso a extensão do arquivo seja diferente de .txt, deve ser exibida a mensagem `Formato inválido` na `stderr`;

- A função deve retornar uma lista contendo as linhas do arquivo.

### 3 - Implemente a função `process` no módulo `file_process`. Essa função deverá ser capaz de transformar o conteúdo da lista gerada pela função `txt_importer` em um dicionário que será armazenado dentro da `Queue`.

- A função irá receber como parâmetro um objeto instanciado da fila implementada no requisito 1 e o caminho para um arquivo;

- A instância da fila recebida por parâmetro **deve** ser utilizada para registrar o processamento dos arquivos;

- A função deve processar o arquivo passado por parâmetro (ou seja, gerar um dicionário com o formato e informações especificadas abaixo);

- Deve-se ignorar arquivos que já tenham sido processados anteriormente (ou seja, arquivos com o mesmo nome e caminho (`nome_do_arquivo`) não devem ser readicionados a fila);

- Após cada nova inserção válida, a função deve mostrar via `stdout` os dados processados, conforme estrutura no exemplo abaixo.

### 4 - Implemente uma função `remove` dentro do módulo `file_process` capaz de remover o primeiro arquivo processado

- A função irá receber como parâmetro a fila implementada no requisito 1.

- Caso não existam arquivos na fila, a função deve apenas emitir a mensagem `Não há elementos` via `stdout`;

- Em caso de sucesso de remoção, deve ser emitida a mensagem `Arquivo {path_file} removido com sucesso` via `stdout`, em que `{path_file}` é o caminho do arquivo.

### 5 - Implemente uma função `file_metadata` dentro do módulo `file_process` capaz de apresentar as informações superficiais de um arquivo processado.


- A função irá receber como parâmetro a fila implementada no requisito 1 e o índice a ser buscado;

- Caso a posição não exista, deve ser exibida a mensagem de erro `Posição inválida` via `stderr`;

- Caso a posição seja válida, as informações relacionadas ao arquivo devem ser mostradas via `stdout`, seguindo o exemplo de estrutura abaixo.

### 6 - Implemente os testes para a classe `PriorityQueue` capaz de armazenar arquivos pequenos de forma prioritária

> Implemente em: tests/priority_queue/test_priority_queue.py

A classe `PriorityQueue` utiliza a implementação da classe `Queue` do requisito `1` para armazenar arquivos pequenos com prioridade. Utilizando a classe `PriorityQueue`, arquivos com menos de 5 linhas são armazenados de forma prioritária na fila, o que impacta no resultado dos métodos `dequeue` e `search`.

Você deve implementar testes para a classe `PriorityQueue`, garantindo que a lógica de prioridades é respeitada pelos métodos `enqueue`, `dequeue` e `search`.

<details>
  <summary>
    <b>🧠 Entenda a lógica da fila de prioridades</b>
  </summary>

Quando um arquivo prioritário (_com menos de 5 linhas_) é adicionado à fila de prioridades, este arquivo ficará "após" todos os arquivos prioritários já inseridos, mas ficará "antes" de todos os arquivos não-prioritários já inseridos.

Quando um arquivo não-prioritário (_com 5 linhas ou mais_) é adicionado à fila de prioridades, este arquivo ficará "após" todos os arquivos já inseridos.

Exemplo:

```python
# Tamanhos dos arquivos, em ordem de inserção na fila: 
[9, 4, 2, 5, 7, 11, 3]

# Tamanhos dos arquivos, em ordem de remoção da fila:
[4, 2, 3, 9, 5, 7, 11]
```

</details>

## Pacote `ting_word_searches`

### 7 - Implemente uma função `exists_word`, dentro do módulo `word_search`, que verifique a existência de uma palavra em todos os arquivos processados.

- A função irá receber como parâmetros a palavra a ser buscada e a fila implementada no requisito 1;

- A função deve retornar uma lista com as informações de cada arquivo e suas linhas em que a palavra foi encontrada, conforme exemplo da estrutura de retorno;

- A busca deve ser _case insensitive_ (não diferenciar maiúsculas e minúsculas);

- Caso a palavra não seja encontrada em nenhum arquivo, deve-se retornar uma lista vazia;

- A fila não deve ser modificada durante a busca. Ela deve permanecer com os mesmos arquivos processados antes e depois da busca.

### 8 - Implemente uma função `search_by_word` dentro do módulo `word_search`, que busque uma palavra em todos os arquivos processados.

- Esta função deverá seguir os mesmos critérios do requisito sete, mas deverá incluir na saída o conteúdo das linhas encontradas, conforme exemplo da estrutura de retorno.

:eyes: **De olho na dica:** este requisito é uma ótima oportunidade para reforçar a prática de código limpo!
