package com.security.ecies;


import org.bouncycastle.crypto.InvalidCipherTextException;
import org.bouncycastle.crypto.digests.SHA256Digest;
import org.bouncycastle.crypto.generators.HKDFBytesGenerator;
import org.bouncycastle.crypto.params.HKDFParameters;
import org.bouncycastle.crypto.params.KeyParameter;
import org.bouncycastle.crypto.params.ParametersWithIV;
import org.bouncycastle.jce.ECNamedCurveTable;
import org.bouncycastle.jce.interfaces.ECPrivateKey;
import org.bouncycastle.jce.interfaces.ECPublicKey;
import org.bouncycastle.jce.provider.BouncyCastleProvider;
import org.bouncycastle.jce.spec.ECNamedCurveParameterSpec;
import org.bouncycastle.jce.spec.ECNamedCurveSpec;
import org.bouncycastle.util.encoders.Hex;

import com.security.ecies.utils.AESGCMBlockCipher;
import com.security.ecies.utils.ECKeyPair;

import javax.crypto.NoSuchPaddingException;
import java.math.BigInteger;
import java.nio.charset.StandardCharsets;
import java.security.*;
import java.security.spec.ECPrivateKeySpec;
import java.security.spec.ECPublicKeySpec;
import java.security.spec.InvalidKeySpecException;
import java.util.Arrays;
import java.util.Base64;


public class ECIES {

    private static final String CURVE_NAME = "secp256k1";
    private static final int UNCOMPRESSED_PUBLIC_KEY_SIZE = 65;
    private static final int AES_IV_LENGTH = 16;
    private static final int AES_TAG_LENGTH = 16;
    private static final int AES_IV_PLUS_TAG_LENGTH = AES_IV_LENGTH + AES_TAG_LENGTH;
    private static final int SECRET_KEY_LENGTH = 32;
    private static final SecureRandom SECURE_RANDOM = new SecureRandom();

    /**
     * Generates new key pair consists of {@link ECPublicKey} and
     * {@link ECPrivateKey}
     *
     * @return new EC key pair
     */
    public static ECKeyPair generateEcKeyPair() throws Exception {
        ECNamedCurveParameterSpec ecSpec = ECNamedCurveTable.getParameterSpec(CURVE_NAME);

        KeyPairGenerator g = KeyPairGenerator.getInstance("EC", new BouncyCastleProvider());
        g.initialize(ecSpec, SECURE_RANDOM);

        KeyPair keyPair = g.generateKeyPair();

        return new ECKeyPair((ECPublicKey) keyPair.getPublic(), (ECPrivateKey) keyPair.getPrivate());
    }

    /**
     * Encrypts given message with given public key in hex
     *
     * @param publicKeyHex EC public key in hex
     * @param message      message to encrypt
     * @return encrypted message in hexadecimal representation as a base64 format
     */
    public static String encryptHex(String publicKeyB64, String message) throws Exception {
        String publicKeyHex = new String(Base64.getDecoder().decode(publicKeyB64.getBytes()));

        byte[] publicKey = Hex.decode(publicKeyHex);
        byte[] encrypt = encrypt(publicKey, message.getBytes(StandardCharsets.UTF_8));

        String encryptHex = Hex.toHexString(encrypt);
        return new String(Base64.getEncoder().encode(encryptHex.getBytes()));
    }

    /**
     * 
     * @param publicKeyB64
     * @param message      Raw string to encrypt
     * @return encrypted message as a binary array in base64 string format
     * @throws Exception
     */
    public static String encrypt(String publicKeyB64, String message) throws Exception {
        String publicKeyHex = new String(Base64.getDecoder().decode(publicKeyB64.getBytes()));

        byte[] publicKey = Hex.decode(publicKeyHex);
        byte[] encrypt = encrypt(publicKey, message.getBytes(StandardCharsets.UTF_8));

        return new String(Base64.getEncoder().encode(encrypt));
    }

    /**
     * Decrypt given cipher-text in hexadecimal representation in Base64 format with
     * given private key
     *
     * @param privateKeyHex    EC private key in hex
     * @param ciphertextHexB64 ciphered text in hexadecimal representation in base64 format
     * @return decrypted message
     */
    public static String decryptHex(String privateKeyB64, String ciphertextHexB64) throws Exception {
        String privateKeyHex = new String(Base64.getDecoder().decode(privateKeyB64.getBytes()));

        byte[] privateKey = Hex.decode(privateKeyHex);
        String ciphertext = new String(Base64.getDecoder().decode(ciphertextHexB64.getBytes()));

        byte[] cipherBytes = Hex.decode(ciphertext);

        return new String(decrypt(privateKey, cipherBytes), StandardCharsets.UTF_8);
    }

