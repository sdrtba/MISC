import pickle
import base64

# Создаем новый объект
new_data = {"user_id": 0, "username": "admin"}

# Сериализуем через pickle
serialized = pickle.dumps(new_data)

# Кодируем в base64
encoded = base64.b64encode(serialized)

print(encoded.decode())

# 09ny333rQSrN
