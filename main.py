from Bio import SeqIO
import pandas as pd
import argparse

def pairwise_align(ref_seq, seq):
    """Runs pairwise alignment for one sequence and the reference"""
    #COMPLETAR
    #Puede ser manual, con MAFFT o Blast. Si se hace con programa debe
    #devolver el nombre del archivo donde esta guardado el alineamiento
    return alignment_filename

def alignment_parser(ref_seq, seq):
    """Return the parsed pairwise alignment"""
    alignment_filename=pairwise_align(ref_seq, seq)
    #Esta funcion tiene sentido si el alineamiento se hace con Blast/MAFFT
    #COMPLETAR
    return parsed_alignment


def parse_ORF_positions(table_filename):
    """Parses a table file with the ORF
    positions and returns them as a dataframe"""
    #Dependiendo el formato de la tabla es posible que haga falta especificar
    #parametros en el read_csv
    #COMPLETAR
    return pd.read_csv(table_filename)

def adjust_ORF_pos(ORF_pos, alignment):
    """Adjusts ORF positions according to gap
    insertions in the reference sequence"""
    #Debe hacer un conteo de gaps en la referencia recorriendo el alineamiento
    #pareado y reajustar las posiciones de inicio y fin de los ORFs.
    #Debe devolver ls posiciones ajustadas en formato lista o diccionario
    #COMPLETAR
    return adjusted_ORFs

def analyze_seq_ORF(seq, ORF):
    """For a specific ORF in a sequence counts nucleotides,
    gaps and missing data, computes percentajes and returns
    them in a tuple with 3 values"""
    #COMPLETAR
    return stats_tuple

def analyze_seqs(ref_seq, input_seqs, table_filename):
    """Iterates every sequence to analyze, performs the
    analysis and returns the results for all the sequences"""
    ORF_pos=parse_ORF_positions(table_filename)
    seqs=list(SeqIO.parse(input_seqs, "fasta"))
    results=[]
    for seq in seqs:
        seq_result=[]
        alignment=alignment_parser(ref_seq, seq)
        adjusted_ORFs=adjust_ORF_pos(ORF_pos, alignment)
        for ORF in adjusted_ORFs:
            seq_result.append(analyze_seq_ORF(seq, ORF))
    return results

def write_analysis_results(ref_seq, input_seqs, table_filename, output_filename):
    """writes sequence analysis results to a csv file"""
    results=analyze_seqs(ref_seq, input_seqs, table_filename)
    #COMPLETAR
    #Tiene que devolver un csv con los resultados, formato de la tabla a discutir
    return 0

def parse_arguments():
    """parses all necessary arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-ref", dest="ref_seq", nargs='+',
                        help="The reference sequence with which other sequences will be compared")
    parser.add_argument("-seqs", dest="seqs", nargs='+',
                        help="Sequences to be analyzed")
    parser.add_argument("-t", dest="table", nargs="+",
                        help="Table with ORF annotations")
    parser.add_argument("-o", dest="output_file", nargs='+',
                        help="Name of the output file")
    return parser.parse_args()

def main():
    """Executes all functions"""
    args=parse_arguments()
    write_analysis_results(args.ref_seq[0], args.seqs[0], args.t[0], args.o[0])
    return 0

if __name__=='__main__':
    main()
