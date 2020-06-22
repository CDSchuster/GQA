import os

def joinFastas(ref_seq_file, seq_file):
	"""Combina dos archivos fasta en uno solo, denominado 'merge.fasta' en el directorio de ejecucion """
	with open(ref_seq_file) as ref:
		ref_data = ref.read()
		ref_name=ref_data.split("\n")[0][1:]
	with open(seq_file) as seq:
		seq_data = seq.read()
	ref_data += "\n"
	ref_data += seq_data
	with open ('merge.fasta', 'w') as fp:
		fp.write(ref_data)
	return ref_name

def runMafft(input_fasta):
	"""Corre MAFFT para la entrada de fastas. Devuelve un msa de nombre 'msa.fasta' en el directorio de ejecucion. Tener en cuenta la ruta de MAFFT para ser invocado (Referencia al directorio o PATH) """
	argumentos=[
			"mafft",
			input_fasta,
			">",
			"msa.fasta"
				]
	process = " ".join(argumentos)
	os.system(process)
	return 0