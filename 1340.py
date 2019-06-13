# -*- coding:utf-8 -*-

# metodo para insercao em uma fila de prioridade
def priority_queue_insertion(queue, value):
    inserted = False
    for i in range(len(queue)):
        if queue[i] >= value:
            queue.insert(i, value)
            inserted = True

    if not inserted:
        queue.append(value)

# faz a comparacao de duas listas elemento a elemento e retorna True caso sejam iguais
def lists_equal(l1, l2):
    tam = len(l1)

    if tam != len(l2):
        return False

    for i in range(tam):
        if l1[i] != l2[i]:
            return False

    return True


# FLUXO PRINCIPAL
# ESTRATEGIA: criar blocos independentes de codigo responsaveis por identificar se eh a estrutura dada ou nao
while True:
    try:
        # captura da entrada
        n = int(input())
        p_queue = []
        p_queue_out = []

        struct_stack = []
        stack_out = []

        entrada = []
        saida = []
        for i in range(n):
            op, val = input().split()

            if op == '1':
                entrada.append(int(val))
                priority_queue_insertion(p_queue, int(val))
                struct_stack.append(int(val))
            else:
                saida.append(int(val))
                p_queue_out.append(p_queue.pop())
                stack_out.append(struct_stack.pop())

        sairam = len(saida)

        # RECONHECIMENTO DAS ESTRUTURAS (guardar em um booleano o resultado de cada teste)
        # 1: FILA (verifica se a ordem do vetor saida eh igual a ordem de entrada)
        queue = lists_equal(entrada[:sairam], saida)


        # 2: PILHA (verifica se a ordem de saida eh inversa a de entrada)
        stack = lists_equal(saida, stack_out)


        # 3: PRIORITY_QUEUE (implementar Fila de prioridade???)
        priority_queue = lists_equal(saida, p_queue_out)


        # saida
        if (not stack) and (not queue) and (not priority_queue):
            print("impossible")
        elif stack and (not queue) and (not priority_queue):
            print("stack")
        elif (not stack) and queue and (not priority_queue):
            print("queue")
        elif (not stack) and (not queue) and priority_queue:
            print("priority queue")
        else:
            print("not sure")

    except EOFError:
        break
