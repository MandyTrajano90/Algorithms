from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError) as error:
        encrypt_message('Amanda', 'Carlos')
    assert str(error.value) == 'The message must be a string'

    with pytest.raises(TypeError) as error:
        encrypt_message(4000, 30)
    assert str(error.value) == 'The key must be a string'

    assert encrypt_message("XFAIL", 99) == "LIAFX"
    assert encrypt_message("HELLO", 3) == "KHOOR"
