package com.security;


import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.security.ecies.ECIES;


public class ApplicationTest {
    private static final Logger logger = LoggerFactory.getLogger(ApplicationTest.class);

    @Test
    public void testPairA() throws Exception {
        String privateKeyA = "MjNmZGNiZTgwNDBhNDY4ZDNkZmY1ZjYxM2RjMDYxNzFiNmIyNjEyMjE4NDA5ODg1NzY2MWZjMzA1NWE5MmU2Zg==";
        String publicKeyA = "MDIyOWUyNTM4MjAyYWRiMTI0YjZkNmI1NjY5YTg2ZmY4NjI5ZjdiZWYyZDU0MmUxMmExMDA1Yzk2MDAxZWFiYmNh";

        String message = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza. -Paul Leary";

        String encryptedA = ECIES.encrypt(publicKeyA, message);
        logger.info("encryptedA: '{}'", encryptedA);

        String decryptedA = ECIES.decrypt(privateKeyA, encryptedA);
        logger.info("decryptedA: '{}'\n", decryptedA);

        Assertions.assertEquals(decryptedA, message);
    }

    @Test
    public void testPairB() throws Exception {
        String privateKeyB = "YzdhODdlYWU1ZDBmOGQ0OGY4Njg3MDYzZDU1NGRkZDM0YjMzYjJjODkzYmQ2MThiYTljOTFhOGRiZmY5NTJkNA==";
        String publicKeyB = "MDMzZTc3N2M1YzkwODFmNGM0YzNlNmE4MDdkM2VlMTZlZmJiZjQ0MGE3MTQwOWQ1OTY3YmIzYWRhMmJlYWZhYTI5";

        String message = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza. -Paul Leary";

        String encryptedB = ECIES.encrypt(publicKeyB, message);
        logger.info("encryptedB: '{}'", encryptedB);

        String decryptedB = ECIES.decrypt(privateKeyB, encryptedB);
        logger.info("decryptedB: '{}'\n", decryptedB);

        Assertions.assertEquals(decryptedB, message);
    }

    @Test
    public void fulltest() throws Exception {
        String message = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza. -Paul Leary";

        String privateKey = "MDllOTFkYjMxZTNiNTYwMzdkOTVlOGQxYmEyYjQ3NzhjN2M5MGNlODE4YWI0MDE4NWE2YTZiNTQ1MTRmOGM1Zg==";
        String publicKey = "MDIzN2E0M2RhYWJiZDJjMjJhZmVjYzE3ZWU3MDkxMDQ1ZDU1YzBkODg2ODIxYmYwMTA0YjEyM2Y0ZmRlZWMyMjc5";

        String data = "BHTWGwQYx/T6kg7qN3GzKfn9JsogcDAsDputCr626igSjlS+qlMCg9ISH8U7t/co8Ic3jHIpgpye99cV1JNfOXZmUtyya+D07oHtrOIM/GdBV5STTmViu5vgBxB2pm8Wn0iuDouwdSYk6QWOdRdOBcVugydFkD5Oit2II/jYHWEts2FvbFkAf1Zus3MQ6OhwIuhXSVllgKy3hf7VHiMB45vsKm+pIKAOvb64lapubEgNWsy9lNDJdZ+5HJqwB4nyPndc4wCId1TI";
        
        String encrypted = ECIES.encrypt(publicKey, message);
        logger.info("encrypted: '{}'", encrypted);

        String decrypted = ECIES.decrypt(privateKey, encrypted);
        logger.info("decrypted: '{}'\n", decrypted);

        String decryptedData = ECIES.decrypt(privateKey, data);
        logger.info("decryptedData: '{}'", decryptedData);
    }
}