
    # public static String decrypt(String cipherText, String secretKey, String Ivtoken) {
    #     SecretKey key = new SecretKeySpec(secretKey.getBytes(), "AES");
    #     AlgorithmParameterSpec iv = new IvParameterSpec(Ivtoken.getBytes());
    #     byte[] decodeBase64 = Base64.getDecoder().decode(cipherText);
    #     Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
    #     cipher.init(2, key, iv);
    #     return new String(cipher.doFinal(decodeBase64), "UTF-8");
    # }

    # public static String decryptBase64(String cipherText, String secretKey, String Ivtoken) {
    #     byte[] strKey = Base64.getEncoder().encode(secretKey.getBytes());
    #     String newKey = new String(strKey);
    #     byte[] striv = Base64.getEncoder().encode(Ivtoken.getBytes());
    #     String newiv = new String(striv);
    #     SecretKey key = new SecretKeySpec(Base64.getDecoder().decode(newKey), "AES");
    #     AlgorithmParameterSpec iv = new IvParameterSpec(Base64.getDecoder().decode(newiv));
    #     byte[] decodeBase64 = Base64.getDecoder().decode(cipherText);
    #     Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
    #     cipher.init(2, key, iv);
    #     return new String(cipher.doFinal(decodeBase64), "UTF-8");
    # }

    # public String decryptJSON(String requestJSON, String tokenH, String keyH) {
    #     try {
    #         String urlKey = "T0PS3CR3TP4SSL0L";
    #         String urlIv = "1198210240070911";
    #         String headertoken = Cifrado.decrypt(tokenH.trim(), urlKey, urlIv);
    #         String headerkey = Cifrado.decrypt(keyH.trim(), urlKey, urlIv);
    #         String key = KeyComplete(headerkey.trim());
    #         String tokenb64 = Employes(headertoken.trim());
    #         String textEncripted = requestJSON.trim();
    #         return Cifrado.decryptBase64(textEncripted, key, tokenb64);
    #     } catch (Exception e) {
    #         e.printStackTrace();
    #         return "";
    #     }
    # }



# class Cyppher():
# 	def __init__(self):
#         self.url_key = "T0PS3CR3TP4SSL0L"
#         self.url_iv = "1198210240070911"


# 	def decrypt(self, data):
        


import base64
from Crypto.Cipher import AES
import re


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

