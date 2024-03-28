# ECIES integration module for Python
Adecuation to include a ECIES system for encrypt y decrypt the transission of sensible data with 
finality of increment security, and performance, in uServices and APIs.

## Formats
The Keys, public & private, are generated as a array of bytes in the backend and exposed to the 
clients as a one of two crossed pairs in Hex representation and Base64 string format. 
Similarly, encrypted strings are transmitted in the request body as binary Base64 strings.

## Project
The projecs is initially conceived as a independent node module to describe and test the function, 
but the principal component to encrypt/decrypt with the provided keys is a class `ECIES` in 
`python/cipher/ecies.py` file.


### Dependencies
- `python3>=3.8.X`

Main dependency:
- `eciespy`

All dependencies are detailed in `requirements.txt`

### Test
Now, as a simple test you can run in a virtual environment:

```shell
$ python -m  venv venv
$ source venv/bin/activate
(venv) $ pip install pip -U
(venv) $ pip install -r requirements.txt
(venv) $ python main.py
```

Tested in
- OpenSUSE Leap 15.5 x64, with `python==3.9.17`
- Fedora 35 x64, with `python==3.9.9`
- Windows 10 x64, with `python==3.9.9`
- Windows 11 x64, with `python==3.9.17`


##### ToD's: 
- Formalize Unit Tests.
- Package as a _static_ class or template, maybe as a decorator or datatype.
