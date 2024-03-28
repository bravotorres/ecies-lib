package com.security;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.security.ecies.ECIES;


public class Application {
    private static final Logger logger = LoggerFactory.getLogger(Application.class);
    
    public static void main(String[] args) {
        try {
            String privateKeyA = "MjNmZGNiZTgwNDBhNDY4ZDNkZmY1ZjYxM2RjMDYxNzFiNmIyNjEyMjE4NDA5ODg1NzY2MWZjMzA1NWE5MmU2Zg==";
            String publicKeyA = "MDIyOWUyNTM4MjAyYWRiMTI0YjZkNmI1NjY5YTg2ZmY4NjI5ZjdiZWYyZDU0MmUxMmExMDA1Yzk2MDAxZWFiYmNh";
        
            String privateKeyB = "YzdhODdlYWU1ZDBmOGQ0OGY4Njg3MDYzZDU1NGRkZDM0YjMzYjJjODkzYmQ2MThiYTljOTFhOGRiZmY5NTJkNA==";
            String publicKeyB = "MDMzZTc3N2M1YzkwODFmNGM0YzNlNmE4MDdkM2VlMTZlZmJiZjQ0MGE3MTQwOWQ1OTY3YmIzYWRhMmJlYWZhYTI5";
        
            String message = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza. -Paul Leary";
            
            
            String encryptedA = ECIES.encrypt(publicKeyA, message);
            logger.info("encryptedA: {}", encryptedA);
            
            String decryptedA = ECIES.decrypt(privateKeyA, encryptedA);
            logger.info("decryptedA: {}\n", decryptedA);
            
            
            String encryptedB = ECIES.encrypt(publicKeyB, message);
            logger.info("encryptedB: {}", encryptedB);
            
            String decryptedB = ECIES.decrypt(privateKeyB, encryptedB);
            logger.info("decryptedB: {}\n", decryptedB);
            
        } catch (Exception e) {
            logger.error("Error in ECIES cipher: {}", e.getMessage());
        }
    }
    

    
}
