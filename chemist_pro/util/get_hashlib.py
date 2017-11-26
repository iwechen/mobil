from hashlib import sha1
import bcrypt

def get_hash(str):
    sh = sha1()
    sh.update(str.encode('utf8'))
    return sh.hexdigest()


def put_bcrypt(pwd):
    # 1.将密码字符串转换成字节数组
    bytes_pwd = bytes(pwd,encoding='utf8')
    # 2.对pwd进行12轮加密，获得加密后的字符串
    hashed = bcrypt.hashpw(bytes_pwd,bcrypt.gensalt(12))
    # print(hashed)
    return hashed

    
    # print(len(hashed))

def get_bcrypt(pwd):

    bytes_pwd = bytes(pwd,encoding='utf8')
    # hashed = bcrypt.hashpw(bytes_pwd,bcrypt.gensalt(12))
    hashed = b'$2b$12$FXDTxUNOjM6DkCLNxfzHT.RBUW/znJGCVMsBj4bkOgvsoEf42HA0.'
    if bcrypt.hashpw(bytes_pwd,hashed) == hashed:
        print("ok")
    else:
        print("no")

# if __name__ == '__main__':
#     a = input("--------------->>>")
#     hashed = put_bcrypt(a)
#     get_bcrypt(a)

