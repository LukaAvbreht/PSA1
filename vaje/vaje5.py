# -*- coding: utf-8 -*-
"""
Funkcije na grafih.

V ocenah časovne zahtevnosti je n število vozlišč v grafu,
m število povezav v grafu, d(u) pa število sosedov vozlišča u.
Pri tem predpostavljamo, da velja n = O(m)
(graf ima O(1) povezanih komponent).
"""

def nothing(u, v = None):
    """
    Previsit/postvisit funkcija, ki ne naredi nič.

    Časovna zahtevnost: O(1)
    """
    return True

def DFS(G, roots = None, previsit = nothing, postvisit = nothing):
    """
    Rekurzivno iskanje v globino.

    Graf G je podan kot seznam seznamov sosedov za vsako vozlišče.
    Seznam roots določa vozlišča, iz katerih se začne iskanje
    - privzeto so to vsa vozlišča v grafu.
    Spremenljivki previsit in postvisit določata funkciji,
    ki se izvedeta ob prvem oziroma zadnjem obisku posameznega vozlišča.
    Kot vhod dobita trenutno vozlišče in njegovega predhodnika
    (oziroma None, če tega ni).
    Da se algoritem nadaljuje, morata vrniti True;
    če vrneta False, se funkcija prekine in vrne False.
    Če iskanje pride do konca, funkcija vrne True.

    Časovna zahtevnost: O(m) + O(n) klicev funkcij previsit in postvisit
    """
    def explore(u, v = None):
        """
        Obišče vozlišče u, če še ni bilo obiskano,
        in se rekurzivno kliče na njegovih sosedih.

        Časovna zahtevnost: O(d(u)) + klica funkcij previsit in postvisit
        """
        if visited[u]:
            return True
        visited[u] = True
        if not previsit(u, v):
            return False
        for w in G[u]:
            if not explore(w, u):
                return False
        return postvisit(u, v)

    n = len(G)
    visited = [False] * n
    if roots is None:
        roots = range(n)
    for u in roots:
        if not explore(u):
            return False
    return True
