from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
import base64

key = b'16bytekeyfor3des!'  # 16 或 24 字节
iv = b'12345678'
data = "信息安全导论课程"

data_bytes = data.encode('utf-8')
padded_data = pad(data_bytes, DES3.block_size)

cipher = DES3.new(key, DES3.MODE_CBC, iv)
cipher_text = cipher.encrypt(padded_data)

print("3DES加密结果（Base64）：", base64.b64encode(cipher_text).decode())
