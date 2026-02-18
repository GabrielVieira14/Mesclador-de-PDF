import PyPDF2
import os

arquivos = 'c:/com/Mesclador_PDF/arquivos'
merger = PyPDF2.PdfMerger()

lista_arquivos = os.listdir(arquivos)
lista_arquivos.sort()
print(lista_arquivos)

for arquivo in lista_arquivos:
    if arquivo.endswith(".pdf"):
        caminho = os.path.join(arquivos, arquivo)
        merger.append(caminho)

merger.write("C:/com/Mesclador_PDF/arquivo mesclado/Arquivo_final_mesclado.pdf")
merger.close()

