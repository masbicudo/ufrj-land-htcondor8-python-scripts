# Usando o cluster do LAND (UFRJ) com HTCondor

Neste repositório estão alguns scripts que demonstram
como utilizar o cluster do LAND, que no momento conta
com nós que possuem: HTCondor 8, Python 3.6.9 e Python 3.8.0.

## Arquivos

- **create-venv.sh**: cria o ambiente virtual do Python 3.8 usando o módulo `virtualenv`, que por sua vez está instalado no Python 3.6. Após a criação do ambiente a versão do Pip é atualizada.
- **job.py**: arquivo da tarefa que recebe os parametros passados pelo arquivo `submit.py`.
- **job.sh**: script que inicializa o ambiente virtual do nó do cluster e em seguida chama o arquivo `job.py`.
- **submit.py**: código que submete várias tarefas variando os parâmetros, ao mesmo tempo que copia o ambiente virtual para os nós do cluster e obtém os arquivos resultantes das tarefas através da pasta `result`.

