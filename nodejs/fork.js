// let http = require("http");

// Modified example from:
// https://github.com/bitchan/eccrypto

import { randomBytes, createHash } from "crypto";
import { getPublic, generatePrivate, encrypt, decrypt } from "eccrypto";

//=================================================
// Private Key Functions
//=================================================

// Returns private key in object, with salt and key in HEX.
function createPrivate(keyphrase, encoding) {
    let salt = randomBytes(32).toString(encoding);
    return {
        salt: salt,
        key: createHash("sha256")
            .update(keyphrase + salt.toString("hex"))
            .digest()
            .toString(encoding)
    };
    // let salt = crypto.randomBytes(32).toString("hex");
    // return {
    //   salt: salt,
    //   key: crypto
    //     .createHash("sha256")
    //     .update(keyphrase + salt)
    //     .digest()
    //     .toString("hex")
    // };
}

// Function used to recover private key by using the keyphrase and salt. Hence only need to store the salt, and not the keyphrase nor private key. Salt also ensures that keyphrase can be similar among users but private key still remains different.
// Returns private key in HEX.
function recoverPrivate(keyphrase, salt, encoding) {
    // return crypto
    //   .createHash("sha256")
    //   .update(keyphrase + salt)
    //   .digest()
    //   .toString("hex");

    return createHash("sha256")
        .update(keyphrase + salt.toString("hex"))
        .digest()
        .toString(encoding);
}

//=================================================
// Public Key Functions
//=================================================

// Generates the public key from a private key.
// Returns public key in HEX.
function get_public(privateKey, encoding) {
    // return eccrypto.getPublic(Buffer.from(privateKey, "hex")).toString("hex");
    return getPublic(Buffer.from(privateKey, encoding)).toString(encoding);
}

//=================================================
// Encryption/Decryption Utility Functions
//=================================================

// Using base64 to shorten a long hex string
// function base64decode(str) {
//   return Buffer.from(str, "base64").toString("hex");
// }

/**
 * Convert ECIES object to a concatenated string
 * @return {string} - A encrypted string of concatenated Ecies properties
 * @param buffer
 * @param encoding
 */
function encryptedBufferToString(buffer, encoding) {
    return Buffer.concat([
        buffer.iv,
        buffer.ephemPublicKey,
        buffer.ciphertext,
        buffer.mac
    ]).toString(encoding);
    // return base64encode(
    //   Buffer.concat([
    //     buffer.iv,
    //     buffer.ephemPublicKey,
    //     buffer.ciphertext,
    //     buffer.mac
    //   ]).toString(encoding)
    // );
}

/**
 * Input/output structure for ECIES operations.
 * @typedef {Object} Ecies
 * @property {Buffer} iv - Initialization vector (16 bytes)
 * @property {Buffer} ephemPublicKey - Ephemeral public key (65 bytes)
 * @property {Buffer} ciphertext - The result of encryption (variable size)
 * @property {Buffer} mac - Message authentication code (32 bytes)
 */
function encryptedStringToBuffer(encodedString, encoding) {
    // let string = base64decode(encodedString);
    let string = Buffer.from(encodedString, encoding).toString("hex");

    let result = {};
    let cipherLength = string.length - 226;
    result.iv = Buffer.from(string.slice(0, 32), "hex");
    result.ephemPublicKey = Buffer.from(string.slice(32, 162), "hex");
    result.ciphertext = Buffer.from(string.slice(162, 162 + cipherLength), "hex");
    result.mac = Buffer.from(string.slice(162 + cipherLength), "hex");
    return result;
}

//=================================================
// Encryption/Decryption Functions
//=================================================

