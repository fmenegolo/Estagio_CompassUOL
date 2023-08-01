path = f'/mnt/wsl/PHYSICALDRIVE2/Projects/Compasso/Azimute/Sprint_7/Tarefa_2/'

from pyspark import SparkContext

sc = SparkContext("local", "Contagem de palavras")
ler_texto = sc.textFile("Readme.md")

total_letras = ler_texto.flatMap(lambda line: line.split(" ")).count()
print("Total de palavras no arquivo: ", total_letras)
