## Lista 6 - Dividir para Conquistar
### Sistema Ordenador de Registros e Contador de Inversões

##### Alunos

| Matrícula | Nome | GitHub |
|--|--|--|
| 15/0029624 | Allan Jefrey Pereira Nobre | @AllanNobre |
| 15/0059213 | Filipe Coelho Hilário Barcelos | @FilipeKN4 |

##### Para executar
O ambiente deve ser configurado para a utilização do framework Django na versão 2.1. Após a configuração, deve-se executar o comando abaixo: 

```sh
$ python3 manage.py runserver
```

Após a execução abra o link do servidor em http://127.0.0.1:8000/.

##### Descrição

Escolhe-se qual algoritmo deseja-se e executar entre Divide and Conquer - Counting Inversions e Divide and Conquer - Merge Sort.
Lê-se um arquivo ".csv" de registros, nos quais são executados nos dois algoritmos. No Divide and Conquer - Merge Sort é executado o algoritmo que ordena os registros de forma crescente por um ID inteiro, retornando essa lista de registros ordenados. No Divide and Conquer - Counting Inversions é executado o algoritmo do Merge Sort, contudo, com uma lógica a mais que permite a contagem das inversões comparadas com o grupo ordenado desses registros.

##### Visualização

Para a visualização dos resultados foi utilizado o Framework Django da linguagem de programação Python, de modo que foi possível criar uma interface Web estilizada por meio do framework Bootstrap.  

##### Divide and Conquer - Merge Sort

São indicados na tela os registros ordenados, uma imagem de exemplo do funcionamento do algorítmo, o tempo de execução e uma observação sobre esse tipo de ordenação.

##### Divide and Conquer - Counting Inversions

São indicados na tela o tempo de execução do algorítmo, a quantidade de inversões e os registros não ordenados recebidos para a contagem das inversões com base nos registros ordenados.

##### Observações

Seguem três ".csv's" de exemplo de entrada para a aplicação, os três servem para as duas opções de algorítmos, contudo possuem quantidade de dados diferentes para testar os tempos de execução.