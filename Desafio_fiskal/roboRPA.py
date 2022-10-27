from classRobo import manipularArquivos


# Abrir / ler aquivo Excel
arquivo = manipularArquivos('arquivos\challenge.xlsx')

# Percorrer dados da planilha
arquivo.percorrer_planilha()
