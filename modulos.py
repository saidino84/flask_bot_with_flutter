import os


def get_current_directory(file_name):
    path = os.path.dirname(file_name)

    dados = os.listdir(path)

    return dados
