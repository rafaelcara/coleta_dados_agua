import os
import pickle
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urljoin
import wget

from src.config import BASE_URL, RELATIVE_PATH, DOWNLOAD, PKL

def coletar_links():

    FULL_URL = urljoin(BASE_URL, RELATIVE_PATH)
    html_page = urllib.request.urlopen(FULL_URL)
    soup = BeautifulSoup(html_page, "html.parser")
    links = []
    for link in soup.findAll("a"):
        links.append(link.get("href"))
    return links


def filtrar_links(links, regra):
    return [urljoin(BASE_URL, link) for link in links if regra in link]

def create_file(links):
    files = []
    for link in links:
        file_name = link.split("/")[-1]
        files.append((file_name, link))
    return files


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