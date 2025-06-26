from database.connection import get_connection
from models.escritor import Escritor
from models.classe import Classe
from models.magia import Magia
from models.magia_classe import MagiaClasse

def menu_escritor(connection):
    while True:
        print("\n=== MENU ESCRITOR ===")
        print("1 - Adicionar escritor")
        print("2 - Buscar escritor por ID")
        print("3 - Listar todos os escritores")
        print("4 - Atualizar escritor")
        print("5 - Deletar escritor")
        print("0 - Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do escritor: ")
            escritor = Escritor(None, nome)
            id_criado = escritor.create(connection)
            print(f"Escritor criado com ID: {id_criado}")
        
        elif opcao == '2':
            id_escritor = int(input("ID do escritor: "))
            escritor = Escritor.read(connection, id_escritor)
            if escritor:
                print(f"ID: {escritor.id_escritor}, Nome: {escritor.nome}")
            else:
                print("Escritor não encontrado.")
        
        elif opcao == '3':
            escritores = Escritor.read_all(connection)
            if escritores:
                for escritor in escritores:
                    print(f"ID: {escritor.id_escritor}, Nome: {escritor.nome}")
            else:
                print("Nenhum escritor encontrado.")
        
        elif opcao == '4':
            id_escritor = int(input("ID do escritor a atualizar: "))
            escritor = Escritor.read(connection, id_escritor)
            if escritor:
                print(f"Nome atual: {escritor.nome}")
                novo_nome = input("Novo nome: ")
                escritor.nome = novo_nome
                if escritor.update(connection):
                    print("Escritor atualizado com sucesso.")
                else:
                    print("Erro ao atualizar escritor.")
            else:
                print("Escritor não encontrado.")
        
        elif opcao == '5':
            id_escritor = int(input("ID do escritor a deletar: "))
            if Escritor.delete(connection, id_escritor):
                print("Escritor deletado com sucesso.")
            else:
                print("Escritor não encontrado ou erro ao deletar.")
        
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")

def menu_classe(connection):
    while True:
        print("\n=== MENU CLASSE ===")
        print("1 - Adicionar classe")
        print("2 - Buscar classe por ID")
        print("3 - Listar todas as classes")
        print("4 - Atualizar classe")
        print("5 - Deletar classe")
        print("0 - Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome da classe: ")
            classe = Classe(None, nome)
            id_criado = classe.create(connection)
            print(f"Classe criada com ID: {id_criado}")
        
        elif opcao == '2':
            id_classe = int(input("ID da classe: "))
            classe = Classe.read(connection, id_classe)
            if classe:
                print(f"ID: {classe.id_classe}, Nome: {classe.nome}")
            else:
                print("Classe não encontrada.")
        
        elif opcao == '3':
            classes = Classe.read_all(connection)
            if classes:
                for classe in classes:
                    print(f"ID: {classe.id_classe}, Nome: {classe.nome}")
            else:
                print("Nenhuma classe encontrada.")
        
        elif opcao == '4':
            id_classe = int(input("ID da classe a atualizar: "))
            classe = Classe.read(connection, id_classe)
            if classe:
                print(f"Nome atual: {classe.nome}")
                novo_nome = input("Novo nome: ")
                classe.nome = novo_nome
                if classe.update(connection):
                    print("Classe atualizada com sucesso.")
                else:
                    print("Erro ao atualizar classe.")
            else:
                print("Classe não encontrada.")
        
        elif opcao == '5':
            id_classe = int(input("ID da classe a deletar: "))
            if Classe.delete(connection, id_classe):
                print("Classe deletada com sucesso.")
            else:
                print("Classe não encontrada ou erro ao deletar.")
        
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")

