# basit_tools.py

import os

def list_files(directory):
    """
    Belirtilen dizindeki dosyaları listeler.
    """
    try:
        files = os.listdir(directory)
        for file in files:
            print(file)
    except Exception as e:
        print(f"Hata: {e}")

def create_file(file_name, content):
    """
    Belirtilen isimde bir dosya oluşturur ve içeriğini yazar.
    """
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"{file_name} adında dosya oluşturuldu.")
    except Exception as e:
        print(f"Hata: {e}")

def write_to_text_file(file_name, content):
    """
    Belirtilen isimde bir metin dosyasına içerik yazar.
    """
    try:
        with open(file_name, 'a') as file:
            file.write(content + '\n')
        print(f"{file_name} adındaki metin dosyasına yazıldı.")
    except Exception as e:
        print(f"Hata: {e}")

def delete_file(file_name):
    """
    Belirtilen isimdeki dosyayı siler.
    """
    try:
        os.remove(file_name)
        print(f"{file_name} adındaki dosya silindi.")
    except Exception as e:
        print(f"Hata: {e}")

def rename_file(old_name, new_name):
    """
    Belirtilen isimdeki dosyanın adını değiştirir.
    """
    try:
        os.rename(old_name, new_name)
        print(f"{old_name} adındaki dosyanın adı {new_name} olarak değiştirildi.")
    except Exception as e:
        print(f"Hata: {e}")

def main():
    print("1. Dosyaları Listele")
    print("2. Dosya Oluştur")
    print("3. Metin Dosyasına Yaz")
    print("4. Dosya Sil")
    print("5. Dosya İsmini Değiştir")

    choice = input("Seçiminizi yapın (1, 2, 3, 4 veya 5): ")

    if choice == '1':
        directory = input("Listelemek istediğiniz dizini girin: ")
        list_files(directory)
    elif choice == '2':
        file_name = input("Oluşturmak istediğiniz dosyanın adını girin: ")
        content = input("Dosyanın içeriğini girin: ")
        create_file(file_name, content)
    elif choice == '3':
        file_name = input("Yazmak istediğiniz metin dosyasının adını girin: ")
        content = input("Dosyaya yazmak istediğiniz içeriği girin: ")
        write_to_text_file(file_name, content)
    elif choice == '4':
        file_name = input("Silmek istediğiniz dosyanın adını girin: ")
        delete_file(file_name)
    elif choice == '5':
        old_name = input("Değiştirmek istediğiniz dosyanın adını girin: ")
        new_name = input("Yeni adı girin: ")
        rename_file(old_name, new_name)
    else:
        print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
