from dao import DAO
from interface import Interface

db = DAO()
db.create_database()
interface = Interface()

while True:
    try:
        print('')
        print('Selecione uma Operação:')
        print('1 - Adicionar Usuário')
        print('2 - Pesquisar Usuário')
        print('3 - Atualizar Usuário')
        print('4 - Deletar Usuário')
        option = int(input('Informe a opção: '))

        if option == 1:
            interface.new_register()
        elif option == 2:
            interface.search_user()
        elif option == 3:
            interface.update_user()
        elif option == 4:
            interface.delete_user()
        elif option > 4:
            print('Opção não reconhecida, por favor informar um número!')

    except ValueError as error:
        print('Opção não reconhecida, por favor informar um número!')