    public static String decrypt(String privateKeyB64, String ciphertextB64) throws Exception {
        String privateKeyHex = new String(Base64.getDecoder().decode(privateKeyB64.getBytes()));

        byte[] privateKey = Hex.decode(privateKeyHex);
        byte[] cipherBytes = Base64.getDecoder().decode(ciphertextB64.getBytes());

        return new String(decrypt(privateKey, cipherBytes), StandardCharsets.UTF_8);
    }

    /**
     * Encrypts given message with given public key
     *
     * @param publicKeyBytes EC public key binary
     * @param message        message to encrypt binary
     * @return encrypted message binary
     */
    public static byte[] encrypt(byte[] publicKeyBytes, byte[] message) throws Exception {
        ECNamedCurveParameterSpec ecSpec = ECNamedCurveTable.getParameterSpec(CURVE_NAME);
        KeyPair pair = generateEphemeralKey(ecSpec);

        ECPrivateKey ephemeralPrivKey = (ECPrivateKey) pair.getPrivate();
        ECPublicKey ephemeralPubKey = (ECPublicKey) pair.getPublic();

        // Generate receiver PK
        KeyFactory keyFactory = getKeyFactory();
        ECNamedCurveSpec curvedParams = new ECNamedCurveSpec(CURVE_NAME, ecSpec.getCurve(), ecSpec.getG(), ecSpec.getN());
        ECPublicKey publicKey = getEcPublicKey(curvedParams, publicKeyBytes, keyFactory);

        // Derive shared secret
        byte[] uncompressed = ephemeralPubKey.getQ().getEncoded(false);
        byte[] multiply = publicKey.getQ().multiply(ephemeralPrivKey.getD()).getEncoded(false);
        byte[] aesKey = hkdf(uncompressed, multiply);

        // AES encryption
        return aesEncrypt(message, ephemeralPubKey, aesKey);
    }

    /**
     * Decrypts given ciphertext with given private key
     *
     * @param privateKeyBytes EC private key binary
     * @param cipherBytes     cipher text binary
     * @return decrypted message binary
     */
    public static byte[] decrypt(byte[] privateKeyBytes, byte[] cipherBytes) throws Exception {
        ECNamedCurveParameterSpec ecSpec = ECNamedCurveTable.getParameterSpec(CURVE_NAME);
        KeyFactory keyFactory = getKeyFactory();
        org.bouncycastle.jce.spec.ECNamedCurveSpec curvedParams = new ECNamedCurveSpec(CURVE_NAME, ecSpec.getCurve(), ecSpec.getG(), ecSpec.getN());

        // generate receiver private key
        ECPrivateKeySpec privateKeySpec = new ECPrivateKeySpec(new BigInteger(1, privateKeyBytes), curvedParams);
        org.bouncycastle.jce.interfaces.ECPrivateKey receiverPrivKey = (ECPrivateKey) keyFactory.generatePrivate(privateKeySpec);

        // Get sender pub key
        byte[] senderPubKeyByte = Arrays.copyOf(cipherBytes, UNCOMPRESSED_PUBLIC_KEY_SIZE);
        ECPublicKey senderPubKey = getEcPublicKey(curvedParams, senderPubKeyByte, keyFactory);

        // Decapsulate
        byte[] uncompressed = senderPubKey.getQ().getEncoded(false);
        byte[] multiply = senderPubKey.getQ().multiply(receiverPrivKey.getD()).getEncoded(false);
        byte[] aesKey = hkdf(uncompressed, multiply);

        // AES decryption
        return aesDecrypt(cipherBytes, aesKey);
    }

    private static KeyFactory getKeyFactory() throws NoSuchAlgorithmException {
        return KeyFactory.getInstance("EC", new BouncyCastleProvider());
    }

