import { generatePrivate, getPublic, encrypt, decrypt } from "eccrypto";

// let privateKeyA = generatePrivate();
// console.log(`privateKeyA: ${privateKeyA}`);
// console.log(`privateKeyA: ${privateKeyA.toString()}`);
//
// let publicKeyA = getPublic(privateKeyA);
// console.log(`publicKeyA: ${publicKeyA}`);
//
// let privateKeyB = generatePrivate();
// console.log(`privateKeyB: ${privateKeyB}`);
//
// let publicKeyB = getPublic(privateKeyB);
// console.log(`publicKeyB: ${publicKeyB}`);
//
//
// // Encrypting the message for B.
// encrypt(publicKeyB, Buffer.from("msg to b")).then(function(encrypted) {
//     // B decrypting the message.
//     decrypt(privateKeyB, encrypted).then(function(plaintext) {
//         console.log("Message to part B:", plaintext.toString());
//     });
// });
//
// // Encrypting the message for A.
// encrypt(publicKeyA, Buffer.from("msg to a")).then(function(encrypted) {
//     // A decrypting the message.
//     decrypt(privateKeyA, encrypted).then(function(plaintext) {
//         console.log("Message to part A:", plaintext.toString());
//     });
// });


function test_i() {
    // const key_private = "MHhjNWU3ZmY5ZDE1NDdmMTNkMmE2YmY5NGViZGYyNzY4MGNkYTk3NGUwNGUzNzI0MTE1ZGMxZjYzMGFhYWY5M2E0";
    // const key_public = "MHhlN2UyYmUwYWUwNGZkOTk5ZDE1NjBhZjQ3NWU1OTAyOWYzZDJlOTM2MzYxZTZiZDA1ZWZiZGVmYzg0MjRkM2YxZjhjODE0ZDZkZjYxMThhN2NkNWM2ODg5YWI3YmFhYzc2MDViMDhhYmJlODhjYzkyNGVhYzllYWU1ZmU0MGUxZA==";
    // const message = " BGDlAFstEpGVkpuo9U8qX1VGzSkPmqd35m7L6dEjxaxkrB8hXD5L5gtcNqOs6ONWaaYF5Ui+7gVjV5FJnCsW+Bh4ZaVffLZTKdQVZ0vOLjsa04vAo2sWnyiVExyQWAlndQ7uDZtT5lowp4wsk3MKFF6WJUkGaAlae5gtT4+HiJqIuROP7PDW7xb9Av52GwzX/jCNDIqr2YbwGP/rONNDNw2uHxVZ7NPpVTu3I1ge4Qw8G489CRdvh1JOTryhSiIGOx124e+lCq40";

    const private_key = "MDllOTFkYjMxZTNiNTYwMzdkOTVlOGQxYmEyYjQ3NzhjN2M5MGNlODE4YWI0MDE4NWE2YTZiNTQ1MTRmOGM1Zg==";
    const public_key = "MDIzN2E0M2RhYWJiZDJjMjJhZmVjYzE3ZWU3MDkxMDQ1ZDU1YzBkODg2ODIxYmYwMTA0YjEyM2Y0ZmRlZWMyMjc5";

    const message_secret = "BL+Fu87LUFBe3X/QJck3kN291VbEI9MmR3xAtIuu3qinDzTy2j7lpoK+pgMkS2zg6LYW8PCHaZokGGLBxc4UxG2" +
                           "EVNb4VNrCR+M2Oh6aY1yuAWMA6WVV0oVPWNcjKU22+GStHTEdRcA=";

    // let msg = "Alexxändr Núñez Göebèlsáê";
    // let msg_b = Buffer.from(msg, "utf-8").base64Slice();
    // console.log(`msg_b: '${msg_b}'`);

    // let data = Buffer.from(msg_b, "base64").toString('utf-8');
    // console.log(`data: '${data}'`);
    // let public_key;
    try {
        //public_key = getPublic(Buffer.from(key_public));
    } catch (e) {
        console.log(e);
    }
    let data = decrypt(public_key).then(function(message) {
        console.log(`message: ${message}`);
    }).catch(function (error) {
        console.log(`error: ${error}`);
    });

    console.log(`data: ${data}`);

}


function test_ii() {
    const private_key = "MDllOTFkYjMxZTNiNTYwMzdkOTVlOGQxYmEyYjQ3NzhjN2M5MGNlODE4YWI0MDE4NWE2YTZiNTQ1MTRmOGM1Zg==";
    const public_key = "MDIzN2E0M2RhYWJiZDJjMjJhZmVjYzE3ZWU3MDkxMDQ1ZDU1YzBkODg2ODIxYmYwMTA0YjEyM2Y0ZmRlZWMyMjc5";

    const message_enc = "BD2NPMycdxfE2hJB5jyG6ozs7MHOA0hQrsrEeq5hnLs9PkZmNQE46BAzrO2dUZ0ecKsT2rB6PZo6jzIEU2b0kimhyV29" +
                        "eE6y0E4hVbdq14RwVXjnAhSODN8ZC5RBxsjp31ivqH0zAKHMpfHRiPkBBPgVr1gPurSvkkNMknXUtYtPBxbQc9IHpIlZ" +
                        "e8YQWX105obraACxDOoCHV2I1kWUiuxlABI1knO0pD1e9mNwmdgkq5YhJApVKKVX4WUcGrfVHNnvdRTkBXCf";


    let x;
    try{
        x = decrypt(private_key, message_enc);
    } catch (e) {
        console.log(e);
    }

    x.then((plaintext) => {
        console.log("Decrypted message: ", plaintext.toString());
    }).catch((result) => {
        console.log("Error: ", result);
    });

}


(() => {
    // test_i();
    test_ii();
})();
