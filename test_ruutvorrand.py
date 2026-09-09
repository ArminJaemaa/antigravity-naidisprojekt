import unittest

from ruutvorrand import lahenda_ruutvorrand


class RuutvorrandiTest(unittest.TestCase):
    def test_kaks_lahendit(self):
        self.assertEqual(lahenda_ruutvorrand(1, -3, 2), (2.0, 1.0))

    def test_uks_lahend(self):
        self.assertEqual(lahenda_ruutvorrand(1, 2, 1), (-1.0,))

    def test_reaalarvulisi_lahendeid_ei_ole(self):
        self.assertEqual(lahenda_ruutvorrand(1, 0, 1), ())

    def test_murdarvulised_kordajad(self):
        self.assertEqual(lahenda_ruutvorrand(0.5, -1.5, 1), (2.0, 1.0))


if __name__ == "__main__":
    unittest.main()

