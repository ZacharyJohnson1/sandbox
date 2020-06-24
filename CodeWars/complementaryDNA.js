// In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
// More similar exercise are found here http://rosalind.info/problems/list-view/ (source)
// DNAStrand ("ATTGC") // return "TAACG"
// DNAStrand ("GTAT") // return "CATA" 

function DNAStrand(dna){
  const dnaMap = {'A':'T','T':'A','C':'G','G':'C'};
  let complement = '';
  for(let strand = 0; strand < dna.length; strand++) {
    complement += dnaMap[dna[strand]];
  }
  return complement;
}

console.log(DNAStrand('AAAA'));
console.log(DNAStrand('TTTT'));
console.log(DNAStrand('CCCC'));
console.log(DNAStrand('TTTT'));