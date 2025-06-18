from pathlib import Path

def ler_arquivo(caminho: str):
    arquivos = Path(caminho).rglob('*.java')
    return [arquivo for arquivo in arquivos]

def ler_conteudo(arquivo: Path):
    with open(arquivo, 'r', encoding='utf-8') as file:
        return file.read()