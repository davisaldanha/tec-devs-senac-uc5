from exceptions.exceptions import *

def validation_age(idade: int):
    '''Validar se a idade corresponde ao limite permitido. (1 - 150)'''
    if not (idade > 0 and idade <= 150):
        raise AgeException("Validation Error: Idade não corresponde ao limite 1 - 150")

def validation_phone(telefone: str):
    '''Validar se o telefone corresponde ao padrão de 11 dígitos numéricos.'''
    if not (telefone.isdigit() and len(telefone) == 11):
        raise PhoneException("Validation Error: O telefone não corresponde a 11 dígitos numéricos.")


def validation_cpf(cpf: str):
    '''Validar se o cpf corresponde ao padrão de 11 dígitos numéricos.'''
    if not (cpf.isdigit() and len(cpf) == 11):
        raise CpfException("Validation Error: O cpf não corresponde a 11 dígitos numéricos.")
