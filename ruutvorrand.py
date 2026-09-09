"""Lihtne ruutvõrrandi lahendaja tunniharjutuseks."""

import math


def lahenda_ruutvorrand(a: float, b: float, c: float) -> tuple[float, ...]:
    """Tagasta võrrandi ax² + bx + c = 0 reaalarvulised lahendid."""
    diskriminant = b**2 - 4 * a * c

    if diskriminant < 0:
        return ()

    if diskriminant == 0:
        return (-b / (2 * a),)

    juur = math.sqrt(diskriminant)
    return ((-b + juur) / (2 * a), (-b - juur) / (2 * a))


def main() -> None:
    print("Lahendame võrrandi ax² + bx + c = 0")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    try:
        lahendid = lahenda_ruutvorrand(a, b, c)
    except ValueError as viga:
        print(f"Viga: {viga}")
        return

    if not lahendid:
        print("Reaalarvulisi lahendeid ei ole.")
    else:
        print("Lahendid:", ", ".join(str(lahend) for lahend in lahendid))


if __name__ == "__main__":
    main()

