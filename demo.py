from seq import Seq
from fasta_reader import FastaReader

seq = Seq("test", "ATCG")
print(f"Длина: {len(seq)}")
print(f"Тип: {seq.alphabet()}")

reader = FastaReader("oop/big_example.fasta")
for sequence in reader:
    print(sequence)