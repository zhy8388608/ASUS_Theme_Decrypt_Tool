#pip install pycryptodome

import os
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# 读取密钥和偏移量
key_base64 = 'x7QfTbkoIh7JPwStEXGI3A=='
iv_base64 = 'YXN1cyMxMjM0AAAAAAAAAA=='

# 解码Base64字符串得到二进制密钥和偏移量
key = base64.b64decode(key_base64)
iv = base64.b64decode(iv_base64)

# 输入和输出文件夹路径
input_folder = "in"
output_folder = "out"

# 确保输出文件夹存在
os.makedirs(output_folder, exist_ok=True)

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    input_file = os.path.join(input_folder, filename)
    output_file = os.path.join(output_folder, filename)

    with open(input_file, 'rb') as f_in:
        # 使用AES CBC解密算法
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # 读取加密文件内容并解密
        encrypted_data = f_in.read()
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

        # 将解密后的数据保存到输出文件中
        with open(output_file, 'wb') as f_out:
            f_out.write(decrypted_data)

    print("已解密文件:", filename)