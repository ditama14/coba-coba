# Program Tebak Angka
# Menerapkan: Variabel, Perulangan, Percabangan

# Variabel
angka_rahasia = 7
batas_percobaan = 3
percobaan = 0

print("Selamat datang di permainan tebak angka!")
print("Kamu punya", batas_percobaan, "kesempatan untuk menebak.\n")

# Perulangan
while percobaan < batas_percobaan:
    tebakan = int(input("Tebak angka antara 1 sampai 10: "))
    percobaan += 1

    # Percabangan
    if tebakan == angka_rahasia:
        print("Selamat! Tebakan kamu benar 🎉")
        break
    elif tebakan < angka_rahasia:
        print("Terlalu kecil!")
    else:
        print("Terlalu besar!")

    if percobaan == batas_percobaan:
        print("\nKesempatan habis! Angka rahasianya adalah", angka_rahasia)