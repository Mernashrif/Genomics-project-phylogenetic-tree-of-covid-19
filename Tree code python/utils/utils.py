"""
Utils phydms.
"""

from ete3 import PhyloTree, TreeStyle, NodeStyle
import pandas as pd
import numpy as np
from phydmslib.constants import INDEX_TO_AA, CODON_TO_AA, CODON_TO_INDEX, INDEX_TO_AA


def create_nodestyle(color):
    ns = NodeStyle()
    ns["bgcolor"] = color
    return ns


def viztree(fname, clade_dictionary):
    with open(fname) as f:
        treestring = f.read()
    t = PhyloTree(treestring)
    # get node names
    node_names = [x.name for x in t.iter_descendants("postorder") if x.name]

    # color the clades
    for key in clade_dictionary:
        specs = clade_dictionary[key]
        present = all([x in node_names for x in specs[0]])
        if present:
            (t.get_common_ancestor(specs[0])
              .set_style(create_nodestyle(specs[1])))
    return t


def omegabysiteresults(models, prefix, sig_cutoff):
    for m in models:
        df = pd.read_csv(f"{prefix}/{m}_omegabysite.txt",
                         sep='\t',
                         comment='#',)
        df = df[df["Q"] < sig_cutoff]
        print(f"Model {m}")
        print(f"There are {len(df[df.P > 1.0])} sites with sig "
              f"(Q < {sig_cutoff}) evidence for omega > 1.")
        print(f"There are {len(df[df.P < 1.0])} sites with sig "
              f"(Q < {sig_cutoff}) evidence for omega < 1.")
        print()


def relresults(models, prefix, sig_cutoff):
    for m in models:
        if "gammaomega" in m:
            df = pd.read_csv(f"{prefix}/"
                             f"{m}_posteriorprobabilities.csv")
            df = df[df["fdr"] < 0.05]
            print(f"Model {m}")
            print(f"There are {len(df[df['p(omega > 1)'] > 1.0])} sites with "
                  f"sig (fdr < {sig_cutoff}) evidence for omega > 1.")
            if len(df) > 0:
                print(df)
            print()


def calc_aa_frequencies(alignment):
    """Calculate amino-acid frequencies from a codon alignment.
    Args:
        `alignment` (list)
            Alignment of codon sequences as a list of tuples, (seq_id, seq)
    Returns:
        `pandas` dataframe of amino-acid frequencies by site
    >>> answer = pd.DataFrame({"site": [1, 2], "A": [0.0, 0.0],\
                               "C": [0.0, 0.0], "D": [0.0, 0.0],\
                               "E": [0.0, 0.0], "F": [0.0, 0.0],\
                               "G": [0.0, 0.0], "H": [0.0, 0.0],\
                               "I": [0.0, 0.0], "K": [0.0, 0.0],\
                               "L": [0.0, 0.0], "M": [0.0, 0.0],\
                               "N": [0.0, 0.0], "P": [0.0, 0.0],\
                               "Q": [0.0, 0.0], "R": [0.0, 0.0],\
                               "S": [0.0, 0.0], "T": [0.0, 0.0],\
                               "V": [0.0, 0.0], "W": [0.0, 0.0],\
                               "Y": [0.0, 0.0]}, columns=["site","A","C",\
                                                          "D","E","F","G",\
                                                          "H","I","K","L",\
                                                          "M","N","P","Q",\
                                                          "R","S","T","V",\
                                                          "W","Y"])
    >>> align1 = [("seq_1", "ATGATG"), ("seq_2", "CTTATG")]
    >>> align2 = [("seq_1", "ATGATG"), ("seq_2", "CTT---")]
    >>> answer1 = answer.copy()
    >>> answer1[["L", "M"]] = pd.DataFrame({"L": [0.5, 0.0],\
                                            "M": [0.5, 1.0]})
    >>> answer1.equals(calc_aa_frequencies(align1))
    True
    >>> answer1.equals(calc_aa_frequencies(align2))
    True
    """
    # make dictionary
    codonstr_to_aastr = {}
    for codon in CODON_TO_INDEX:
        codonstr_to_aastr[codon] = INDEX_TO_AA[CODON_TO_AA[CODON_TO_INDEX[codon]]]
    # Read in the alignnment
    assert np.all(np.array([len(s[1]) % 3 for s in alignment]) == 0),\
        "At least one sequence in the alignment is not a multiple of 3."
    seqlength = len(alignment[0][1]) // 3
    df = {k: [0 for x in range(seqlength)] for k in list(INDEX_TO_AA.values())}

    # count amino acid frequencies
    for seq in alignment:
        for i in range(seqlength):
            codon = seq[1][3 * i: 3 * i + 3]
            if codon != '---':
                df[codonstr_to_aastr[codon]][i] += 1
    df = pd.DataFrame(df)

    # Normalize the dataframe
    assert not np.any(df.sum(axis=1) == 0), ("Attempting to normalize a "
                                                "site by an amino acid count"
                                                " of zero. Does the alignment"
                                                " have an all gap column?")
    df = df.div(df.sum(axis=1), axis=0)
    assert np.allclose(df.sum(axis=1), 1, atol=0.005)

    # Final formatting
    aa = [x for x in INDEX_TO_AA.values()]
    aa.sort()  # ABC order
    final_cols = ["site"]
    final_cols.extend(aa)
    df["site"] = [x+1 for x in range(len(df))]
    df = df[final_cols]
    return df
