import { encrypt, decrypt } from 'eciesjs';


/**
 * @name ECIES
 * @description Adaptation to ECIES, a public-key authenticated encryption scheme to implement 
 * in Javascript or TypeScript projects. Require a library 'eciesjs' and key pair generated and 
 * parsed to Base64 as a priori.
 * 
 * @author 'Sistemas B.I.G, Captación' by Alejandro Bravo <alejandro.bravo@bancoazteca.com.mx>
 */
class ECIES {
    private_key;
    public_key;

    /**
     * @name constructor
     * @description Random hashing algorithm I found on Stack Overflow.
     * @param {private_key} ECIES private key in Base64. 
     * @param {public_key} ECIES public key in Base64.
     */
    constructor(private_key = '', public_key = '') {
        this.private_key = private_key;
        this.public_key = public_key;
    }

    /**
     * @name encrypt
     * @description Method to encrypt a raw message.
     * @param {message} Raw message data.
     * 
     * @returns {string} Cyphered data in Base64 format.
     */
    encrypt(message = '') {
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

    /**
     * @name decrypt
     * @description Method to decrypt message in the EC Integrated schema
     * @param {data} Cyphered string data in Base64 format.
     * 
     * @returns {string} Raw string with deciphered UTF-8 data.
     */
    decrypt(data) {
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

    /**
     * @name getKeyPair
     * @description Simply get the Key pair to encrypt/decrypt (to debug)
     * 
     * @returns {object} Key pair in simple Base64 format.
     */
    getKeyPair() {
        return {
            "private_key": this.private_key,
            "public_key": this.public_key
        };
    }
}


export { ECIES };
