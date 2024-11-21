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

## O que são untracked files em git?

São todos os arquivos adicionados no repositório que ainda não foram colcoados em nenhum commit. Use git add para fazer o tracking do arquivo.

## Diferença entre autor e commiter em git

Autor é a pessoa que fez o código, que o modificou. Já o commiter foi a pessoa que aplicou essas modificações em um commit. Dessa forma, tanto a pessoa que commitou quanto o próprio autor ganham crédito pelo commit.

## Dois tipos de Tag em git lightweight e annotated

A lightweight é simplesmente uma tag simples de texto que aponta para o commit. Já a tag annotated guarda diversas informações de quem fez o commit com segurança e assinatura GNU Privacy Guard.

## O que o HEAD em git e como funciona a lógica de pointers?

O HEAD é um pointer especial que indica em que branch você está naquele momento. A branch por consequência aponta para um commit e um commit aponta para seus commits passados e internamente para os arquivos em árvore armazenados (snapshots)

## O que é fast-forward merging e merge commit em git?

fast-forward merge ocorre quando é possível fazer o merge de duas branches que são parentes diretas na árvore, por exemplo, a master branch e um hotfix rápido. Dessa forma git apenas aponta a master branch direto para a branch hotfix, já que não existe outros commits diferentes no meio entre os dois.
Já o merge commit ocorre quando as branches não são parentes diretos, ou seja, existem modificações nas duas. Então o git vai criar um novo commit (snapshot) que vai representar o merge das modificações das duas. Esse commit é conhecido por merge commit.

# Commands

## Configuration

```bash
# Comandos para as configurações do git
git config --list
git config --global user.name <name>
git config --global user.email <email>

```

## Iniciar git

```bash
# Cria um novo repositório git localmente. Cria uma pasta .git no diretório onde é executado
git init
git clone <url>
git clone <url> <directory_name>

```

## Modifying

```bash
git checkout -- <file>
git restore <file>
```

## Stage

```bash
# Adiciona os arquivos modificados para o próximo commit (staging)
git add .
git reset HEAD <file> # Tira o arquivo do próximo commit
git rm <file> # Remover arquivo tracked
git rm -f <file> # Força caso o arquivo já tenha sido staged para o próximo commit
git rm --cached <file> # Remove do staged
git restore --staged <file> # Remove do staged
```

## Consulta

```bash
# Mostra o estado dos arquivos do projeto:
git status
git status -s
git branch -r
git branch -avv
```

## Commiting

```bash
# Faz o commit (snapshot) do código:
git commit
git commit -m "comentário"
git commit -a # Stage todos os arquivos modificados e commita.
git commit --amend # permite substituir o último commit caso tenha esquecido de algo.

```

## Logs (Commit history)

```bash
# Mostra o histórico de commits
git log
git log -2 # Mostra apenas os dois últimos commits
git log -p # Mostra as mudanças que ocorreram no commit
git log --stat # Mostra as estatíticas do commit
git log --pretty=online # Mostra os commits com uma formatação diferente, existem várias opções para o --pretty
git log --graph # Mostra o caminho de criação e merge das branches.
git log --since="2022-10-01"
git log --until="2023-10-03"
git log --author="Caio Henrique"
git log --grep="keyword"
git log -- path/to/file
git log --no-merges # Não mostra os commits de merge.
# Mostra as exatas mudanças que ocorreram nos arquivos:
git diff
git diff --staged
git diff --cached
```

## Remote repository

```bash
git remote # Indica o repositório remoto configurado para aquele projeto
git remote -v # Link do repositório
git remote add <shortname> <url> # Adiciona um novo repositório remoto (usar fetch para puxar a branch main)
git remote show <remote>
git remote rename <remote> <new-shortname>
git remote remove <remote>
git fetch <remote> # Pega os dados do repositório remoto que você não tem (não faz o merge)
git pull # Puxa os dados do repositório remoto daquela branch (se tiver) (faz o merge)
git push <remote> <branch> # Envia seus commits para o repositório remoto
```

## Tagging

```bash
git tag -l # Lista todas as tags
git tag -a <tag-name> -m "<message>" # Cria uma tag
git show <tag-name> # Mostra uma tag específica
git tag <tag-name> # lightweigth tag
git tag -a <tag-name> <commit-checksum(hash)> # Tagging em um commit passado
git push origin <tag-name>
git push origin --tags # Envia as tags para o repositório remoto
git tag -d <tagname> # Deletando tag
git push origin --delete <tagname> # Deleta tag do repositório remoto
```

## Branching

```bash
git branch # Shows list of branches
git branch -v # Shows last commit on branch
git branch --merged # shows list of branches tat you didnt merge
git branch <branch-name> # Create branch
git branch -d <branch-name> # Deleta branch
git branch --move <old-branch-name> <new-branch-name> # Changes branch name
git merge <branch-name> # Merge the current HEAD->Branch to the <branch-name>

git checkout <branch-name> # Moves HEAD to branch-name
git checkout -b <branch-name> # Create and moves HEAD to branch-name
```

```bash

git push
git branch
git checkout -b [nova-branch] [tracking-branch]
git checkout [branch]
git merge [branch-to-be-merged-to-current-branch]
```
