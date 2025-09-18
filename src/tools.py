import pickle
import urllib.request
from pathlib import Path
from urllib.parse import urljoin

import wget
from bs4 import BeautifulSoup

from src.logger import logger
from src.config import BASE_URL, RELATIVE_PATH, DOWNLOAD, PKL


def get_links():
    '''
    Retorna uma lista com os links encontrados.
    '''
    FULL_URL = urljoin(BASE_URL, RELATIVE_PATH)
    with urllib.request.urlopen(FULL_URL) as response:
        soup = BeautifulSoup(response, "html.parser")
    return [a.get("href") for a in soup.find_all("a") if a.get("href")]


def filter_links_by_extension(links, extension):
    """
    Retorna uma lista com os links que contêm a extensão específicada.
    """
    return [
        urljoin(BASE_URL, link)
        for link in links
        if link and extension in link
    ]

def create_file(links):
    """
    Retorna uma lsita contendo o nome do arquivo e a URL.
    """
    return [(link.split("/")[-1], link) for link in links if link]


def save_pkl(my_list):
    with open(PKL, "wb") as file:
        pickle.dump(my_list, file)


def read_pkl():
    logger.info("Carregando .pkl")
    with open(PKL, "rb") as f:
        return pickle.load(f)
    

def save_file(url):
    wget.download(url, out=DOWNLOAD)


def list_files(directory):
    """
    Retorna uma lista com os arquivos no diretório informado.
    """
    directory = Path(directory)
    return [f for f in directory.iterdir() if f.is_file()]