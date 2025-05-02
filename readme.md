# 🛡️ DES / 3DES 加解密系统实现实验

本项目面向北方工业大学信息安全专业的同学，旨在帮助大家深入理解对称加密算法的工作原理，掌握 Python 中 DES 和 3DES 加解密的基本实现方法。通过编写和运行加密、解密程序，体验现代密码技术在数据安全中的核心作用。

---

## 📁 项目结构

```
├── des_encrypt.py         # DES 加密脚本
├── des_decrypt.py         # DES 解密脚本
├── des3_encrypt.py        # 3DES 加密脚本
├── des3_decrypt.py        # 3DES 解密脚本
├── requirements.txt       # Python 依赖文件
└── README.md              # 实验说明文档
```

---

## 🧰 环境依赖

请使用 Python 3.7 或以上版本，并提前安装 `pycryptodome` 加密库：

```bash
pip install -r requirements.txt
```

> ✅ 提示：运行前请确保已创建虚拟环境或使用本机支持 pip 的环境。

---

## 🔐 DES 加解密实验说明

### DES 加密（des_encrypt.py）

运行后会输出一段 Base64 编码的密文：

```bash
python des_encrypt.py
```

### DES 解密（des_decrypt.py）

粘贴加密得到的 Base64 密文，程序会输出原始明文：

```bash
python des_decrypt.py
```

---

## 🔒 3DES 加解密实验说明

### 3DES 加密（des3_encrypt.py）

```bash
python des3_encrypt.py
```

### 3DES 解密（des3_decrypt.py）

```bash
python des3_decrypt.py
```

---

## 🎯 实验目的

- 理解分组加密算法的工作流程；
- 掌握对称加密中 **密钥管理、初始向量、填充模式** 的应用；
- 体验 `CBC` 模式下的加解密操作；
- 培养独立编程实现加密功能的能力。

---

## ⚠️ 注意事项

- DES 密钥长度必须为 **8字节**；
- 3DES 密钥长度为 **16 或 24 字节**；
- 加密模式为 CBC，需指定 8 字节初始向量（IV）；
- 明文必须在加密前进行填充，解密后去除填充。

---

## 📌 教学用途说明

本项目仅用于教学演示与实验验证，实际生产环境请优先采用 **AES 等更安全的加密算法**。

---

## 👨‍🏫 致信息安全导论课程学生

本实验是密码学基础的重要实践部分，请结合课堂内容理解每一步加解密的含义，思考以下问题：
- 加密前为什么要填充？
- 初始向量的作用是什么？
- 如果密钥泄露，系统还安全吗？

你可以尝试修改密钥或 IV，观察不同加密结果，进一步加深理解。


 
 
