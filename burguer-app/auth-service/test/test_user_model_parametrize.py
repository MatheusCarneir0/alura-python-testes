import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user_model import serialize_user

@pytest.mark.parametrize("user, esperado", [
    (
        {
            "email": "tete@example.com",
            "name": "Test User",
            "address": "123 Test St",
            "role": "admin"
        
        },
        {
            "email": "tete@example.com",
            "name": "Test User",
            "address": "123 Test St",
            "role": "admin"
        }
    ),
    (
        {
            "email": "tete@example.com"
        },
        {
            "email": "tete@example.com",
            "name": "",
            "address": "",
            "role": "cliente"
        }
    ),
    (
        {
            "email": "teste@example.com",
        },
        {
            "email": "teste@example.com",
            "name": "",
            "address": "",
            "role": "cliente"
        }
    ),
    (
        {},
        {
            "email": None,
            "name": "",
            "address": "",
            "role": "cliente"
        }
    ),
    (
        {
            "email": None,
            "name": None,
            "address": None,
            "role": None
        },
        {
            "email": None,
            "name": None,
            "address": None,
            "role": None
        }
    ),
    (
        {
            "email": 12345,
            "name": ["Teste", "User"],
            "address": {"Rua Teste"},
            "role": True
        },
        {
            "email": 12345,
            "name": ["Teste", "User"],
            "address": {"Rua Teste"},
            "role": True
        }
    )       
])

def test_serialize_user_parametrizado(user, esperado):    
    resultado = serialize_user(user)
    assert resultado == esperado

@pytest.mark.parametrize("entrada", [   
    None,
    "string teste",
    [],
    123456
])

def test_serialize_user_parametrizado_excecao(entrada):
    with pytest.raises(AttributeError):
        serialize_user(entrada)