def menu_magia(connection):
    while True:
        print("\n=== MENU MAGIA ===")
        print("1 - Adicionar magia")
        print("2 - Buscar magia por ID")
        print("3 - Listar todas as magias")
        print("4 - Atualizar magia")
        print("5 - Deletar magia")
        print("6 - Buscar magias por escola")
        print("7 - Buscar magias por nível")
        print("0 - Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome da magia: ")
            nivel = int(input("Nível (0-9): "))
            alcance = input("Alcance: ")
            duracao = input("Duração: ")
            concentracao = input("Requer concentração? (s/n): ").lower() == 's'
            escola = input("Escola: ")
            ritual = input("É ritual? (s/n): ").lower() == 's'
            descricao = input("Descrição: ")
            escritor_id = int(input("ID do escritor: "))
            
            magia = Magia(None, nome, nivel, alcance, duracao, concentracao, 
                         escola, ritual, descricao, escritor_id)
            id_criado = magia.create(connection)
            print(f"Magia criada com ID: {id_criado}")
        
        elif opcao == '2':
            id_magia = int(input("ID da magia: "))
            magia = Magia.read(connection, id_magia)
            if magia:
                print(f"ID: {magia.id_magia}")
                print(f"Nome: {magia.nome}")
                print(f"Nível: {magia.nivel}")
                print(f"Alcance: {magia.alcance}")
                print(f"Duração: {magia.duracao}")
                print(f"Concentração: {'Sim' if magia.concentracao else 'Não'}")
                print(f"Escola: {magia.escola}")
                print(f"Ritual: {'Sim' if magia.ritual else 'Não'}")
                print(f"Descrição: {magia.descricao}")
                print(f"ID Escritor: {magia.escritor_id}")
            else:
                print("Magia não encontrada.")
        
        elif opcao == '3':
            magias = Magia.read_all(connection)
            if magias:
                for magia in magias:
                    print(f"ID: {magia.id_magia}, Nome: {magia.nome}, Nível: {magia.nivel}, Escola: {magia.escola}")
            else:
                print("Nenhuma magia encontrada.")
        
        elif opcao == '4':
            id_magia = int(input("ID da magia a atualizar: "))
            magia = Magia.read(connection, id_magia)
            if magia:
                print(f"Nome atual: {magia.nome}")
                magia.nome = input("Novo nome (Enter para manter): ") or magia.nome
                novo_nivel = input(f"Novo nível atual {magia.nivel} (Enter para manter): ")
                magia.nivel = int(novo_nivel) if novo_nivel else magia.nivel
                magia.alcance = input(f"Novo alcance atual '{magia.alcance}' (Enter para manter): ") or magia.alcance
                magia.duracao = input(f"Nova duração atual '{magia.duracao}' (Enter para manter): ") or magia.duracao
                nova_conc = input(f"Concentração atual {'Sim' if magia.concentracao else 'Não'} (s/n/Enter para manter): ")
                if nova_conc.lower() in ['s', 'n']:
                    magia.concentracao = nova_conc.lower() == 's'
                magia.escola = input(f"Nova escola atual '{magia.escola}' (Enter para manter): ") or magia.escola
                novo_ritual = input(f"Ritual atual {'Sim' if magia.ritual else 'Não'} (s/n/Enter para manter): ")
                if novo_ritual.lower() in ['s', 'n']:
                    magia.ritual = novo_ritual.lower() == 's'
                magia.descricao = input(f"Nova descrição (Enter para manter): ") or magia.descricao
                novo_escritor = input(f"Novo ID escritor atual {magia.escritor_id} (Enter para manter): ")
                magia.escritor_id = int(novo_escritor) if novo_escritor else magia.escritor_id
                
                if magia.update(connection):
                    print("Magia atualizada com sucesso.")
                else:
                    print("Erro ao atualizar magia.")
            else:
                print("Magia não encontrada.")
        
        elif opcao == '5':
            id_magia = int(input("ID da magia a deletar: "))
            if Magia.delete(connection, id_magia):
                print("Magia deletada com sucesso.")
            else:
                print("Magia não encontrada ou erro ao deletar.")
        
        elif opcao == '6':
            escola = input("Nome da escola: ")
            magias = Magia.read_by_escola(connection, escola)
            if magias:
                for magia in magias:
                    print(f"ID: {magia.id_magia}, Nome: {magia.nome}, Nível: {magia.nivel}")
            else:
                print("Nenhuma magia encontrada para esta escola.")
        
        elif opcao == '7':
            nivel = int(input("Nível (0-9): "))
            magias = Magia.read_by_nivel(connection, nivel)
            if magias:
                for magia in magias:
                    print(f"ID: {magia.id_magia}, Nome: {magia.nome}, Escola: {magia.escola}")
            else:
                print("Nenhuma magia encontrada para este nível.")
        
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")

def menu_relacionamentos(connection):
    while True:
        print("\n=== MENU RELACIONAMENTOS MAGIA-CLASSE ===")
        print("1 - Associar magia a classe")
        print("2 - Remover associação magia-classe")
        print("3 - Ver classes de uma magia")
        print("4 - Ver magias de uma classe")
        print("5 - Ver todas as associações")
        print("0 - Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            magia_id = int(input("ID da magia: "))
            classe_id = int(input("ID da classe: "))
            if MagiaClasse.associar_magia_classe(connection, magia_id, classe_id):
                print("Associação criada com sucesso.")
            else:
                print("Erro ao criar associação.")
        
        elif opcao == '2':
            magia_id = int(input("ID da magia: "))
            classe_id = int(input("ID da classe: "))
            if MagiaClasse.remover_associacao(connection, magia_id, classe_id):
                print("Associação removida com sucesso.")
            else:
                print("Associação não encontrada.")
        
        elif opcao == '3':
            magia_id = int(input("ID da magia: "))
            classes = MagiaClasse.get_classes_por_magia(connection, magia_id)
            if classes:
                print("Classes que podem usar esta magia:")
                for classe in classes:
                    print(f"ID: {classe['id']}, Nome: {classe['nome']}")
            else:
                print("Nenhuma classe associada a esta magia.")
        
        elif opcao == '4':
            classe_id = int(input("ID da classe: "))
            magias = MagiaClasse.get_magias_por_classe(connection, classe_id)
            if magias:
                print("Magias disponíveis para esta classe:")
                for magia in magias:
                    print(f"ID: {magia['id']}, Nome: {magia['nome']}, Nível: {magia['nivel']}, Escola: {magia['escola']}")
            else:
                print("Nenhuma magia associada a esta classe.")
        
        elif opcao == '5':
            associacoes = MagiaClasse.get_todas_associacoes(connection)
            if associacoes:
                print("Todas as associações Magia-Classe:")
                for assoc in associacoes:
                    print(f"Magia: {assoc['magia']} (Nível {assoc['nivel']}) - Classe: {assoc['classe']}")
            else:
                print("Nenhuma associação encontrada.")
        
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")

def main():
    connection = get_connection()
    if not connection:
        raise Exception("Não foi possível conectar ao banco de dados.")

    while True:
        print("\n" + "="*50)
        print("    ENCICLOPÉDIA DE MAGIAS - SISTEMA CRUD")
        print("="*50)
        print("1 - Gerenciar Escritores")
        print("2 - Gerenciar Classes")
        print("3 - Gerenciar Magias")
        print("4 - Gerenciar Relacionamentos Magia-Classe")
        print("0 - Sair")
        print("="*50)
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_escritor(connection)
        elif opcao == '2':
            menu_classe(connection)
        elif opcao == '3':
            menu_magia(connection)
        elif opcao == '4':
            menu_relacionamentos(connection)
        elif opcao == '0':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida.")

    connection.close()

if __name__ == "__main__":
    main()

