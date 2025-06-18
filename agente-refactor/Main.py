import LeitorArquivos as leitor

def main(): 
    arquivos = leitor.ler_arquivo("/home/victor/victor/dev/repo/eclipse/econect/Econect-AssistenteAPI/")
    
    for arquivo in arquivos:
        conteudo = leitor.ler_conteudo(arquivo)
        print(f"Conteúdo do arquivo {arquivo.name}:\n{conteudo}\n")
    
    
if __name__ == "__main__":
    main()