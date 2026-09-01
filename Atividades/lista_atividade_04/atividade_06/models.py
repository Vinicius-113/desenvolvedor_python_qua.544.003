
from abc import ABC, abstractmethod


class IConta(ABC):

    @abstractmethod
    def consultar_dados(self):
        pass

    @abstractmethod
    def gerar_extrato(self):
        pass

    @abstractmethod
    def depositar(self, valor: float) -> float:
        pass

    @abstractmethod
    def sacar(self, valor: float) -> float:
        pass


class Pessoa:

    def __init__(self, nome: str, cpf: str):
        self.__nome = nome
        self.__cpf = cpf

    # Getter e Setter - nome
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    # Getter e Setter - CPF
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, valor):
        self.__cpf = valor

    def __str__(self):
        return f"Nome: {self.__nome} | CPF: {self.__cpf}"


class Conta(IConta):

    def __init__(
        self,
        titular: Pessoa,
        agencia: str,
        n_conta: str,
        saldo: float = 0.0
    ):
        self.__titular = titular
        self.__agencia = agencia
        self.__n_conta = n_conta
        self.__saldo = saldo

    # Getter e Setter - titular
    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, valor):
        self.__titular = valor

    # Getter e Setter - agência
    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self, valor):
        self.__agencia = valor

    # Getter e Setter - número da conta
    @property
    def n_conta(self):
        return self.__n_conta

    @n_conta.setter
    def n_conta(self, valor):
        self.__n_conta = valor

    # Getter e Setter - saldo
    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    # Métodos da interface
    def consultar_dados(self):
        print("\n===== DADOS DA CONTA =====")
        print(f"Titular: {self.__titular}")
        print(f"Agência: {self.__agencia}")
        print(f"Conta: {self.__n_conta}")
        print(f"Saldo: R$ {self.__saldo:.2f}")

    def gerar_extrato(self):
        print("\n===== EXTRATO =====")
        print(f"Titular: {self.__titular.nome}")
        print(f"Conta: {self.__n_conta}")
        print(f"Saldo atual: R$ {self.__saldo:.2f}")

    def depositar(self, valor: float) -> float:
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")

        self.__saldo += valor

        return self.__saldo

    def sacar(self, valor: float) -> float:
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")

        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente.")

        self.__saldo -= valor

        return self.__saldo

