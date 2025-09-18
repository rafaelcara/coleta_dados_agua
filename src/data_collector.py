from src.tools import (
    get_links,
    filter_links_by_extension,
    save_file,
    save_pkl,
    create_file,
    list_files,
    read_pkl,
)
from src.logger import logger
from src.config import DOWNLOAD



def save_files(files, saved_files, limit):
    """
    Faz o download do arquivo se ele ainda não foi baixado.
    """
    for name, url in files:
        if limit <= 0:
            break
        if name not in saved_files:
            save_file(url)
            limit -= 1


def collect_data(use_pkl, limit):
    if use_pkl.upper() == "N":
        logger.info("Sem uso do arquivo .pkl")
        links = get_links()
        links_filtrados = filter_links_by_extension(links, extension=".xls")
        save_pkl(links_filtrados)
    else:
        links_filtrados = read_pkl()
    files = create_file(links_filtrados)
    list_saved_files = list_files(DOWNLOAD)
    save_files(files, list_saved_files, limit)