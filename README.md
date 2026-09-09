# Ruutvõrrandi näidisprojekt

Väike Python-programm ruutvõrrandi $ax^2 + bx + c = 0$ reaalarvuliste lahendite leidmiseks.

## Funktsioon `lahenda_ruutvorrand(a, b, c)`

Funktsioon arvutab ja tagastab võrrandi reaalarvulised lahendid ennikuna (`tuple[float, ...]`).

### Käitumine:
- **Kaks lahendit** (diskriminant > 0): tagastab kahe lahendiga enniku `(x1, x2)`.
- **Üks lahend** (diskriminant = 0): tagastab ühe lahendiga enniku `(x,)`.
- **Reaalarvulisi lahendeid ei ole** (diskriminant < 0): tagastab tühja enniku `()`.
- **Kordaja $a = 0$**: viskab `ValueError` veateatega `"Kordaja 'a' ei tohi olla 0."`, kuna tegemist pole ruutvõrrandiga ja tekiks nulliga jagamine.

## Käivitamine

Liigu sellesse kausta ja käivita interaktiivne programm:

```powershell
python ruutvorrand.py
```

## Testimine

Automaattestide käivitamiseks:

```powershell
python -m unittest -v
```

Projekt sisaldab viit automaattesti failis `test_ruutvorrand.py`, mis katavad erinevaid diskriminandi väärtusi, murdarvulisi kordajaid ning piirjuhtu $a = 0$.
