import { encrypt, decrypt, PrivateKey } from 'eciesjs';


const k1 = new PrivateKey();
const data = Buffer.from('this is a test');

const key_private = "MHhjNWU3ZmY5ZDE1NDdmMTNkMmE2YmY5NGViZGYyNzY4MGNkYTk3NGUwNGUzNzI0MTE1ZGMxZjYzMGFhYWY5M2E0"
const key_public = "MHhlN2UyYmUwYWUwNGZkOTk5ZDE1NjBhZjQ3NWU1OTAyOWYzZDJlOTM2MzYxZTZiZDA1ZWZiZGVmYzg0MjRkM2YxZjhjODE0ZDZkZjYxMThhN2NkNWM2ODg5YWI3YmFhYzc2MDViMDhhYmJlODhjYzkyNGVhYzllYWU1ZmU0MGUxZA=="

const message = "BGDlAFstEpGVkpuo9U8qX1VGzSkPmqd35m7L6dEjxaxkrB8hXD5L5gtcNqOs6ONWaaYF5Ui+7gVjV5FJnCsW+Bh4ZaVffLZTKdQVZ0vOLjsa04vAo2sWnyiVExyQWAlndQ7uDZtT5lowp4wsk3MKFF6WJUkGaAlae5gtT4+HiJqIuROP7PDW7xb9Av52GwzX/jCNDIqr2YbwGP/rONNDNw2uHxVZ7NPpVTu3I1ge4Qw8G489CRdvh1JOTryhSiIGOx124e+lCq40"


let message_dec = decrypt(
    key,
    message
).toString();

// decrypt(
//     k1.toHex(), 
//     encrypt(k1.publicKey.toHex(), data)
// ).toString();
// console.log('this is a test')
