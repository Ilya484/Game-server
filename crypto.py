from hashlib import sha256


def encrypt(string: str) -> str:
    """
    Зашифровка в sha256
    :param string: str
    :return: str
    """
    return sha256(string.encode("utf-8")).hexdigest()
