# Ruutvõrrandi näidisprojekt

Väike Python-programm Antigravity tunniharjutuseks. Lähtekood sisaldab teadlikult käsitlemata piirjuhtu `a = 0`.

Ülesanne on täiendada funktsiooni `lahenda_ruutvorrand` nii, et:

- `lahenda_ruutvorrand(0, 2, -8)` tagastab `(4.0,)`;
- `lahenda_ruutvorrand(0, 0, 5)` tõstab `ValueError`-i;
- olemasolev käitumine ja testid jäävad tööle;
- lahendus ei lisa väliseid sõltuvusi.

## Käivitamine

Liigu sellesse kausta ja käivita:

```powershell
python ruutvorrand.py
```

## Testimine

```powershell
python -m unittest -v
```

Enne harjutust peavad neli olemasolevat testi läbima. Harjutuse käigus lisatakse kaks piirjuhu testi.
