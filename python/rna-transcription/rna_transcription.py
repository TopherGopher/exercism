def to_rna(dna_strand):
  dna_rna_map = {'G':'C', 'C': 'G', 'T': 'A', 'A': 'U'}
  transcription = ""
  for dna_piece in dna_strand:
    if dna_piece.upper() in dna_rna_map.keys():
      transcription += dna_rna_map[dna_piece.upper()]
    else:
      return ''
  return transcription