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

    a = "MDRhNjUxNzIyZDVlNjZjZDIzOTZlN2Y2YTM0ZGUxODlhOGY3YWExOTEyYjViOTFkODQ3Y2U5NjkwM2YxYjMxYjVhNWQ3NmY3YTg4ZDA4ZjQ5OTJlZjhkMTRhZjljZmJiMDM1OTc2MDU2YTlkZGYzMTMxODM0ZjNhOGE1NmNjNzIyNmYwY2U5YjcxYzBmN2FkMDNhNTIyNDJlY2Y0NmQzMmQ3YzdjMzVjYmRkYzc2MGMyOTNmOTRiZjUwMjg3ZTcwNzQ4NDg4NTAwNDgzYzA2ZmRmYTM1NGNkY2QzODFhZDcwZjNiNTQ0NmI3NjM1M2ZkZmZlNWY2NGI1MWE1YmJmMGIzNzBmZjlhN2ExYTc5Zjg4ZDUzNzZiZTVlM2Y5MzI3ZmI1NWVkMjNhYzA5NjY0ODA2YjRiMTljNGRlM2UzODVmZGJhOTllODQ2MjUzNzEyMGI4MTNkMmFmNGJjOWU3MjM2NjU1NTA2MDBhZjgyYjYxY2E1NzA4ZTU1ZGQ4NDMwYWY0OWVhYTZjOTNlNmU2N2Zi"
    message_dec = ecies.decrypt(a)
    print(f"Decrypted: {message_dec}")


def demo_iii():
    message = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza. -Paul Leary"

    e = ECIES()

    public_key = e.get_public_key()
    print(f' String public_key = "{public_key}";')

    private_key = e.get_private_key()
    print(f' String private_key = "{private_key}";')

    encrypted = e.encrypt(message=message)
    print(f' String encrypted = "{encrypted}";')

    decrypted = e.decrypt(message=encrypted)
    print(f' String decrypted = "{decrypted}";')


if __name__ == '__main__':
    # demo_i()
    demo_ii()
    # demo_iii()
