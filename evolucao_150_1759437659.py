# Legado de Prometheus (Geração 1)\n# Meta: "Otimizar estruturas de dados para melhorar a leitura e escrita de grandes conjuntos de dados em Python".\n\n```
import collections

class DataProcessor:
    def __init__(self):
        self.data_structures = collections.defaultdict(list)

    def processar(self, data):
        for item in data:
            if isinstance(item, dict):  # processa dicionários
                self.processar_dict(item)
            else:  # processa outros tipos de dados
                self.data_structures[0].append(item)

    def processar_dict(self, dictionary):
        for key, value in dictionary.items():
            if isinstance(value, list) or isinstance(value, dict):  # processa dicionários e listas
                self.processar(value)
            else:  # processa outros tipos de dados
                self.data_structures[0].append((key, value))

    def get_data_structures(self):
        return self.data_structures

def main():
    processor = DataProcessor()
    data = [...]  # lista de dados a ser processada
    processor.processar(data)
    processed_data = processor.get_data_structures()

# Executar o código principal
if __name__ == "__main__":
    main()
```