// Returns a promise of encrypted JSON string
function encrypt_(publicKey, message, encoding) {
    // Get Buffer of public key to be used
    let publicKeyBuffer = Buffer.from(publicKey, encoding);
    let encryptedString;

    // Encrypting the message for B.
    // result is a Buffer
    //  * @property {Buffer} iv - Initialization vector (16 bytes)
    //  * @property {Buffer} ephemPublicKey - Ephemeral public key (65 bytes)
    //  * @property {Buffer} ciphertext - The result of encryption (variable size)
    //  * @property {Buffer} mac - Message authentication code (32 bytes)

    return encrypt(publicKeyBuffer, Buffer.from(message))
        .then(function(response) {
            return encryptedBufferToString(response, encoding);
        });
    // return encryptedString;
}

// Returns a promise of decrypted plain string
function decrypt_(privateKey, encryptedString, encoding) {
    // Prepare the encrypted message as Buffer to be used
    let encryptedBuffer = encryptedStringToBuffer(encryptedString, encoding);
    // console.log("Encrypted message as Buffer converted from JSON to be used for decryption:");
    // console.log(JSON.stringify(encryptedBuffer));
    // console.log();

    // Get Buffer of private key to be used
    let privateKeyBuffer = Buffer.from(privateKey, encoding);

    // B decrypting the message.
    return decrypt(privateKeyBuffer, encryptedBuffer)
        .then(function(plaintext) {
            return plaintext.toString();
        });
}

//=================================================
// MAIN: HOW TO USE?
//=================================================
const encoding = 'base64';
//=================================================
// This funciton is defined to ensure encrypt function is finished before the decrypt function is ran in the right order
//=================================================
async function runEncryptDecrypt(privateKey, publicKey, message) {
    //=================================================
    // Encrypting a message from a public key
    //=================================================
    console.log("=======================================");
    console.log("ENCRYPTING A MESSAGE");
    console.log("=======================================\n");

    console.log("MESSAGE TO BE ENCRYPTED:\n%s\n", message);

    let encryptedString = await encrypt(publicKey, message, encoding);
    console.log(`Encrypted message as ${encoding} that is sent.`);
    console.log(encryptedString);
    console.log();

    //=================================================
    // Decrypting a message from a public key
    //=================================================
    console.log("=======================================");
    console.log("DECRYPTING A MESSAGE");
    console.log("=======================================\n");

    let decryptedMessage = await decrypt(privateKey, encryptedString, encoding);
    console.log(`DECRYPTED MESSAGE: '${decryptedMessage}'`);

    console.log("DONE!");
}

//=================================================
// Main procedure
//=================================================

