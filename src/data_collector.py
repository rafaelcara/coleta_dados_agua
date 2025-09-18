from src.tools import (
    coletar_links,
    filtrar_links,
    save_file,
    save_pkl,
    create_file,
    list_files,
    read_pkl,
)
from src.config import DOWNLOAD


def save_files(files, saved_files, limit):
    for item in files:
        name, url = item
        if limit <= 0:
            break
        if name not in saved_files:
            save_file(url)
            limit -= 1


            

def collect_data(use_pkl, limit):
    if use_pkl.upper() == "N":
        print("Not PKL")
        links = coletar_links()
        links_filtrados = filtrar_links(links, regra=".xls")
        save_pkl(links_filtrados)
    else:
        links_filtrados = read_pkl()
    print(links_filtrados)
    files = create_file(links_filtrados)
    list_saved_files = list_files(DOWNLOAD)
    save_files(files, list_saved_files, limit)