    private static byte[] aesEncrypt(byte[] message, ECPublicKey ephemeralPubKey, byte[] aesKey) throws NoSuchAlgorithmException, NoSuchPaddingException, NoSuchProviderException, InvalidCipherTextException {
        AESGCMBlockCipher aesgcmBlockCipher = new AESGCMBlockCipher();
        byte[] nonce = new byte[AES_IV_LENGTH];
        SECURE_RANDOM.nextBytes(nonce);

        ParametersWithIV parametersWithIV = new ParametersWithIV(new KeyParameter(aesKey), nonce);
        aesgcmBlockCipher.init(true, parametersWithIV);

        int outputSize = aesgcmBlockCipher.getOutputSize(message.length);

        byte[] encrypted = new byte[outputSize];
        int pos = aesgcmBlockCipher.processBytes(message, 0, message.length, encrypted, 0);
        aesgcmBlockCipher.doFinal(encrypted, pos);

        byte[] tag = Arrays.copyOfRange(encrypted, encrypted.length - nonce.length, encrypted.length);
        encrypted = Arrays.copyOfRange(encrypted, 0, encrypted.length - tag.length);

        byte[] ephemeralPkUncompressed = ephemeralPubKey.getQ().getEncoded(false);
        return org.bouncycastle.util.Arrays.concatenate(ephemeralPkUncompressed, nonce, tag, encrypted);
    }

    private static KeyPair generateEphemeralKey(ECNamedCurveParameterSpec ecSpec) throws NoSuchAlgorithmException, InvalidAlgorithmParameterException {
        KeyPairGenerator g = KeyPairGenerator.getInstance("EC", new BouncyCastleProvider());
        g.initialize(ecSpec, SECURE_RANDOM);

        return g.generateKeyPair();
    }

    private static byte[] aesDecrypt(byte[] inputBytes, byte[] aesKey) throws NoSuchAlgorithmException, NoSuchPaddingException, NoSuchProviderException, InvalidCipherTextException {
        byte[] encrypted = Arrays.copyOfRange(inputBytes, UNCOMPRESSED_PUBLIC_KEY_SIZE, inputBytes.length);
        byte[] nonce = Arrays.copyOf(encrypted, AES_IV_LENGTH);
        byte[] tag = Arrays.copyOfRange(encrypted, AES_IV_LENGTH, AES_IV_PLUS_TAG_LENGTH);
        byte[] ciphered = Arrays.copyOfRange(encrypted, AES_IV_PLUS_TAG_LENGTH, encrypted.length);

        AESGCMBlockCipher aesgcmBlockCipher = new AESGCMBlockCipher();
        ParametersWithIV parametersWithIV = new ParametersWithIV(new KeyParameter(aesKey), nonce);
        aesgcmBlockCipher.init(false, parametersWithIV);

        int outputSize = aesgcmBlockCipher.getOutputSize(ciphered.length + tag.length);
        byte[] decrypted = new byte[outputSize];
        int pos = aesgcmBlockCipher.processBytes(ciphered, 0, ciphered.length, decrypted, 0);
        pos += aesgcmBlockCipher.processBytes(tag, 0, tag.length, decrypted, pos);
        aesgcmBlockCipher.doFinal(decrypted, pos);

        return decrypted;
    }

    /**
     * HKDF: HMAC Key Derivation Function
     * 
     * @param uncompressed
     * @param multiply
     * @return bytes of AES Key
     */
    private static byte[] hkdf(byte[] uncompressed, byte[] multiply) {
        byte[] master = org.bouncycastle.util.Arrays.concatenate(uncompressed, multiply);

        HKDFBytesGenerator hkdfBytesGenerator = new HKDFBytesGenerator(new SHA256Digest());
        hkdfBytesGenerator.init(new HKDFParameters(master, null, null));

        byte[] aesKey = new byte[SECRET_KEY_LENGTH];
        hkdfBytesGenerator.generateBytes(aesKey, 0, aesKey.length);

        return aesKey;
    }

    private static ECPublicKey getEcPublicKey(ECNamedCurveSpec curvedParams, byte[] senderPubKeyByte, KeyFactory keyFactory) throws InvalidKeySpecException {
        java.security.spec.ECPoint point = org.bouncycastle.jce.ECPointUtil.decodePoint(curvedParams.getCurve(), senderPubKeyByte);
        ECPublicKeySpec pubKeySpec = new ECPublicKeySpec(point, curvedParams);

        return (ECPublicKey) keyFactory.generatePublic(pubKeySpec);
    }
}