(() => {
    // Set encoding
    let encoding = "base64";

    console.log("=======================================");
    console.log("PRIVATE KEYS");
    console.log("=======================================\n");

    console.log("B begins by specifying a keyphrase to create a private key.\n");
    let keyphrase = "secretmessage";
    // let salt = crypto.randomBytes(32).toString('hex');
    // let privateKeyB = crypto.createHash("sha256").update(keyphrase+salt).digest();

    let private_k = createPrivate(keyphrase, encoding);
    let salt = private_k.salt;

    console.log("B's keyphrase: %s\n", keyphrase);
    console.log("B's salt:\n%s\n", salt);

    // Store private key in HEX
    console.log(
        "Generate and store B's private key as %s:\n%s\n",
        encoding,
        private_k.key
    );

    // Convert private key from HEX to Buffer to be used
    let privateKeyBufferB = Buffer.from(private_k.key, encoding);
    console.log("Convert B's private key to Buffer to be used:");
    console.log(privateKeyBufferB);
    console.log();

    // Recovering a private key with keyphrase and salt
    console.log("Recover private key with keyphrase and salt:");
    let keyRecovered = recoverPrivate(keyphrase, salt, encoding);
    console.log("Recovered B's private key: \n%s\n", keyRecovered);

    console.log("=======================================");
    console.log("PUBLIC KEYS");
    console.log("=======================================\n");

    // Generate public key from the private key
    let publicKeyHexB = get_public(private_k.key, encoding);
    console.log(
        "Generate and store B's public key as %s:\n%s\n",
        encoding,
        publicKeyHexB
    );

    // Convert to Buffer
    let publicKeyB = Buffer.from(publicKeyHexB, encoding);
    console.log("Convert B's public key to Buffer to be used:");
    console.log(publicKeyB);
    console.log();

    // Executing the test
    let message = "love joy peace patience kindness goodness longsuffering gentleness faith modesty continence chastity";
    runEncryptDecrypt(private_k.key, publicKeyHexB, message);

    //create a server object:
    // http.createServer(async function(req, res) {
    //         res.write("=======================================\n"); //write a response to the client
    //         res.write("PRIVATE KEYS\n"); //write a response to the client
    //         res.write("=======================================\n\n"); //write a response to the client
    //
    //         let keyphrase = "secretmessage";
    //
    //         res.write(
    //             "B begins by specifying a keyphrase to create a private key.\n\n"
    //         ); //write a response to the client
    //
    //         let private = createPrivate(keyphrase, encoding);
    //         let salt = private.salt;
    //
    //         res.write("B's keyphrase: " + keyphrase + "\n\n");
    //         res.write("B's salt: " + salt + "\n\n");
    //
    //         // Store private key in HEX
    //         res.write(
    //             "Generate and store B's private key as " +
    //             encoding +
    //             ":\n" +
    //             private.key +
    //             "\n\n"
    //         );
    //
    //         // Convert private key from HEX to Buffer to be used
    //         let privateKeyBufferB = Buffer.from(private.key, encoding);
    //         res.write("Convert B's private key to Buffer to be used:\n");
    //         res.write(JSON.stringify(privateKeyBufferB) + "\n\n");
    //
    //         // Recovering a private key with keyphrase and salt
    //         res.write("Recover private key with keyphrase and salt:\n");
    //         let keyRecovered = recoverPrivate(keyphrase, salt, encoding);
    //         res.write("Recovered B's private key:\n", keyRecovered);
    //         res.write(keyRecovered + "\n\n");
    //
    //         res.write("=======================================\n"); //write a response to the client
    //         res.write("PUBLIC KEYS\n"); //write a response to the client
    //         res.write("=======================================\n\n"); //write a response to the client
    //         // Generate public key from the private key
    //         let publicKeyHexB = getPublic(private.key, encoding);
    //         res.write(
    //             "Generate and store B's public key as " +
    //             encoding +
    //             ": " +
    //             publicKeyHexB +
    //             "\n\n"
    //         );
    //
    //         // Convert to Buffer
    //         let publicKeyB = Buffer.from(publicKeyHexB, encoding);
    //         res.write("Convert B's public key to Buffer to be used:\n");
    //         res.write(JSON.stringify(publicKeyB) + "\n\n");
    //
    //         let message =
    //             "love joy peace patience kindness goodness longsuffering gentleness faith modesty continence chastity";
    //
    //         res.write("=======================================\n"); //write a response to the client
    //         res.write("ENCRYPTING A MESSAGE\n"); //write a response to the client
    //         res.write("=======================================\n\n"); //write a response to the client
    //
    //         res.write("MESSAGE TO BE ENCRYPTED:\n" + message + "\n\n"); //write a response to the client
    //
    //         let encryptedString = await encrypt(publicKeyHexB, message, encoding);
    //         res.write("Encrypted message as " + encoding);
    //         res.write(" that is sent:\n");
    //         res.write(encryptedString + "\n\n");
    //
    //         res.write("=======================================\n"); //write a response to the client
    //         res.write("DECRYPTING A MESSAGE\n"); //write a response to the client
    //         res.write("=======================================\n\n"); //write a response to the client
    //
    //         let decryptedMessage = await decrypt(
    //             private.key,
    //             encryptedString,
    //             encoding
    //         );
    //         res.write("DECRYPTED MESSAGE:\n" + decryptedMessage + "\n\n"); //write a response to the client
    //
    //         res.write("DONE!\n\n"); //write a response to the client
    //
    //         res.end(); //end the response
    //     })
    //     .listen(8080); //the server object listens on port 8080
})();