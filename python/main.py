from cypher import AESCipher
import base64

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



if __name__ == '__main__':
    unittest.main()
