from cipher.ecies import EciesEth, Ecies
from utils.utils import diff_time

import unittest

class TestStringMethods(unittest.TestCase):

    def test_ciphered(self):
        url_key = "T0PS3CR3TP4SSL0L"
        url_iv = "1198210240070911"
        
        message = "ov1JosKpSt58xVYzXQVPiSp1HVIEZTSqmnFrZ4EKlOzKwGTWlaier7GK6IqsdNMctV3O3O+sq6wRcwjTL2PppY2gxjdaeyR2KwxizXbr7I6eGR2NEY9Ch2g4gcQA2zOotveXyi08Qbx1/oTDgtXR16mDMZLXBmPv6RQMM2reHlhvlTN7QlN+JjpBgNgrVzOw5A1RK+cfpMv+1UgN4ntFxl9R7VZRZUcv59ynuGdx0888J+TRhX0G36Pvo6O5ENGtWSVOHswkx7hrwWF9PgWHPuMPbum6kk8oLARWKcNj7wuODurMiTY2pdyXJIPgi0ZO7cOWw+f6lZ3tSSx4aK3mxWujEndkbsWX886kesjdDjh9F/nawdi8yUhegkL7j4Hc9bLaRnaxjhulF0d3IbxSkUsq/Detc8XJZCsiggajNWGkgzBqUdjneBeu09bQWwd3CGzmWqP4VjWHT834nfOtN7cUpst+o1fhoRRsFdtcfRl+XXaQqzEpDoiDAbm2QUzBKXc76nvBW0XAIxPLm0KKHM89A9iZwSFZClTqHDLKsjLjfxpvC8Xoc3Qq6FaQKq+X9E3YAexDHflFGLAuz/Pjmp4Ie/n6zDyE2mx6Txl5wJQel+EuAk+ab/9IGYtrjlm1aN2cmWkNm56kjcqY5GZobX7I3SdtzHS3GahiDpM7EMp4riX6qF5FVHAi4FqvShHtb/bhIn12AhjpseswE6wv2JZrgXbXys2+JsyvAicZV4AVJpUwyBMD7OdjoNPRRuHfrsYmad9NDRs+9HuSM217NJUT1Cjo/0Yl0OknOK2fjFHA8xhKI74zJHNLnSHi3jmEquENYsESCmdQjGqbs/GNW/9KlDB7v6oLRRdlkt9bzU81LV7xIzG2zHyCtXp2Qh58rZSMA0UDTLoVT92KKWGgf2MAw+do9wS0VewNNtskgZPMAGKonwMLl5Ih37q8M1pYIz3UuluJw2w0/1pl1CsdP9DoPkIMylT9R2fpbob9nGTZHRx55P2qEBT/qP6PMVpqzQOIcK4A/6d01ZRiWnxJozM16WFHQKdOXxZdCwH1QHe7ki7aFg/8VpJZqYd46aywLpurz48O9kMtH5iplBQJVM74Tyh2cN1O7LXQnLn7T6EyHZTKA1uNmKJ9EldNYX3Lv1y0ylwMn3hJGu4P/Mdyhn/cMZWxXmEhmdbyObDaV0rjyqHIyQCFPfJCSwyRYiW0Sck/KKrwPzrtPCvRc/LDyxFnhx3jCtKCayNq+omPKuoFEpxwFjZhu6L7XJsTGYdc5X7x8/1hsk6OcxYEGswrygfwLRYMI74Mtc+xW1ynnEM="

        # cypher = Cypher()
        cypher = AESCipher(key=base64.b64encode(url_key.encode('UTF-8')), iv=url_iv)

        data = "{\"branch\":\"0172\",\"canal\":\"01\",\"entity\":\"0127\",\"terminal\":\"WE50\",\"user\":\"B638318\",\"zipCode\":\"20925\"}"

        # print(f"message: {data}")

        encrypted = cypher.encrypt(data)
        # print(f"encrypted: {encrypted}")

        decrypted = cypher.decrypt(message)
        # decrypted = cypher.decrypt(encrypted)
        # print(f"decrypt: {decrypted}")

        self.assertEqual(decrypted, data)


@diff_time
def test_ii():
    message = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza. -Paul Leary"

    private = "MHhjNWU3ZmY5ZDE1NDdmMTNkMmE2YmY5NGViZGYyNzY4MGNkYTk3NGUwNGUzNzI0MTE1ZGMxZjYzMGFhYWY5M2E0"
    # private = "MDIxMDc3ZWU4YTA5NDk4N2M2YTc4NGY2MjE3ZTkwNGY3YjI5YWMyMzk1MDRkNmIzYmYxYjI2ZTNhNDFjZjYxMA=="
    print(f"key_private: {private}")

    public = "MHhlN2UyYmUwYWUwNGZkOTk5ZDE1NjBhZjQ3NWU1OTAyOWYzZDJlOTM2MzYxZTZi" \
             "ZDA1ZWZiZGVmYzg0MjRkM2YxZjhjODE0ZDZkZjYxMThhN2NkNWM2ODg5YWI3YmFh" \
             "Yzc2MDViMDhhYmJlODhjYzkyNGVhYzllYWU1ZmU0MGUxZA=="
    print(f"key_public: {public}")

    ecies = EciesEth(private, public)
    message_enc = "BGDlAFstEpGVkpuo9U8qX1VGzSkPmqd35m7L6dEjxaxkrB8hXD5L5gtcNqO" \
                  "s6ONWaaYF5Ui+7gVjV5FJnCsW+Bh4ZaVffLZTKdQVZ0vOLjsa04vAo2sWny" \
                  "iVExyQWAlndQ7uDZtT5lowp4wsk3MKFF6WJUkGaAlae5gtT4+HiJqIuROP7" \
                  "PDW7xb9Av52GwzX/jCNDIqr2YbwGP/rONNDNw2uHxVZ7NPpVTu3I1ge4Qw8" \
                  "G489CRdvh1JOTryhSiIGOx124e+lCq40"

    decrypt_data = ecies.decrypt(message_enc)
    print(f"Decrypt message: '{decrypt_data}'")


def test_iii():
    private = "MDllOTFkYjMxZTNiNTYwMzdkOTVlOGQxYmEyYjQ3NzhjN2M5MGNlODE4YWI0MDE4NWE2YTZiNTQ1MTRmOGM1Zg =="
    public = "MDIzN2E0M2RhYWJiZDJjMjJhZmVjYzE3ZWU3MDkxMDQ1ZDU1YzBkODg2ODIxYmYwMTA0YjEyM2Y0ZmRlZWMyMjc5"

    data = "BL+Fu87LUFBe3X/QJck3kN291VbEI9MmR3xAtIuu3qinDzTy2j7lpoK+pgMkS2zg6LYW8PCHaZokGGLBxc4UxG2EVNb" + \
           "4VNrCR+M2Oh6aY1yuAWMA6WVV0oVPWNcjKU22+GStHTEdRcA="
    e = Ecies(private_key=private, public_key=public)
    # print(f"PrivateKey: {e.get_private_key()}")
    # print(f" PublicKey: {e.get_public_key()}")

    m = "Mensaje"
    # m_e = e.encrypt(m)
    print(f"Encrypted: {data}")

    m_d = e.decrypt(data)
    print(f"Decrypted: {m_d}")


if __name__ == '__main__':
    # test()
    # test_ii()
    test_iii()

    unittest.main()
