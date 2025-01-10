# Batalha Naval

Este é um jogo de **Batalha Naval** desenvolvido em Java, onde você pode jogar contra a máquina ou contra outro jogador humano. O objetivo é afundar todos os navios do adversário, atacando posições no tabuleiro.

## Como Jogar

### Requisitos
- Java 8 ou superior

### Instruções de Jogo

1. **Objetivo**: O objetivo do jogo é afundar todos os navios do adversário.
2. **Jogadores**: Você pode jogar contra a máquina ou contra outro jogador humano.
3. **Tabuleiro**: O jogo utiliza um tabuleiro de 10x10 onde cada jogador posiciona seus navios.
4. **Navios**: São utilizados navios de tamanhos variados (1, 2, 3, 4 e 5 quadrados). Eles são posicionados aleatoriamente no tabuleiro.
5. **Ataques**: Em cada turno, o jogador pode atacar uma posição do tabuleiro adversário.
6. **Fim do Jogo**: O jogo termina quando todas as embarcações de um dos jogadores forem afundadas.

### Como Rodar

1. **Clonar o repositório**:
    ```bash
    git clone https://github.com/usuario/batalha-naval.git
    cd batalha-naval
    ```

2. **Compilar e rodar o projeto**:

    Se você estiver utilizando o **Maven**:
    ```bash
    mvn clean install
    mvn exec:java
    ```

    Se estiver utilizando apenas o **Java** diretamente:
    Compile o código:
    ```bash
    javac *.java
    ```

    Em seguida, execute o código:
    ```bash
    java Main
    ```

## Estrutura do Projeto

O projeto é estruturado da seguinte forma:

