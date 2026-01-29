import json
import os

ARQUIVO_DADOS = "tarefas.json"

def carregar_tarefas():
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

def listar_tarefas(tarefas):
    print("\n--- MINHAS TAREFAS ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    for i, tarefa in enumerate(tarefas, 1):
        status = "✅" if tarefa["concluida"] else "❌"
        print(f"{i}. [{status}] {tarefa['descricao']}")
    print("-" * 22)

def main():
    tarefas = carregar_tarefas()

    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar como Concluída")
        print("4. Remover Tarefa")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            desc = input("Descrição da tarefa: ")
            tarefas.append({"descricao": desc, "concluida": False})
            salvar_tarefas(tarefas)
            print("Tarefa adicionada!")

        elif opcao == "2":
            listar_tarefas(tarefas)

        elif opcao == "3":
            listar_tarefas(tarefas)
            try:
                num = int(input("Número da tarefa concluída: ")) - 1
                tarefas[num]["concluida"] = True
                salvar_tarefas(tarefas)
                print("Status atualizado!")
            except (ValueError, IndexError):
                print("Número inválido.")

        elif opcao == "4":
            listar_tarefas(tarefas)
            try:
                num = int(input("Número da tarefa para remover: ")) - 1
                tarefas.pop(num)
                salvar_tarefas(tarefas)
                print("Tarefa removida!")
            except (ValueError, IndexError):
                print("Número inválido.")

        elif opcao == "5":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()