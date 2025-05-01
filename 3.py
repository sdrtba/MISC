import struct
import binascii

in_file = "png"
out_file = "1.png"

with open(in_file, "rb") as f:
    data = bytearray(f.read())

# Проверяем сигнатуру PNG
assert data[0:8] == b"\x89PNG\r\n\x1a\n", "Не PNG или сигнатура повреждена"

# Офсет начала IHDR
ihdr_off = 8
length = struct.unpack(">I", data[ihdr_off : ihdr_off + 4])[0]
assert length == 13, "Длина IHDR отличается от 13"

# Меняем высоту (4 байта в big-endian)
width_off = ihdr_off + 4 + 4  # +4 длина, +4 «IHDR»
height_off = width_off + 4
data[height_off : height_off + 4] = struct.pack(">I", 742)

# Пересчитываем CRC блока IHDR
crc_off = ihdr_off + 4 + 4 + 13  # смещение до CRC-поля
crc_data = data[ihdr_off + 4 : crc_off]  # от «IHDR» и далее 13 байт
new_crc = binascii.crc32(crc_data) & 0xFFFFFFFF
data[crc_off : crc_off + 4] = struct.pack(">I", new_crc)

# Сохраняем результат
with open(out_file, "wb") as f:
    f.write(data)

print(f"Сохранено: {out_file}")
