# PYTHON_17 — Biopython: GenBank -> FASTA -> global alignment (Needleman–Wunsch)

from Bio import Entrez, SeqIO
from Bio.Align import PairwiseAligner
import time

# 1) Ustaw swój email (NCBI tego wymaga)
Entrez.email = "twoj.email@example.com"  # <- ZMIEŃ NA SWÓJ

# Identyfikatory z zadania
IDS = ["JX669568", "JX669571"]

# Nazwa pliku FASTA do zapisu i późniejszego odczytu
FASTA_OUT = "pobrane_sekwencje.fasta"


def pobierz_rekordy_genbank(ids):
    """
    Pobiera rekordy z GenBank (baza 'nucleotide') i zwraca listę SeqRecord.
    """
    # retmode="text" i rettype="gb" -> format GenBank
    handle = Entrez.efetch(db="nucleotide", id=",".join(ids), rettype="gb", retmode="text")
    rekordy = list(SeqIO.parse(handle, "genbank"))
    handle.close()
    return rekordy


def zapisz_do_fasta(rekordy, sciezka):
    """
    Zapisuje listę SeqRecord do FASTA.
    """
    SeqIO.write(rekordy, sciezka, "fasta")


def wczytaj_z_fasta(sciezka):
    """
    Wczytuje rekordy z FASTA i zwraca listę SeqRecord.
    """
    return list(SeqIO.parse(sciezka, "fasta"))


def dopasowanie_globalne(seq1, seq2):
    """
    Globalne dopasowanie Needleman–Wunsch przez PairwiseAligner w trybie 'global'.
    Zwraca najlepsze dopasowanie i jego score.
    """
    aligner = PairwiseAligner()
    aligner.mode = "global"  # global = Needleman–Wunsch

    # Opcjonalnie możesz ustawić punktację (domyślne też działa):
    # aligner.match_score = 1
    # aligner.mismatch_score = -1
    # aligner.open_gap_score = -2
    # aligner.extend_gap_score = -0.5

    alignments = aligner.align(seq1, seq2)
    best = alignments[0]
    return best, best.score


def main():
    try:
        print("Pobieranie rekordów z GenBank:", IDS)
        rekordy_gb = pobierz_rekordy_genbank(IDS)

        if len(rekordy_gb) != 2:
            raise RuntimeError(f"Oczekiwano 2 rekordów, pobrano: {len(rekordy_gb)}")

        # Mała grzeczność wobec NCBI (limit zapytań)
        time.sleep(0.4)

        print(f"Zapis do FASTA: {FASTA_OUT}")
        zapisz_do_fasta(rekordy_gb, FASTA_OUT)

        print("Wczytanie FASTA i przygotowanie sekwencji...")
        rekordy_fasta = wczytaj_z_fasta(FASTA_OUT)

        rec1, rec2 = rekordy_fasta[0], rekordy_fasta[1]
        seq1 = str(rec1.seq)
        seq2 = str(rec2.seq)

        print(f"Seq1: {rec1.id}, długość: {len(seq1)}")
        print(f"Seq2: {rec2.id}, długość: {len(seq2)}")

        print("\nGlobalne dopasowanie (Needleman–Wunsch)...")
        best_alignment, score = dopasowanie_globalne(seq1, seq2)

        print("\nNajlepsze dopasowanie:")
        print(best_alignment)
        print(f"Punktacja (score): {score}")

    except Exception as e:
        print("Wystąpił błąd:", e)


if __name__ == "__main__":
    main()
