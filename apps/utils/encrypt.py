import hashlib
from ATPlatform.settings import PASSWORD_STRING

def encrypt_pwd_md5(encString):
    md5 = hashlib.md5()
    md5.update(encString.encode('utf-8'))
    md5_encode_string = md5.hexdigest()
    return md5_encode_string

def encrypt_pwd_sha(encString):
    sha256 = hashlib.sha256()
    sha256.update(encString.encode('utf-8'))
    sha256_encode_string = sha256.hexdigest()
    return sha256_encode_string

# print(encrypt_pwd_md5('admin123' + PASSWORD_STRING))