# GQA

Segun mail Mariana Viegas.

Entrada:

+ alineamiento/secuencia en FASTA
+ secuencia de referencia (la que uno quiera, ahora sería utilizada para Corona pero podría ser usada para cualquier virus)
+ un archivo tabulado de anotación de genes (posición de cada ORF)

  - Creo que partiendo de la idea de lo que hicimos para el MSA_cut, que le dabamos una query, podriamos usar la posicion como dice Mariana o una query.

* un archivo tabulado de localización de primers y sondas de interés

Calcular:

1) % de cada ORF con datos (entiéndase: bases nucleotídicas)

2) % NNNs en cada ORF

3) gaps encontrados en los ORF  

4) Codones START atrasados

5) Codones de STOP prematuros

6) Detección de mutaciones en los primers que se usan para hacer las qPCR de diagnóstico  

Salida:

* una o dos tablas de doble entrada que para cada secuencia informen el resultado de cada análisis 
