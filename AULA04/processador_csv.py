import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('execucao_bot.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)


def processar_arquivo(caminho: str):
    try:
        with open(caminho, 'r') as arquivo:
            for linha in arquivo:
                logging.info(f"Linha lida: {linha}")
    except FileNotFoundError:
        logging.error(f"O arquivo {caminho} não foi encontrado")
    finally:
        logging.info("Fim da tentativa de processamento.")
