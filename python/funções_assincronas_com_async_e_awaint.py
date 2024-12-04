import asyncio

async def tarefa():
    print("Começando a tarefa...")
    await asyncio.sleep(2)
    print("Tarefa concluída!")

asyncio.run(tarefa())
