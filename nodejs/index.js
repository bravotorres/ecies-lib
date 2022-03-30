import { generatePrivate, getPublic, encrypt, decrypt } from "eccrypto";

let privateKeyA = generatePrivate();
let publicKeyA = getPublic(privateKeyA);
let privateKeyB = generatePrivate();
let publicKeyB = getPublic(privateKeyB);

const message_a = "Lorem ipsum";

// Encrypting the message for B.
encrypt(publicKeyB, Buffer.from(message_a)).then(function(encrypted) {
    // B decrypting the message.
    console.log(`ecrypted: ${encrypted}`);
    // console.log(`ecrypted: ${Buffer.from(encrypted.ciphertext).toString('base64')}`);
    decrypt(privateKeyB, encrypted).then(function(plaintext) {
        console.log("Message to part B:", plaintext.toString());
    });
});

// Encrypting the message for A.
encrypt(publicKeyA, Buffer.from("msg to a")).then(function(encrypted) {
    // A decrypting the message.
    console.log(`ecrypted: ${encrypted}`);
    decrypt(privateKeyA, encrypted).then(function(plaintext) {
        console.log("Message to part A:", plaintext.toString());
    });
});

