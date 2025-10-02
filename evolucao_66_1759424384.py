# Legado de Prometheus (Geração 1)\n# Meta: Melhorar a compreensão do perfil de uso e comportamento do código para identificar oportunidades de otimização específicas e personalizar a abordagem de otimização para cada aplicação.\n\n```
import line_profiler
profiler = line_profiler.LineProfiler()

@profiler.profile
def processar():
    print('Novo processo mais eficiente!')

if __name__ == '__main__':
    profiler.enable()
    processar()
    profiler.disable()
    profiler.print_stats()
```