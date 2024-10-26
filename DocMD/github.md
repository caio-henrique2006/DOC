# Git

# Conceitos

## O que é um Version Control System (VCS)

Um sistema de controle de versionamento de código é simplesmente um sistema que guarda o histórico de mudanças dentro de um arquivo no computador. Dessa forma é possível ter acesso a todas as modificações que ocorreram e voltar, caso necessário, para versões anteriores do arquivo.

## Centralized Version Control Systems (CVCS)

Sistemas de controle de versionamento que ficavam armazenados em um servidor e permitiam os usuários compartilhar as suas contribuições com o projeto.
Um problema com esses sistemas é que como todo o projeto está sendo compartilhado em um único servidor, caso esse servidor fique fora do ar não é possível trabalhar nele e se seu armazenamento se corromper sem um backup próximo, parte ou todo o projeto se perde.

## Distributed Version Control Systems (DVCS)

Sistemas de controle de versionamento que ao invés de ter os arquivos centralizados em um servidor, todos os usuários conseguem gerar uma cópia espelhada desses arquivos, podendo trabalhar localmente como um VCS e enviar suas contribuições para o servidor conjunto como um CVCS.
Git é um exemplo de Sistema de Controle de Versionamento Distribuído.

## Git snapshots (picture) logic

Toda vez que um código é commitado, o git tira uma foto (print) de como os arquivos do projeto estão naquele exato momento. Essa forma é diferente de pensar, já que outras Sistemas de Versionamento guardavam as mudanças no que é chamado de **delta-based version control**, onde cada "commit" guardava apenas as mudanças que ocorreram de um arquivo para o outro.

## Porque git é poderoso localmente?

Como git clona uma cópia de todo o projeto para o computador, ele pode executar todos os seus comandos localmente, dessa forma, todos os comandos são rápidos e é possível trabalhar no projeto sem uma conexão com a internet (É claro que é necessário enviar para o servidor compartilhado depois).

## Por que é impossível modificar um arquivo sem o git saber?

O git interpreta todo arquivo em um projeto como um hash de 40 digitos baseado nas informações que vem no arquivo. Essa capacidade é construída em low-level no git e impede, por exemplo, a existência de arquivos corrompidos sem o git saber.

## Por que é difícil deletar dados no git ?

A partir do momento que um commit é feito, é difícil perder a referência aos arquivos que estavam naquele snapshot (print) do projeto.

## Git three states

Todo arquivo no seu projeto pode ter 3 estados.

- modified: Você mudou algo no arquivo, mas ainda não commitou.
- staged: Arquivos modificados escolhidos que vão fazer parte do próximo commit
- committed: Você comittou seus arquivos staged e agora eles representam a versão atual do seu arquivo.

# Commands

## Ação:

```bash
# Cria um novo repositório git localmente. Cria uma pasta .git no diretório onde é executado
git init

#
git add .
git commit -m "comentário"
git push
git branch
git checkout -b [nova-branch] [tracking-branch]
git checkout [branch]
git merge [branch-to-be-merged-to-current-branch]
```

## Consulta:

```bash
git status
git branch -r
git branch -avv
```
