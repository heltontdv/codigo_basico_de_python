from concurrent.futures import ThreadPoolExecutor

def tarefa(nome):
    print(f"Tarefa {nome}")

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(tarefa, range(5))
