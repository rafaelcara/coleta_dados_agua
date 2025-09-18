import os
import pickle
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urljoin
import wget

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
    list_files = []
    for link in links:
        file_name = link.split("/")[-1]
        list_files.append((file_name, link))
    return list_files


def save_pkl(my_list):
    with open(PKL, "wb") as file:
        pickle.dump(my_list, file)


def read_pkl():
    with open(PKL, "rb") as f:
        return pickle.load(f)
    

def save_file(url):
    filename = wget.download(url, out=DOWNLOAD)


def list_files(directory):
    all_entries = os.listdir(directory)
    files_only = [f for f in all_entries if os.path.isfile(os.path.join(directory, f))]
    return files_only