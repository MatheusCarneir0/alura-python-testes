import pytest
import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.user_model import serialize_user

def test_serialize_user_completo():

    user = {
        "email": "tete@example.com",
        "name": "Test User",
        "address": "123 Test St",
        "role": "admin"
    }

    resultado = serialize_user(user)

    esperado = {
        "email": "tete@example.com",
        "name": "Test User",
        "address": "123 Test St",
        "role": "admin"
    }

    assert resultado == esperado


def test_serialize_user_incompleto():

    user = {
        "email": "tete@example.com"
    }

    resultado = serialize_user(user)

    esperado = {
        "email": "tete@example.com",
        "name": "",
        "address": "",
        "role": "cliente"
    }

    assert resultado == esperado


def test_serialize_user_completo():

    user = {}

    resultado = serialize_user(user)

    esperado = {
        "email": None,
        "name": "",
        "address": "",
        "role": "cliente"
    }

    assert resultado == esperado


def test_serialize_user_inteiro():
    with pytest.raises(AttributeError):
        serialize_user(123456)


def test_serialize_user_string():
    with pytest.raises(AttributeError):
        serialize_user("string teste")


def test_serialize_user_lista():
    with pytest.raises(AttributeError):
        serialize_user([])


def test_serialize_user_none():
    with pytest.raises(AttributeError):
        serialize_user(None)                                                                


def test_serialize_user_inesperado():
    user = {
        "email": 12345,
        "name": None,
        "address": ["Rua Teste"],
        "role": True
    }

    resultado = serialize_user(user)

    esperado = {
        "email": 12345,
        "name": None,
        "address": ["Rua Teste"],
        "role": True
    }

    assert resultado == esperado


def test_serializer_user_dict_none():

    user = {
        "email": None,
        "name": None,
        "address": None,
        "role": None
    }

    resultado = serialize_user(user)

    esperado = {
        "email": None,
        "name": None,
        "address": None,
        "role": None
    }

    assert resultado == esperado
