# MOTD

Retrieve famous "Mathematicians Of The Day" from 
[http://mathshistory.st-andrews.ac.uk/Day_files/Year.html](http://mathshistory.st-andrews.ac.uk/Day_files/Year.html)

Disclaimer: This is not an official package!

## 0.1

### Usage as a library

#### Minimal example

``` python3
>>> import motd
>>> motd.motd()
<motd.motd.motd object at 0x7fd2675eb550>
>>> motd.motd().sortie()
'{"30/12": [{"annee": 1869, "prenom": null, "nom": null, "type": "naissance"}, {"annee": null, "prenom": "Emilie", "nom": "MARTIN", "type": "naissance"}, {"annee": 1897, "prenom": "Stanis\\u0142aw", "nom": "SAKS", "type": "naissance"}, {"annee": 1691, "prenom": "Robert", "nom": "BOYLE", "type": "mort"}, {"annee": 1932, "prenom": "Eliakim", "nom": "MOORE", "type": "mort"}, {"annee": 1947, "prenom": "Alfred North", "nom": "WHITEHEAD", "type": "mort"}, {"annee": 1956, "prenom": "Heinrich", "nom": "SCHOLZ", "type": "mort"}, {"annee": 1978, "prenom": "Mark Aronovich", "nom": "NAIMARK", "type": "mort"}, {"annee": 1982, "prenom": "Philip", "nom": "HALL", "type": "mort"}]}'
>>> 

```

#### Options

The constructor admits two optional arguments:

* `jour` specifying date using a string formated as `DD/MM`
  (default is the current system day)
* `decalage` specifying the number of days before (negative
  integer) or after (positivie integer) `date` value. (default is
  0)


``` python3

>>> import motd
>>> motd.motd('01/01').sortie()
>>> '{"01/01": [{"annee": 1803, "prenom": null, "nom": null, "type": "naissance"}, {"annee": null, "prenom": "Guglielmo", "nom": "LIBRI", "type": "naissance"}, {"annee": 1878, "prenom": "Agner", "nom": "ERLANG", "type":...

```

``` python3

>>> import motd
>>> motd.motd(decalage=1).sortie()
>>> motd.motd(decalage=1).sortie()
'{"31/12": [{"annee": 1856, "prenom": null, "nom": null, "type": "naissance"}, {"annee": null, "prenom": "William", "nom": "THOMSON", "type":...

```

``` python3

>>> import motd
>>> motd.motd('01/01', decalage=-2).sortie()
'{"30/12": [{"annee": 1869, "prenom": "Emilie", "nom": "MARTIN", "type": "naissance"}, {"annee": 1897, "prenom": "Stanis\\u0142aw", "nom": "SAKS", "type": "naissance"}, {"annee": 1691, "prenom": "Robert", "nom": "BOYLE", "type": "mort"}, {"annee": 1932, "prenom": "Eliakim", "nom": "MOORE", "type": "mort"}, {"annee": 1947, "prenom": "Alfred North", "nom": "WHITEHEAD", "type": "mort"}, {"annee": 1956, "prenom": "Heinrich", "nom": "SCHOLZ", "type": "mort"}, {"annee": 1978, "prenom": "Mark Aronovich", "nom": "NAIMARK", "type": "mort"}, {"annee": 1982, "prenom": "Philip", "nom": "HALL", "type": "mort"}]}'

```

``` python3

>>> import motd
>>> motd.motd(jour='01/01', decalage=-2).sortie()
'{"30/12": [{"annee": 1869, "prenom": "Emilie", "nom": "MARTIN", "type": "naissance"}, {"annee": 1897,...

```



### Usage in standalone app (code below)

#### How-to use it

1. Copy next code content in a `motd` file.

2. Change eventually the shebang line and make the file executable
`chmod 755 motd`

3. Move it in a path known by your shell. For example: `~/.local/bin`

4. Session example

``` console
$ motd
1869 naissance Emilie MARTIN
1897 naissance Stanisław SAKS
1691 mort Robert BOYLE
1932 mort Eliakim MOORE
1947 mort Alfred North WHITEHEAD
1956 mort Heinrich SCHOLZ
1978 mort Mark Aronovich NAIMARK
1982 mort Philip HALL
$ motd -d 01/08
1861 naissance Ivar BENDIXSON
1881 naissance Otto TOEPLITZ
1937 naissance Barry JOHNSON
1955 naissance Bernadette PERRIN-RIOU
1987 mort Evelyn NELSON
1992 mort Leslie FOX
$ motd -d 01/08 -1
1704 naissance Gabriel CRAMER
1712 naissance Samuel KÖNIG
1777 naissance William SPENCE
1810 naissance Oliver BYRNE
1826 naissance Ernst MEISSEL
1863 naissance George MILLER
1923 naissance Joseph KELLER
1927 naissance Felix BROWDER
1726 mort Nicolaus(II) BERNOULLI
1896 mort Christian WIENER
1980 mort Pascual JORDAN

```

Further you can pipe with `sort` command.

You can also change source code of the app to output different
lines.


#### Standalone app code

``` python3

#!/usr/bin/python3
__author__ = "David COBAC"
__date__ = 20191230

import motd
import json
import argparse


parseur_args = argparse.ArgumentParser(
    description="""Mathematicians Of The Day from website
    http://mathshistory.st-andrews.ac.uk/Day_files/Year.html
    not an official package""")

parseur_args.add_argument('-d', '--date', help='JJ/MM')
parseur_args.add_argument('decalage',
                          nargs='?',
                          default='+0')

args = parseur_args.parse_args()

m = motd.motd(args.date, args.decalage)
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

```

## about

`motd` is rather an attempt to publish on the `PyPi` packages
index than a fully completed python project, I do not recommend
to use it for professionnal purpose. You have to consider this
package as an experiment.
