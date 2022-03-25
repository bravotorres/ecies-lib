import base64
import re

from Crypto.Cipher import AES


class AESCipher:
    def __init__(self, key: str, iv: str):
        """
        Recibe una llave (key) en base64 ascii y un vector de inicialización.
        """
        self.key = base64.b64decode(key)
        self.iv = iv.encode()
        self.block_size = 16

    def get_padding(self, string: str):
        k = self.block_size - len(string) % self.block_size

        return f"{string}{k * chr(k)}"

    def encrypt(self, raw: str) -> str:
        try:
            generator = AES.new(self.key, AES.MODE_CBC, self.iv)

            bstring_encoded = generator.encrypt(self.get_padding(raw).encode())
            b64_string = base64.b64encode(bstring_encoded)

            return b64_string.decode()
        except Exception as e:
            print(f"Error: {e}")
            return ""

    def decrypt(self, enc: str) -> str:
        try:
            generator = AES.new(self.key, AES.MODE_CBC, self.iv)
            print(f"data: {enc}")

            enc = base64.b64decode(enc.encode('UTF-8'))
            dec_bytes = generator.decrypt(enc)

            result = re.sub('[\\x00-\\x08\\x0b-\\x0c\\x0e-\\x1f\n\r\t]', '', dec_bytes.decode())

            return result
        except Exception as e:
            print(f"Error: {e}")
            return ""
