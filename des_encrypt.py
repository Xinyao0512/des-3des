from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import base64

key = b'8bytekey'  # 必须是8字节
iv = b'12345678'   # 初始向量，也是8字节
data = "信息安全导论课程"

# 转换为字节并填充
data_bytes = data.encode('utf-8')
padded_data = pad(data_bytes, DES.block_size)

# 创建加密器并加密
cipher = DES.new(key, DES.MODE_CBC, iv)
cipher_text = cipher.encrypt(padded_data)

# 输出Base64编码结果
print("加密结果（Base64）：", base64.b64encode(cipher_text).decode())
