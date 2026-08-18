# Espaços Vetoriais de Dimensão Finita

Repositório educativo e prático sobre **Espaços Vetoriais de Dimensão Finita**.

Este projeto cobre os conceitos fundamentais da Álgebra Linear relacionados com espaços de dimensão finita, desde a definição de espaço vetorial até à mudança de base, com implementações em Python puro.

## Objetivos de Aprendizagem

- Compreender a definição formal de espaço vetorial e subespaço
- Verificar independência e dependência linear
- Determinar bases e calcular a dimensão
- Representar vetores por coordenadas relativamente a uma base
- Realizar mudanças de base
- Aplicar os conceitos a problemas concretos

## Estrutura

| Pasta / Ficheiro     | Conteúdo                                      |
|----------------------|-----------------------------------------------|
| `docs/`              | Explicações teóricas detalhadas               |
| `src/`               | Implementações principais                     |
| `examples/`          | Exemplos de utilização                        |
| `tests/`             | Testes unitários                              |

## Conceitos Abordados

- Espaço vetorial e axiomas
- Subespaços vetoriais
- Combinações lineares e Span
- Independência linear
- Base e dimensão
- Coordenadas de um vetor
- Matriz de mudança de base
- Teorema da dimensão

## Instalação e Utilização

```bash
git clone https://github.com/TEU_USER/espacos-vetoriais-dimensao-finita.git
cd espacos-vetoriais-dimensao-finita

pip install -r requirements.txt

# Executar exemplos
python examples/01_verificar_independencia.py
python examples/04_mudanca_de_base.py

# Correr testes
pytest
