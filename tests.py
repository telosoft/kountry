import unittest
from kountry import Country


class TestDBFunctions(unittest.TestCase):

    def test_get(self):
        self.assertEqual(Country.get("TR"), Country.get("TUR"))
        self.assertEqual(Country.get("TUR"), Country.get("792"))
        self.assertEqual(Country.get("792"), Country.get("TR"))
        self.assertEqual(Country.get("TR"), Country.get("Turkey"))

    def test_put(self):
        new_country = Country("XX", "XXX", "000", "XX", "XX", "XXX", ".xx",
                              "X X X", "X X X", "", "", [])
        Country.put(new_country)
        self.assertEqual(Country.get("XX"), new_country)


if __name__ == "__main__":
    unittest.main()
