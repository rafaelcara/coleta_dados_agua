import argparse
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


def main(use_pkl):
    if use_pkl.upper() == "N":
        print("Not PKL")
        links = coletar_links()
        links_filtrados = filtrar_links(links, regra=".xls")
        save_pkl(links_filtrados)
    else:
        links_filtrados = read_pkl()

    files = create_file(links_filtrados)
    saved_files = list_files(DOWNLOAD)

    for _file, _url in files[:4]:
        if _file not in saved_files:
            save_file(_url)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pkl", help="use pkl Y/N")
    args = parser.parse_args()
    main(use_pkl=args.pkl)
