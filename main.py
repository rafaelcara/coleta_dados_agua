import argparse
from src.data_collector import collect_data
from src.data_processor import process_data
from src.logger import logger


def main(use_pkl, limit):
    logger.info("Iniciando aplicação")
    data = collect_data(use_pkl, limit)
    data = process_data(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pkl", help="use pkl Y/N")
    parser.add_argument("-l", "--limit", type=int, help="limit")
    args = parser.parse_args()
    main(use_pkl=args.pkl, limit=args.limit)
