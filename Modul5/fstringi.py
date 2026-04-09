# ==============================
# 📌 ŚCIĄGAWA – FORMATOWANIE (f-string)
# ==============================

# 🔢 LICZBY CAŁKOWITE
x = 5
print(f"{x}")        # 5
print(f"{x:02d}")    # 05  -> 2 cyfry, zera z przodu
print(f"{x:05d}")    # 00005


# 🔢 LICZBY FLOAT
pi = 3.14159
print(f"{pi:.2f}")   # 3.14  -> 2 miejsca po przecinku
print(f"{pi:.4f}")   # 3.1416
print(f"{pi:10.2f}") # '      3.14' -> szerokość 10


# 📊 WYRÓWNANIE TEKSTU
text = "Hi"
print(f"{text:>10}")  # '        Hi' -> do prawej
print(f"{text:<10}")  # 'Hi        ' -> do lewej
print(f"{text:^10}")  # '    Hi    ' -> środek


# 🔣 WYPEŁNIANIE
print(f"{text:*^10}") # '****Hi****'


# 💰 SEPARATOR TYSIĘCY
num = 1000000
print(f"{num:,}")     # 1,000,000


# 📉 PROCENTY
p = 0.756
print(f"{p:.2%}")     # 75.60%


# 🔡 TEKST
name = "jan kowalski"
print(f"{name.title()}") # Jan Kowalski
print(f"{name.upper()}") # JAN KOWALSKI
print(f"{name.lower()}") # jan kowalski


# 🎬 TWÓJ PRZYKŁAD (serial)
season = 1
episode = 5
print(f"S{season:02d}E{episode:02d}")  # S01E05


# ==============================
# 🧠 TL;DR
# ==============================
# :02d  -> liczba, 2 cyfry, zera z przodu
# :.2f  -> 2 miejsca po przecinku
# :>10  -> do prawej
# :<10  -> do lewej
# :^10  -> wyśrodkowanie