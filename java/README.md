# ECIES integration module for Java
Adecuation to include a ECIES system for encrypt y decrypt the transission of sensible data with 
finality of increment security, and performance, in uServices and APIs.

## Formats
The Keys, public & private, are generated as a array of bytes in the backend and exposed to the 
clients as a one of two crossed pairs in Hex representation and Base64 string format. 
Similarly, encrypted strings are transmitted in the request body as binary Base64 strings.

## Project
The projecs is initially conceived as a independent node module to describe and test the function, 
but the principal component to encrypt/decrypt with the provided keys is a class `ECIES` in 
`java/src/main/java/com/security/ecies/ECIES.java` file.


### Dependencies
- `Java Development Kit >= 21`, but is tested wit OpenJDK and Oracle JDK since version 11.
- `maven >= 3.8.X`

Main dependency: The Bouncy Castle Java APIs
- `bcpkix-jdk15on==1.70`

The Bouncy Castle Java APIs for CMS, PKCS, EAC, TSP, CMP, CRMF, OCSP, and certificate generation. 
This jar contains APIs for JDK 1.8 and up. The APIs can be used in conjunction with a JCE/JCA 
provider such as the one provided with the Bouncy Castle Cryptography APIs.
Java Cryptography Architecture (JCA) and Java Cryptography Extension (JCE).

All dependencies are detailed in `pom.xml`


### Test
Now, to see a a simple view of results you can run:

```shell
$ mvn clean install
$ java -jar target/ecies-jar-with-dependencies.jar 
```

Or simply execute the simple JUnit tests (`java/src/test/java/com/security/ApplicationTest.java`)
```shell
$ mvn test
```

Tested in
- OpenSUSE Leap 15.5 x64, with `OpenJDK 21` & `maven 3.8.8`
- Fedora 35 x64, with `OpenJDK 19` & `maven 3.8.6`
- Windows 10 x64, with `Oracle JDK 17` & `maven 3.8.2`
- Windows 11 x64, with `Open JDK 19` & `maven 3.9.2`


##### ToD's: 
- Define a own Exception types.
- Package as a _static_ class or template, maybe as a decorator or datatype.
