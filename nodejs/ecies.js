import { encrypt, decrypt } from 'eciesjs';


class ECIES {
  private_key;
  public_key;

  constructor(private_key = '', public_key = '') {
      this.private_key = private_key;
      this.public_key = public_key;
  }

  async encrypt(message = '') {
      try {
          if (this.public_key === '') {
              throw new Error("Can't encrypt your data, 'public_key' is not defined.");
          }
          
          let key_buffered = Buffer.from(this.public_key, 'base64').toString();
          let encrypted = encrypt(key_buffered, message);

          return Buffer.from(encrypted).toString('base64');

      } catch(e) {
          console.log(`Error: ${e}`);
          throw e;
      }
  }

  async decrypt(data) {
      try {
          if (this.private_key === '') {
              throw new Error("Can't decrypt your data, 'private_key' is not defined.");
          }
          let key_buffered = Buffer.from(this.private_key, 'base64').toString();
          let decrypted = decrypt(key_buffered, Buffer.from(data, 'base64'));

          return Buffer.from(decrypted).toString('utf-8');

      } catch(e) {
          console.log(`Error: ${e}`);
          throw e;
      }
  }

  async getKeyPair() {
      return {
          "private_key": this.private_key,
          "public_key": this.public_key
      };
  }
}

export { ECIES };
