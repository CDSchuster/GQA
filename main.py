from Bio import SeqIO
import pandas as pd
import argparse

from pairwise_align import *

def run_pairwise_align(ref_seq, seq):
    """Runs pairwise alignment for one sequence and the reference using MAFFT"""
    ref_name = joinFastas(ref_seq, seq)
    runMafft('merge.fasta')
    # Devuele el nombre de la referencia en caso de que haya multiples secuencias
    return ref_name

def alignment_parser():
    """Return the parsed pairwise alignment"""
    parsed_alignment=SeqIO.parse('merge.fasta', "fasta")
    return parsed_alignment

def parse_ORF_positions(table_filename):
    """Parses a table file with the ORF
    positions and returns them as a dataframe"""
    #Dependiendo el formato de la tabla es posible que haga falta especificar
    #parametros en el read_csv
    #COMPLETAR
    return pd.read_csv(table_filename)

def adjust_ORF_pos(ORF_pos, alignment, ref_name):
    """Adjusts ORF positions according to gap
    insertions in the reference sequence"""
    #Debe hacer un conteo de gaps en la referencia recorriendo el alineamiento
    #pareado y reajustar las posiciones de inicio y fin de los ORFs.
    #Debe devolver ls posiciones ajustadas en formato lista o diccionario
    #COMPLETAR

    # Busco unicamente la secuencia de referencia( Para ello la entrada tambien es el nombre de la referencia "ref_name")
    for seq in alignment:
        if seq.id == ref_name:

            x_index=0
            seq_ref=seq.seq
            gaps_count=0
            largo_seq=len(seq_ref)

            # ORF_pos: Lista de posiciones ordenadas de menor a mayor
            i=0
            target_position=ORF_pos[i]
            adjusted_ORFS=[]
            
            while x_index<largo_seq:
                if seq_ref[x_index] =="N":
                    gaps_count+=1
                if target_position == x_index:
                    adjusted_ORFS.append(x_index+gaps_count)
                    if i<len(ORF_pos)-1:
                        i=i+1
                        target_position=ORF_pos[i]
                x_index=x_index+1

    return adjusted_ORFS

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
