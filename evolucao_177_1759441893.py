# Legado de Prometheus (Geração 1)\n# Meta: Melhorar a compressão de dados para reduzir o uso de memória e melhorar o desempenho de aplicativos Python em 2024.\n\nfrom typing import Callable, Any

class Logger:
    def __init__(self):
        self.log_file = open("log.txt", "w+")

    def log(self, message: str) -> None:
        self.log_file.write(f"{message}\n")
        self.log_file.flush()

def processar(logger: Logger | None = None) -> None:
    if logger is not None:
        logger.log('código antigo')
    else:
        print('código antigo')

logger = Logger()
processar(logger)
# or
processar()