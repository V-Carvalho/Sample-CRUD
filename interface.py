from dao import DAO

db = DAO()


class Interface:

    def new_register(self):
        print('')
        print('*********** Cadastro de usuários ***********')
        username = input('Nome: ')
        password = input('Senha: ')

        if username != '' and password != '':
            response = db.insert_data(username, password)
            if response == 1:
                print('Usuário cadastrado com sucesso!')
            else:
                print('Erro ao cadastrar usuário')
            self.quit_program()
        else:
            print('Todos os campos devem ser preenchidos!')
            self.new_register()

    def search_user(self):
        print('')
        print('*** Pesquisa de usuários (Insira * para visualizar todos os usuários cadastrados!) ***')
        username = input('Nome do usuário: ')
        if username != '':
            data = db.select_data(username)
            if len(data.fetchall()) == 0:
                print('Usuário não encontrado!')
                self.search_user()
            else:
                data = db.select_data(username)
                for row in data:
                    print(f'ID: ' + str(row[0]) + ' | Nome: ' + str(row[1]) + ' | Senha: ' + str(row[2]))
        else:
            print('Todos os campos devem ser preenchidos!')
            self.search_user()

    def update_user(self):
        print('')
        print('*********** Atualizar dados do usuário ***********')
        username = input('Nome do usuário: ')
        new_username = input('Novo nome de usuário:')
        if username != '' and new_username != '':
            response = db.update_data(new_username, username)
            if response >= 1:
                print('Dados alterados com sucesso!')
            else:
                print('Erro ao alterar dados do usuário')
        else:
            print('Informe um nome!')
            self.update_user()

    def delete_user(self):
        print('')
        print('*** Deletar usuário (Insira * para deletar todos os usuários cadastrados!) ***')
        username = input('Nome do usuário: ')
        if username != '':
            response = db.delete_data(username)
            print(response)
            if response >= 1:
                print('Usuário deletado com sucesso!')
            elif response == -1:
                print('Todos os dados foram deletados!')
            else:
                print('Erro ao deletar usuário')
        else:
            print('Informe um nome!')
            self.search_user()

    def quit_program(self):
        new_register = input('Deseja voltar ao menu? (sim/não)')
        print(' ')
        if new_register == 'não':
            exit(0)
