# -*- coding: utf-8 -*-
from .motd import *


version = '0.1.3'

if __name__ == '__main__':
    import argparse

    parseur_args = argparse.ArgumentParser(
        description="Mathematicians Of The Day")

    parseur_args.add_argument('-d',
                              '--date',
                              help='JJ/MM')
    parseur_args.add_argument('decalage',
                              nargs='?',
                              default='+0')

    args = parseur_args.parse_args()

    m = motd(args.date, args.decalage)
    dico = json.loads(m.sortie())
    for k in dico:
        # print(k)
        for entree in dico[k]:
            s = str(entree['annee'])
            s += " "
            s += entree['type']
            s += " "
            s += entree['prenom']
            s += " "
            s += entree['nom']
            #
            print(s)
