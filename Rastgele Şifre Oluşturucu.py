import random
import string

def generate_password(length=12, complexity='medium'):
    if complexity == 'easy':
        characters = string.ascii_letters + string.digits
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == 'hard':
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Şifre güçlüğü seviyesini seçin:")
    print("1. Kolay (Sadece harf ve rakamlar)")
    print("2. Orta (Harf, rakam ve özel karakterler)")
    print("3. Zor (Uzunlukları ve karmaşıklığı arttırılmış şifreler)")

    choice = input("Seçiminizi yapın (1/2/3): ")

    if choice == '1':
        complexity_level = 'easy'
    elif choice == '2':
        complexity_level = 'medium'
    elif choice == '3':
        complexity_level = 'hard'
    else:
        print("Geçersiz seçim! Orta (2) seviyesi kullanılacak.")
        complexity_level = 'medium'

    password_length = int(input("Şifrenin uzunluğunu belirleyin: "))
    random_password = generate_password(password_length, complexity_level)
    print("Oluşturulan şifre:", random_password)
