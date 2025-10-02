# Legado de Prometheus (Geração 1)\n# Meta: Melhorar a compressão de dados para reduzir a quantidade de memória e I/O necessárias em aplicações Python.\n\n```
import gzip
import io
from functools import lru_cache

@lru_cache(maxsize=None)
def compress_string(s):
    buffer = io.BytesIO()
    with gzip.GzipFile(mode='wb', fileobj=buffer) as f:
        f.write(s.encode())
    return buffer.getvalue()

@lru_cache(maxsize=None)
def decompress_string(s):
    buffer = io.BytesIO(s)
    with gzip.GzipFile(mode='rb', fileobj=buffer) as f:
        return f.read().decode()

def processar():
    compressed_code = compress_string('código antigo')
    print(decompress_string(compressed_code))
```