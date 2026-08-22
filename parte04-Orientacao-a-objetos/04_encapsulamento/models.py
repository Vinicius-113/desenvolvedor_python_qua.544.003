class Pessoa:
    def __init__(self,nome,cpf,email,telefone):
        
        self.__nome = nome
        self.__cpf = cpf                   #protect um _
        self.__email = email               #private dois __
        self.__telefone = telefone

        # métodos de acesso

        # get é o primeiro método (acessa o valor do atributo) 
        @property
        def nome(self):
            return self.__nome

        @property
        def cpf(self):
            return self.__cpf
        @property
        def email(self):
            return self.__email
        @property
        def telefone(self):
            return self.__telefone


        # Set: (definir o valor do atributo)
        @nome.setter
        def nome(self, nome):
            self.__nome = nome
        @cpf.setter
        def cpf(self, cpf):
            self.__cpf = cpf
        @email.setter
        def email(self, email):
            self.__email = email
        @telefone.setter
        def telefone(self, telefone):
            self.__telefone = telefone

    