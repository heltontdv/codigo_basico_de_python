from multiprocessing import Process

def tarefa(nome):
    print(f"Tarefa {nome} em execução")

if __name__ == "__main__":
    processos = [Process(target=tarefa, args=(i,)) for i in range(5)]
    for p in processos:
        p.start()
    for p in processos:
        p.join()
