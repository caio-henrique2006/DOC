# Diferença entre paralelismo e concorrência

**Paralelismo:** 
Quando duas ou mais tarefas são executados literalmente ao mesmo tempo. Sendo necessário mais de um núcleo para que ocorra paralelismo.

**Concorrência:** 
Quando duas ou mais tarefas que começam e terminam suas execuções em espaços de tempo que se sobrepoe. Podem ser executadas em apenas um núcleo, pulando de instruções de uma para a outra.

# Sistemas multitarefas
A concorência é o princípio base que permite que um sistema execute mais de um programa por vez, chamados de sistemas multitarefas.

# Classificação dos processos

### CPU Bound
Atividades/aplicações que exigem grande uso da CPU na execução.
### I/O Bound
Atividades/aplicações que exigem espera por Input e Output, como requisições em rede, transferência de arquivos. (Não confundir com I/O puramente do usuário).

# Múltiplos processos:
Implementação de concorrência em que vários processos são criados em que não há conexão entre eles e eles não compartilham contextos de hardware, software e memória.

# Subprocessos:
Subprocessos são processos criados apartir de um processo pai, havendo conexão hierarquica entre os processos. Caso o processo pai seja interrompido, os filhos também são. Eles não compartilham contextos de hardware, software e memória.

# Threads:
Threads são "processos leves" originados de um processo pai que não compartilham o contexto de hardware, mas compartilham o contexto de software e memória. Como eles compartilham software e memória são necessárias algumas medidas para que conflitos não ocorram.

# Python Global Interpreter Lock (GIL)
GIL é uma implementação de Lock em Python no nível de interpretador, ou seja, apenas uma thread pode ser interpretada por vez. Entretanto isso não significa que a performace diminui, pois o GIL é solto quando há I/O bound processos.

# Lock, programação em concorrência
Lock é a implementação de mútua exclusão (Mutex) em concorrência, sua função é impedir que mais de uma thread tenha acesso a um recurso. Podem existir outros tipos além de Mutex, que definem regras diferentes de acesso a um recurso.
