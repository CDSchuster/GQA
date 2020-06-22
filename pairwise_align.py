import os

def joinFastas(ref_seq_file, seq_file):
	"""Combina dos archivos fasta en uno solo, denominado 'merge.fasta' en el directorio de ejecucion """
	with open(ref_seq_file) as ref:
		ref_data = ref.read()
	with open(seq_file) as seq:
		seq_data = seq.read()
	ref_data += "\n"
	ref_data += seq_data
	with open ('merge.fasta', 'w') as fp:
		fp.write(ref_data)
	return 0

def runMafft(input_fasta):
	"""Corre MAFFT para la entrada de fastas. Devuelve un msa de nombre 'msa.fasta' en el directorio de ejecucion """
	argumentos=[
			"mafft",
			input_fasta,
			">",
			"msa.fasta"
				]
	process = " ".join(argumentos)
	os.system(process)
	return 0