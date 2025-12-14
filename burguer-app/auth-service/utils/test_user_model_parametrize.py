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
            "email": 123,
            "name": ["Teste", "Ususario"],
            "address": {"street": "123 Test St"},
            "role": True
        },
        {
            "email": 123,
            "name": ["Teste", "Ususario"],
            "address": {"street": "123 Test St"},
            "role": True
        }
    )
])

def test_serialize_user_parametrized(user, esperado):
    resultado = serialize_user(user)
    assert resultado == esperado

@pytest.mark.parametrize("entrada", [
     None,
     "string",
     12345,
     []
])

def test_serialize_user_parametrizado_execucao(entrada):
    with pytest.raises(AttributeError):
        serialize_user(entrada)
