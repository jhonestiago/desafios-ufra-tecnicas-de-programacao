armazenamento_total_GB:int = 8
espaco_ocupado_MB:int = 3584

espaco_ocupado_GB = espaco_ocupado_MB / 1000
espaco_disponivel_GB = armazenamento_total_GB - espaco_ocupado_GB

print(f'O pendrive ainda pode armazenar {espaco_disponivel_GB} GB.')
