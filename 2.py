import base64
import pickle

data = "gASVHgAAAAAAAACMAm9zlIwFcG9wZW6Uk5SMB2xzIC90bXCUhZRSlC4=="

# Декодируем base64
decoded = base64.b64decode(data)

# Десериализуем pickle
obj = pickle.loads(decoded)

print(obj)
