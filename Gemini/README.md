# Sistema Fuzzy para Gestão de Riscos de Projetos de Software

Este projeto implementa um Sistema de Inferência Fuzzy (SIF) para avaliar o Nível de Risco de um Projeto de Software (NRP). Utilizando 15 variáveis de entrada chave, o sistema processa essas informações através de uma base de regras fuzzy para gerar uma avaliação quantitativa do risco do projeto.

## Funcionalidades

* Avaliação de risco baseada em lógica fuzzy.
* Utiliza 15 variáveis de entrada relevantes para projetos de software.
* Interface de linha de comando para entrada de dados.
* Saída do nível de risco em uma escala de 0 a 100%.
* Implementado em Python com a biblioteca `scikit-fuzzy`.

## Estrutura do Repositório

* `sistema_risco_fuzzy.py`: O script principal Python contendo a lógica do sistema fuzzy.
* `README.md`: Este arquivo.
* `REPORT.md`: Documento detalhado descrevendo a metodologia, variáveis, conjuntos fuzzy, fases do sistema e considerações.
* `requirements.txt`: Lista das dependências Python para o projeto.

## Pré-requisitos

* Python 3.7 ou superior.

## Instalação de Dependências

1.  Clone o repositório (ou crie os arquivos manualmente).
2.  Navegue até o diretório do projeto.
3.  Recomenda-se criar e ativar um ambiente virtual:
    ```bash
    python -m venv venv
    # No Windows:
    # venv\Scripts\activate
    # No macOS/Linux:
    # source venv/bin/activate
    ```
4.  Instale as dependências listadas no arquivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
    (O conteúdo do `requirements.txt` está listado na seção "Dependências" abaixo).

## Dependências

As seguintes bibliotecas Python são necessárias:

* `numpy`
* `scikit-fuzzy`
* `matplotlib` (opcional, para visualização dos gráficos de pertinência e da saída fuzzy)

Você pode criar o arquivo `requirements.txt` com o seguinte conteúdo:

numpy
scikit-fuzzy
matplotlib


## Como Executar o Sistema

Após instalar as dependências, execute o script principal:

```bash
python sistema_risco_fuzzy.py