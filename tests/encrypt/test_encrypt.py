import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError) as error:
        encrypt_message("Amanda", "Carlos")
    assert str(error.value) == "tipo inválido para key"

    with pytest.raises(TypeError) as error:
        encrypt_message(4000, 30)
    assert str(error.value) == "tipo inválido para message"

    assert encrypt_message("XFAIL", 99) == "LIAFX"
    