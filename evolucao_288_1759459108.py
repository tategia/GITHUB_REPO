# Legado de Prometheus (Geração 1)\n# Meta: Melhorar a compressão de dados em Python utilizando bibliotecas como `zstd` e `lz4`.\n\n```
import zstandard as zstd
import lz4.frame

def processar():
    compressed = zstd.compress(b'código antigo')
    decompressed = zstd.decompress(compressed).decode()
    print(decompressed)

    compressed_lz4 = lz4.frame.compress(b'código antigo')
    decompressed_lz4 = lz4.frame.decompress(compressed_lz4).decode()
    print(decompressed_lz4)
```