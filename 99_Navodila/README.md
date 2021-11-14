# Navodila

## Python-3.10.0

### Windows

[Navodila](./Navodila_Python_Win.pdf) za namestitev Python-3.10.0 so na voljo v pdf obliki in vsebujejo celotni postopek namestitve.

### Linux

Python je prednaložen v operacijskem sistemu Linux. Za zagon pa je potrebno uporabiti ukaz `python3`.

### MacOS

* Prenesite namestitveni program (na voljo na povezavi https://www.python.org/downloads/).
* Sledite korakom v namestitvenem programu.
* Pravilno namestitev lahko preverite v terminalu z ukazom `python3`, ki zažene interaktivni način.

## Lokalna namestitev JupyterLab

* Preverite, da imate delujočo namestitev Python-a (`python(3) --version`).
* Odprite terminal oz. ukazno vrstico.
* Poženite ukaz:
  * Windows: `pip install jupyterlab`
  * Linux/MacOS: `pip3 install jupyterlab`
* Po končani namestitvi okolje JupyterLab poženete z ukazom:
  * Windows: `python -m jupyterlab`
  * Linux/MacOS: `python3 -m jupyterlab` oz. kar `jupyterlab`
* Odpre se vam okno vašega privzetega brskalnika z okoljem JupyterLab.

# Uporabna orodja

Čeprav bomo na krožku večinoma uporabljali okolje JupyterLab preko sistema JupyterHub bi rad poudaril, da obstajajo tudi druga orodja, ki jih lahko uporabite.

Kodo lahko pišete v vašem najljubšem urejvalniku besedil, kot so:
* Notepad++,
* Sublime,
* Vi,
* Vim,
* Nano...

In jo nato poženete preko terminala oz. ukazne vrstice.

To je zelo dober začetek, seveda pa za razvoj programov obstajajo tudi računalniški programi, ki že vključujejo množico orodji za razvoj.

## Integrirano razvojno okolje (integrated developnemt environment - IDE)

IDLE je Python IDE, ki je (načeloma) vključen v namestitvi. Poženete ga lahko z ukazom `python -m idlelib` oz. če je že vlkjučen v PATH (namestitev Python preko Windows Store) kar z `idle`.

Tukaj bi omenil še dva IDE-ja katera priporočam, da preizkusite (za nadaljni razvoj v Python):
* [PyCharm](https://www.jetbrains.com/pycharm/),
* [VSCode](https://code.visualstudio.com/).


V teh okoljih so voljo orodja za pisanje, zagon in razhroščevanje vse na enem mestu. In seveda ogromno drugih orodji, uporabljenih pri razvoju programske opreme.

## GIT - Nadzor različic

Pri programiranju je ključnega pomena nadzor različic. Hitri opis si lahko preberete na povezavi https://git-scm.com/book/sl/v2/Pri%C4%8Detek-O-nadzoru-razli%C4%8Dic.
