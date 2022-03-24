from base64 import b64encode, b64decode
from ecies import encrypt, decrypt
from ecies.utils import generate_eth_key, generate_key
from eth_keys.main import PrivateKey


class EciesEth:
    """
    Adaptation to ECIES, a public-key authenticated encryption scheme to implement in Python3 projects.
    Require a library eciespy and key pair generated and parsed to Base64 as a priori.
    """

    def __init__(self, private_key: str = '', public_key: str = ''):
        """
        Constructor
        :param private_key: ECIES private key in Base64.
        :param public_key: ECIES public key in Base64.
        """

        if not private_key and not public_key:
            self.eth_key = generate_eth_key()

            private_key = self.eth_key.to_hex()
            private_key = b64encode(private_key.encode()).decode()

            public_key = self.eth_key.public_key.to_hex()
            public_key = b64encode(public_key.encode()).decode()

        self.private_key = private_key
        self.public_key = public_key

    def encrypt(self, message: str) -> str:
        """
        Method to encrypt a raw message.
        :param message: Raw message data.
        :return: Cyphered data in Base64 format.
        """
        if not self.public_key:
            raise Exception("Can't encrypt your data, 'public_key' is not defined.")

        key = b64decode(self.public_key.encode())
        key = key.decode()

        encrypted = encrypt(key, message.encode('UTF-8'))

        return b64encode(encrypted).decode('UTF-8')

    def decrypt(self, message: str) -> str:
        """
        Method to decrypt message in the EC Integrated schema
        :param message: Cyphered string data in Base64 format.
        :return: Raw string with deciphered data.
        """
        if not self.private_key:
            raise Exception("Can't decrypt your data, 'private_key' is not defined.")

        key = b64decode(self.private_key.encode())
        key = key.decode()

        data = b64decode(message.encode('UTF-8'))

        decrypted = decrypt(key, data)

        return decrypted.decode('UTF-8')

    def get_key(self) -> PrivateKey:
        return self.eth_key if self.eth_key else None

    def get_public_key(self) -> str:
        return self.public_key

    def get_private_key(self) -> str:
        return self.private_key


class Ecies:
    """
    Adaptation to ECIES, a public-key authenticated encryption scheme to implement in Python3 projects.
    Require a library eciespy and key pair generated and parsed to Base64 as a priori.
    """

    def __init__(self, private_key: str = '', public_key: str = ''):
        """
        Constructor
        :param private_key: ECIES private key in Base64.
        :param public_key: ECIES public key in Base64.
        """

        if not private_key and not public_key:
            self.eth_key = generate_key()

            private_key = self.eth_key.to_hex()
            private_key = b64encode(private_key.encode()).decode()

            public_key = self.eth_key.public_key.format().hex()
            public_key = b64encode(public_key.encode()).decode()

        self.private_key = private_key
        self.public_key = public_key

    def encrypt(self, message: str) -> str:
        """
        Method to encrypt a raw message.
        :param message: Raw message data.
        :return: Cyphered data in Base64 format.
        """
        if not self.public_key:
            raise Exception("Can't encrypt your data, 'public_key' is not defined.")

        key = b64decode(self.public_key.encode())
        key = key.decode()

        encrypted = encrypt(key, message.encode('UTF-8'))

        return b64encode(encrypted).decode('UTF-8')

    def decrypt(self, message: str) -> str:
        """
        Method to decrypt message in the EC Integrated schema
        :param message: Cyphered string data in Base64 format.
        :return: Raw string with deciphered data.
        """
        if not self.private_key:
            raise Exception("Can't decrypt your data, 'private_key' is not defined.")

        key = b64decode(self.private_key.encode())
        key = key.decode()

        data = b64decode(message.encode('UTF-8'))

        decrypted = decrypt(key, data)

        return decrypted.decode('UTF-8')

    def get_key(self) -> PrivateKey:
        return self.eth_key if self.eth_key else None

    def get_public_key(self) -> str:
        return self.public_key

    def get_private_key(self) -> str:
        return self.private_key