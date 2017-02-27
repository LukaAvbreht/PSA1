# -*- coding: utf-8 -*-
import sys
from .otherFunctions import all_valid_cycles,directet_tree
sys.setrecursionlimit(100000)

__author__ = "LukaAvbreht"

def maxCycleTreeIndependentSet(T, w):
    """
    Najtežja neodvisna množica
    v kartezičnem produktu cikla C_k in drevesa T z n vozlišči,
    kjer ima tabela tež w dimenzije k×n (k >= 2).

    Vrne par (c, s), kjer je c teža najdene neodvisne množice,
    s pa je seznam vozlišč v neodvisni množici,
    torej seznam parov oblike (i, u) (0 <= i <= k-1, 0 <= u <= n-1).
    """
    n = len(T)
    assert all(len(r) == n for r in w), \
        "Dimenzije tabele tež ne ustrezajo številu vozlišč v drevesu!"
    assert all(all(u in T[v] for v in a) for u, a in enumerate(T)), \
        "Podani graf ni neusmerjen!"
    k = len(w)
    assert k >= 2, "k mora biti vsaj 2!"
    if n == 0:
        return (0, [])
    # raise NotImplementedError("Naredi sam!")

    T = directet_tree(T)

    memovred = dict()

    def vrednost_cikla_na_nivoju(nivo,cikel):
        """Vrne vrednost cikla na mestu (nivo) v grafu"""
        if (nivo,cikel) in memovred:
            return memovred[(nivo,cikel)]
        else:
            res = 0
            nivo = int(nivo)
            for j,i in enumerate(cikel):
                if i == '1':
                    res+= w[j][nivo]
            memovred[nivo,cikel] = (res) #, cikel)
            return res  #, cikel

    vsi_mozni_cikli = all_valid_cycles(k)

    graf = [None] * n

    memo = dict()

    def recursive_max_subgroup(ind_voz, cycle):
        """
        Rekurzivna fukncija ki prejme koren v drevesu (n) in njegov vzorec(cycle),
        ter vrne najvecjo utezeno mnozico na drevesu z korenom v n
        """
        # We returnn the value if we calculatet it before and saved it in memo
        if (ind_voz, cycle) in memo:
            return memo[(ind_voz, cycle)]

        # Computation of largest subgroup
        res = 0

        for patern in vsi_mozni_cikli[cycle]:
            weight = vrednost_cikla_na_nivoju(ind_voz, patern)
            for voz in T[ind_voz]:
                tr_weight = recursive_max_subgroup(voz, patern)
                weight += tr_weight
            if weight > res:
                res = weight
                graf[ind_voz] = patern
        memo[(ind_voz, cycle)] = (res)
        return res


    cycle = '0'*k
    res = recursive_max_subgroup(0, cycle)
    resg = list()
    for i,j in enumerate(graf):
        for m,k in enumerate(j):
            if k == "1":
                resg.append((i,m))
    return res, resg
