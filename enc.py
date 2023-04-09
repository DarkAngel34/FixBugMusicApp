# pip install cryptography

import os

from cryptography.fernet import Fernet

def generate_key(path):
    key = Fernet.generate_key()
    path_to_file_key = os.path.join(path, 'key')
    with open(path_to_file_key, 'wb') as file_key:
        file_key.write(key)


def load_key(path_to_file_key):
    with open(path_to_file_key, 'rb') as file_key:
        key = file_key.read()
    return key


def encrypt(key, path_to_file_data, path_to_dir_encrypted_data):
    with open(path_to_file_data, 'rb') as file_data:
        data = file_data.read()

    f = Fernet(key)
    encrypted_data = f.encrypt(data)
    name_file_encrypted_data = f'{os.path.splitext(path_to_file_data)[0]}.dll'
    path_to_file_encrypted_data = os.path.join(path_to_dir_encrypted_data, name_file_encrypted_data)
    with open(path_to_file_encrypted_data, 'wb') as file_encrypted_data:
        file_encrypted_data.write(encrypted_data)



def dencrypt(key, path_to_file_encrypted_data, path_to_dir_dencrypted_data):
    with open(path_to_file_encrypted_data, 'rb') as file_encrypted_data:
        encrypted_data = file_encrypted_data.read()
    f = Fernet(key)
    dencrypted_data = f.decrypt(encrypted_data)
    name_file_dencrypted_data = f'{os.path.splitext(path_to_file_encrypted_data)[0]}.dec'
    path_to_file_dencrypted_data = os.path.join(path_to_dir_dencrypted_data, name_file_dencrypted_data)
    with open(path_to_file_dencrypted_data, 'wb') as file_dencrypted_data:
        file_dencrypted_data.write(dencrypted_data)


if __name__ == '__main__':
    current_path = os.path.dirname(os.path.abspath(__file__))

    generate_key(current_path)

    path_to_file_key = os.path.join(current_path, 'key')
    path_to_file_data = os.path.join(current_path, 'settingsMusicApp.txt')
    path_to_dir_encrypted_data = current_path

    key = load_key(path_to_file_key)

    encrypt(key, path_to_file_data, path_to_dir_encrypted_data)

    path_to_file_encrypted_data = os.path.join(current_path, 'settingsMusicApp.dll')
    path_to_dir_dencrypted_data = current_path


    dencrypt(key, path_to_file_encrypted_data, path_to_dir_dencrypted_data)


