from cipher.ecies import ECIES
from utils.utils import diff_time


@diff_time
def demo_i():
    message = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza. -Paul Leary"

    private = "MHhjNWU3ZmY5ZDE1NDdmMTNkMmE2YmY5NGViZGYyNzY4MGNkYTk3NGUwNGUzNzI0MTE1ZGMxZjYzMGFhYWY5M2E0"
    # private = "MDIxMDc3ZWU4YTA5NDk4N2M2YTc4NGY2MjE3ZTkwNGY3YjI5YWMyMzk1MDRkNmIzYmYxYjI2ZTNhNDFjZjYxMA=="
    print(f"key_private: {private}")

    public = "MHhlN2UyYmUwYWUwNGZkOTk5ZDE1NjBhZjQ3NWU1OTAyOWYzZDJlOTM2MzYxZTZiZDA1ZWZiZGVmYzg0MjRkM2YxZjhjODE0ZDZkZjYxMThhN2NkNWM2ODg5YWI3YmFhYzc2MDViMDhhYmJlODhjYzkyNGVhYzllYWU1ZmU0MGUxZA=="
    print(f"key_public: {public}")

    ecies = ECIES(private, public)
    message_enc = "BGDlAFstEpGVkpuo9U8qX1VGzSkPmqd35m7L6dEjxaxkrB8hXD5L5gtcNqO" \
                  "s6ONWaaYF5Ui+7gVjV5FJnCsW+Bh4ZaVffLZTKdQVZ0vOLjsa04vAo2sWny" \
                  "iVExyQWAlndQ7uDZtT5lowp4wsk3MKFF6WJUkGaAlae5gtT4+HiJqIuROP7" \
                  "PDW7xb9Av52GwzX/jCNDIqr2YbwGP/rONNDNw2uHxVZ7NPpVTu3I1ge4Qw8" \
                  "G489CRdvh1JOTryhSiIGOx124e+lCq40"

    decrypt_data = ecies.decrypt(message_enc)
    print(f"Decrypt message: '{decrypt_data}'")


@diff_time
def demo_ii():
    message = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza. -Paul Leary"
    private = "MDllOTFkYjMxZTNiNTYwMzdkOTVlOGQxYmEyYjQ3NzhjN2M5MGNlODE4YWI0MDE4NWE2YTZiNTQ1MTRmOGM1Zg=="
    public = "MDIzN2E0M2RhYWJiZDJjMjJhZmVjYzE3ZWU3MDkxMDQ1ZDU1YzBkODg2ODIxYmYwMTA0YjEyM2Y0ZmRlZWMyMjc5"

    data = "BD2NPMycdxfE2hJB5jyG6ozs7MHOA0hQrsrEeq5hnLs9PkZmNQE46BAzrO2dUZ0ecKsT2rB6PZo6jzIEU2b0kimhyV29eE6y0E4hVbdq1" \
           "4RwVXjnAhSODN8ZC5RBxsjp31ivqH0zAKHMpfHRiPkBBPgVr1gPurSvkkNMknXUtYtPBxbQc9IHpIlZe8YQWX105obraACxDOoCHV2I1k" \
           "WUiuxlABI1knO0pD1e9mNwmdgkq5YhJApVKKVX4WUcGrfVHNnvdRTkBXCf"

    ecies = ECIES(private_key=private, public_key=public)
    # print(f"PrivateKey: {e.get_private_key()}")
    # print(f" PublicKey: {e.get_public_key()}")

    message_enc = ecies.encrypt(message)
    print(f"Encrypted: {message_enc}")

    message_dec = ecies.decrypt(message_enc)
    print(f"Decrypted: {message_dec}")


if __name__ == '__main__':
    # demo_i()
    demo_ii()
