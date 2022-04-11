package com.bancoazteca.big.ecies;

import com.bancoazteca.big.security.utils.ECIES;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


public class EciesMain {
    private static final Logger logger = LoggerFactory.getLogger(EciesMain.class);
    
    public static void main(String[] args) {
        try {
            String privateKey = "MDllOTFkYjMxZTNiNTYwMzdkOTVlOGQxYmEyYjQ3Nzhj" +
                "N2M5MGNlODE4YWI0MDE4NWE2YTZiNTQ1MTRmOGM1Zg==";
            String publicKey = "MDIzN2E0M2RhYWJiZDJjMjJhZmVjYzE3ZWU3MDkxMDQ1Z" +
                "DU1YzBkODg2ODIxYmYwMTA0YjEyM2Y0ZmRlZWMyMjc5";

            ECIES ecies = new ECIES(privateKey, publicKey);

            String message = "Es genial trabajar con ordenadores. No discuten" +
                ", lo recuerdan todo y no se beben tu cerveza. -Paul Leary";

            String msgEncrypted = ecies.encrypt(message);
            logger.info("Message Encrypted: {}", msgEncrypted);

            String msgDecrypted = ecies.decrypt(msgEncrypted);
            logger.info("Decrypted Message: {}", msgDecrypted);

            String data = "BD2NPMycdxfE2hJB5jyG6ozs7MHOA0hQrsrEeq5hnLs9PkZmNQ" +
                "E46BAzrO2dUZ0ecKsT2rB6PZo6jzIEU2b0kimhyV29eE6y0E4hVbdq14RwVX" +
                "jnAhSODN8ZC5RBxsjp31ivqH0zAKHMpfHRiPkBBPgVr1gPurSvkkNMknXUtY" +
                "tPBxbQc9IHpIlZe8YQWX105obraACxDOoCHV2I1kWUiuxlABI1knO0pD1e9m" +
                "Nwmdgkq5YhJApVKKVX4WUcGrfVHNnvdRTkBXCf";

            String dataDecrypted = ecies.decrypt(data);
            logger.info("Decrypted data: {}", dataDecrypted);
            
        } catch (Exception e) {
            logger.error(e.getMessage());
        }
    }
}
