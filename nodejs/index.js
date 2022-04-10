import { ECIES } from './ecies.js';


function test() {
    const private_key = "MDllOTFkYjMxZTNiNTYwMzdkOTVlOGQxYmEyYjQ3NzhjN2M5MGNlODE4YWI0MDE4NWE2YTZiNTQ1MTRmOGM1Zg=="
    const public_key = "MDIzN2E0M2RhYWJiZDJjMjJhZmVjYzE3ZWU3MDkxMDQ1ZDU1YzBkODg2ODIxYmYwMTA0YjEyM2Y0ZmRlZWMyMjc5"
    // const ecies = new ECIES(private_key, public_key);
    const ecies = new ECIES();

    const message = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza. -Paul Leary";

    let msg_encrypted = ecies.encrypt(message);
    console.log(`Encrypted Message: ${msg_encrypted}`);

    let msg_decrypted = ecies.decrypt(msg_encrypted);
    console.log(`Decrypted Message: ${msg_decrypted}`);

    const data = "BD2NPMycdxfE2hJB5jyG6ozs7MHOA0hQrsrEeq5hnLs9PkZmNQE46BAzrO2dUZ0ecKsT2rB6PZo6jzIEU2b0kimhyV29eE6y0E4" +
        "hVbdq14RwVXjnAhSODN8ZC5RBxsjp31ivqH0zAKHMpfHRiPkBBPgVr1gPurSvkkNMknXUtYtPBxbQc9IHpIlZe8YQWX105obraACxDOoCHV2" +
        "I1kWUiuxlABI1knO0pD1e9mNwmdgkq5YhJApVKKVX4WUcGrfVHNnvdRTkBXCf";

    let data_dec = ecies.decrypt(data);
    console.log(`Decrypted Message: ${data_dec}`);
}


(() => {
  test();
})();
