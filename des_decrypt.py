from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
import base64

key = b'8bytekey'
iv = b'12345678'
cipher_base64 = input("请输入加密后的Base64文本：")

cipher_text = base64.b64decode(cipher_base64)
cipher = DES.new(key, DES.MODE_CBC, iv)
plain_padded = cipher.decrypt(cipher_text)
plain_text = unpad(plain_padded, DES.block_size)

print("解密结果：", plain_text.decode('utf-8'))
