# Legado de Prometheus (Geração 1)\n# Meta: Melhorar a compressão de dados utilizando técnicas como Gzip e Brotli para reduzir o tamanho dos arquivos e melhorar o desempenho da aplicação.\n\n```
import gzip
import brotli

def processar():
    compressed_code = ''
    
    with open(__file__, 'r') as file:
        code = file.read()
        
    compressed_code += 'print(gzip.compress(' + code.encode() + ').decode())\n'
    compressed_code += 'print(brotli.compress(' + code.encode() + ').decode())\n'
    
    with open(__file__, 'w') as file:
        file.write(compressed_code)
```