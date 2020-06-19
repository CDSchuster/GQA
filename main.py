from Bio import SeqIO
import pandas as pd
import argparse

def run_mafft_add(ref_seq, seqs):
    """Runs mafft, adding the seqs to the reference sequence"""
    #Aca habria que hacer que el MSA tenga un nombre estandar para que el usuario sepa lo que es
    return MSA_filename

def MSA_parse(ref_seq, seqs):
    """Runs function run_mafft_add, parses the MSA file and returns it as a
    list of SeqIO objects"""
    MSA_filename=run_mafft_add(ref_seq, seqs)
    return list(SeqIO.parse(MSA_filename, "fasta"))

def parse_ORF_positions(table_filename):
    table=pd.read_csv(table_filename)
    #si hay una insercion en la referencia va a haber desfasaje
    #por lo que habria que ajustar las posiciones de ORFS en genoma sin alinear
    #en funcion de la cantidad de gaps detectados
    #esta funcion deberia hacer eso, devolver una lista o diccionario con las
    #posiciones ajustadas al MSA
    return ORF_pos

def analyze_seq_ORF(seq, ORF):
    """For a specific ORF in a sequence counts nucleotides,
    gaps and missing data, computes percentajes and returns
    them in a tuple with 3 values"""
    return stats_tuple

def analyze_MSA(ref_seq, seqs, table_filename):
    """Executes MSA_parse, parse_ORF_positions and generates an array with all
    results of analysis for every ORF in every sequence"""
    MSA=MSA_parse(ref_seq, seqs)
    ORF_pos=parse_ORF_positions(table_filename)
    return [[analyze_seq_ORF(seq, ORF) for ORF in ORF_pos] for seq in MSA]

def write_analysis_results(ref_seq, seqs, table_filename, output_filename):
    """writes MSA analysis results to a csv file"""
    MSA_analysis=analyze_MSA(ref_seq, seqs, table_filename)
    #Tiene que devolver un csv con los resultados, formato de la tabla a discutir
    return 0

def parse_arguments():
    """parses all necessary arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-ref", dest="ref_seq", nargs='+',
                        help="The sequence with which other sequences will be compared")
    parser.add_argument("-seqs", dest="seqs", nargs='+',
                        help="Sequences to be analyzed")
    parser.add_argument("-t", dest="table", nargs="+", type=int,
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
