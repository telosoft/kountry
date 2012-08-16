# Copyright (c) 2012, Vehbi Sinan Tunalioglu <vst@vsthost.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# - Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
#
# - Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in
#   the documentation and/or other materials provided with the
#   distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

__version__ = (0, 0, 0, "dev", 0)


class Country(object):
    """
    Provides the canonical representation of a country object and
    further functionality such as querying.
    """

    """
    Provides the country database.
    """
    DB = {"index_code_2": dict(),
          "index_code_3": dict(),
          "index_enum": dict()}

    def __init__(self, code_2, code_3, enum, code_fips, continent, currency,
                 tld, name, capital, postal_code_format, postal_code_regex,
                 phone_prefixes):
        # Save object attributes:
        self.code_2 = code_2
        self.code_3 = code_3
        self.enum = enum
        self.code_fips = code_fips
        self.continent = continent
        self.currency = currency
        self.tld = tld
        self.name = name
        self.capital = capital
        self.postal_code_format = postal_code_format
        self.postal_code_regex = postal_code_regex
        self.phone_prefixes = phone_prefixes

    def __repr__(self):
        return self.name

    @classmethod
    def get(cls, identifier):
        """
        Queries the :attr:`Country.DB` for the identifier provideds
        and returns the country object if found, ``None`` otherwise.
        """
        return cls.DB["index_code_2"].get(identifier) or \
               cls.DB["index_code_3"].get(identifier) or \
               cls.DB["index_enum"].get(identifier)

    @classmethod
    def put(cls, country):
        """
        Inserts or overrides a country in the DB.

        Note that this method indexes every country by its
        :attr:`code_2`, :attr:`code_3` and :attr:`enum` attributes.
        """
        cls.DB["index_code_2"][country.code_2] = country
        cls.DB["index_code_3"][country.code_3] = country
        cls.DB["index_enum"][country.enum] = country

#######################
# DATABASE POPULATION #
#######################

Country.put(Country("AD", "AND", "020", "AN", "EU", "EUR", ".ad",
                    "Andorra", "Andorra la Vella",
                    "AD###", "^(?:AD)*(\d{3})$", ["376"]))
Country.put(Country("AD", "AND", "020", "AN", "EU", "EUR", ".ad",
                    "Andorra", "Andorra la Vella",
                    "AD###", "^(?:AD)*(\d{3})$", ["376"]))
Country.put(Country("AE", "ARE", "784", "AE", "AS", "AED", ".ae",
                    "United Arab Emirates", "Abu Dhabi",
                    "", "", ["971"]))
Country.put(Country("AF", "AFG", "004", "AF", "AS", "AFN", ".af",
                    "Afghanistan", "Kabul",
                    "", "", ["93"]))
Country.put(Country("AG", "ATG", "028", "AC", "NA", "XCD", ".ag",
                    "Antigua and Barbuda", "St. John's",
                    "", "", ["1-268"]))
Country.put(Country("AI", "AIA", "660", "AV", "NA", "XCD", ".ai",
                    "Anguilla", "The Valley",
                    "", "", ["1-264"]))
Country.put(Country("AL", "ALB", "008", "AL", "EU", "ALL", ".al",
                    "Albania", "Tirana",
                    "", "", ["355"]))
Country.put(Country("AM", "ARM", "051", "AM", "AS", "AMD", ".am",
                    "Armenia", "Yerevan",
                    "######", "^(\d{6})$", ["374"]))
Country.put(Country("AO", "AGO", "024", "AO", "AF", "AOA", ".ao",
                    "Angola", "Luanda",
                    "", "", ["244"]))
Country.put(Country("AQ", "ATA", "010", "AY", "AN", "", ".aq",
                    "Antarctica", "",
                    "", "", [""]))
Country.put(Country("AR", "ARG", "032", "AR", "SA", "ARS", ".ar",
                    "Argentina", "Buenos Aires",
                    "@####@@@", "^([A-Z]\d{4}[A-Z]{3})$", ["54"]))
Country.put(Country("AS", "ASM", "016", "AQ", "OC", "USD", ".as",
                    "American Samoa", "Pago Pago",
                    "", "", ["1-684"]))
Country.put(Country("AT", "AUT", "040", "AU", "EU", "EUR", ".at",
                    "Austria", "Vienna",
                    "####", "^(\d{4})$", ["43"]))
Country.put(Country("AU", "AUS", "036", "AS", "OC", "AUD", ".au",
                    "Australia", "Canberra",
                    "####", "^(\d{4})$", ["61"]))
Country.put(Country("AW", "ABW", "533", "AA", "NA", "AWG", ".aw",
                    "Aruba", "Oranjestad",
                    "", "", ["297"]))
Country.put(Country("AX", "ALA", "248", "", "EU", "EUR", ".ax",
                    "Aland Islands", "Mariehamn",
                    "", "", ["358-18"]))
Country.put(Country("AZ", "AZE", "031", "AJ", "AS", "AZN", ".az",
                    "Azerbaijan", "Baku",
                    "AZ ####", "^(?:AZ)*(\d{4})$", ["994"]))
Country.put(Country("BA", "BIH", "070", "BK", "EU", "BAM", ".ba",
                    "Bosnia and Herzegovina", "Sarajevo",
                    "#####", "^(\d{5})$", ["387"]))
Country.put(Country("BB", "BRB", "052", "BB", "NA", "BBD", ".bb",
                    "Barbados", "Bridgetown",
                    "BB#####", "^(?:BB)*(\d{5})$", ["1-246"]))
Country.put(Country("BD", "BGD", "050", "BG", "AS", "BDT", ".bd",
                    "Bangladesh", "Dhaka",
                    "####", "^(\d{4})$", ["880"]))
Country.put(Country("BE", "BEL", "056", "BE", "EU", "EUR", ".be",
                    "Belgium", "Brussels",
                    "####", "^(\d{4})$", ["32"]))
Country.put(Country("BF", "BFA", "854", "UV", "AF", "XOF", ".bf",
                    "Burkina Faso", "Ouagadougou",
                    "", "", ["226"]))
Country.put(Country("BG", "BGR", "100", "BU", "EU", "BGN", ".bg",
                    "Bulgaria", "Sofia",
                    "####", "^(\d{4})$", ["359"]))
Country.put(Country("BH", "BHR", "048", "BA", "AS", "BHD", ".bh",
                    "Bahrain", "Manama",
                    "####|###", "^(\d{3}\d?)$", ["973"]))
Country.put(Country("BI", "BDI", "108", "BY", "AF", "BIF", ".bi",
                    "Burundi", "Bujumbura",
                    "", "", ["257"]))
Country.put(Country("BJ", "BEN", "204", "BN", "AF", "XOF", ".bj",
                    "Benin", "Porto-Novo",
                    "", "", ["229"]))
Country.put(Country("BL", "BLM", "652", "TB", "NA", "EUR", ".gp",
                    "Saint Barthelemy", "Gustavia",
                    "### ###", "", ["590"]))
Country.put(Country("BM", "BMU", "060", "BD", "NA", "BMD", ".bm",
                    "Bermuda", "Hamilton",
                    "@@ ##", "^([A-Z]{2}\d{2})$", ["1-441"]))
Country.put(Country("BN", "BRN", "096", "BX", "AS", "BND", ".bn",
                    "Brunei", "Bandar Seri Begawan",
                    "@@####", "^([A-Z]{2}\d{4})$", ["673"]))
Country.put(Country("BO", "BOL", "068", "BL", "SA", "BOB", ".bo",
                    "Bolivia", "Sucre",
                    "", "", ["591"]))
Country.put(Country("BQ", "BES", "535", "", "NA", "USD", ".bq",
                    "Bonaire, Saint Eustatius and Saba", "",
                    "", "", ["599"]))
Country.put(Country("BR", "BRA", "076", "BR", "SA", "BRL", ".br",
                    "Brazil", "Brasilia",
                    "#####-###", "^(\d{8})$", ["55"]))
Country.put(Country("BS", "BHS", "044", "BF", "NA", "BSD", ".bs",
                    "Bahamas", "Nassau",
                    "", "", ["1-242"]))
Country.put(Country("BT", "BTN", "064", "BT", "AS", "BTN", ".bt",
                    "Bhutan", "Thimphu",
                    "", "", ["975"]))
Country.put(Country("BV", "BVT", "074", "BV", "AN", "NOK", ".bv",
                    "Bouvet Island", "",
                    "", "", [""]))
Country.put(Country("BW", "BWA", "072", "BC", "AF", "BWP", ".bw",
                    "Botswana", "Gaborone",
                    "", "", ["267"]))
Country.put(Country("BY", "BLR", "112", "BO", "EU", "BYR", ".by",
                    "Belarus", "Minsk",
                    "######", "^(\d{6})$", ["375"]))
Country.put(Country("BZ", "BLZ", "084", "BH", "NA", "BZD", ".bz",
                    "Belize", "Belmopan",
                    "", "", ["501"]))
Country.put(Country("CA", "CAN", "124", "CA", "NA", "CAD", ".ca",
                    "Canada", "Ottawa",
                    "@#@ #@#", "^([a-zA-Z]\d[a-zA-Z]\d[a-zA-Z]\d)$", ["1"]))
Country.put(Country("CC", "CCK", "166", "CK", "AS", "AUD", ".cc",
                    "Cocos Islands", "West Island",
                    "", "", ["61"]))
Country.put(Country("CD", "COD", "180", "CG", "AF", "CDF", ".cd",
                    "Democratic Republic of the Congo", "Kinshasa",
                    "", "", ["243"]))
Country.put(Country("CF", "CAF", "140", "CT", "AF", "XAF", ".cf",
                    "Central African Republic", "Bangui",
                    "", "", ["236"]))
Country.put(Country("CG", "COG", "178", "CF", "AF", "XAF", ".cg",
                    "Republic of the Congo", "Brazzaville",
                    "", "", ["242"]))
Country.put(Country("CH", "CHE", "756", "SZ", "EU", "CHF", ".ch",
                    "Switzerland", "Berne",
                    "####", "^(\d{4})$", ["41"]))
Country.put(Country("CI", "CIV", "384", "IV", "AF", "XOF", ".ci",
                    "Ivory Coast", "Yamoussoukro",
                    "", "", ["225"]))
Country.put(Country("CK", "COK", "184", "CW", "OC", "NZD", ".ck",
                    "Cook Islands", "Avarua",
                    "", "", ["682"]))
Country.put(Country("CL", "CHL", "152", "CI", "SA", "CLP", ".cl",
                    "Chile", "Santiago",
                    "#######", "^(\d{7})$", ["56"]))
Country.put(Country("CM", "CMR", "120", "CM", "AF", "XAF", ".cm",
                    "Cameroon", "Yaounde",
                    "", "", ["237"]))
Country.put(Country("CN", "CHN", "156", "CH", "AS", "CNY", ".cn",
                    "China", "Beijing",
                    "######", "^(\d{6})$", ["86"]))
Country.put(Country("CO", "COL", "170", "CO", "SA", "COP", ".co",
                    "Colombia", "Bogota",
                    "", "", ["57"]))
Country.put(Country("CR", "CRI", "188", "CS", "NA", "CRC", ".cr",
                    "Costa Rica", "San Jose",
                    "####", "^(\d{4})$", ["506"]))
Country.put(Country("CU", "CUB", "192", "CU", "NA", "CUP", ".cu",
                    "Cuba", "Havana",
                    "CP #####", "^(?:CP)*(\d{5})$", ["53"]))
Country.put(Country("CV", "CPV", "132", "CV", "AF", "CVE", ".cv",
                    "Cape Verde", "Praia",
                    "####", "^(\d{4})$", ["238"]))
Country.put(Country("CW", "CUW", "531", "UC", "NA", "ANG", ".cw",
                    "Curacao", "Willemstad",
                    "", "", ["599"]))
Country.put(Country("CX", "CXR", "162", "KT", "AS", "AUD", ".cx",
                    "Christmas Island", "Flying Fish Cove",
                    "####", "^(\d{4})$", ["61"]))
Country.put(Country("CY", "CYP", "196", "CY", "EU", "EUR", ".cy",
                    "Cyprus", "Nicosia",
                    "####", "^(\d{4})$", ["357"]))
Country.put(Country("CZ", "CZE", "203", "EZ", "EU", "CZK", ".cz",
                    "Czech Republic", "Prague",
                    "### ##", "^(\d{5})$", ["420"]))
Country.put(Country("DE", "DEU", "276", "GM", "EU", "EUR", ".de",
                    "Germany", "Berlin",
                    "#####", "^(\d{5})$", ["49"]))
Country.put(Country("DJ", "DJI", "262", "DJ", "AF", "DJF", ".dj",
                    "Djibouti", "Djibouti",
                    "", "", ["253"]))
Country.put(Country("DK", "DNK", "208", "DA", "EU", "DKK", ".dk",
                    "Denmark", "Copenhagen",
                    "####", "^(\d{4})$", ["45"]))
Country.put(Country("DM", "DMA", "212", "DO", "NA", "XCD", ".dm",
                    "Dominica", "Roseau",
                    "", "", ["1-767"]))
Country.put(Country("DO", "DOM", "214", "DR", "NA", "DOP", ".do",
                    "Dominican Republic", "Santo Domingo",
                    "#####", "^(\d{5})$", ["1-809", "1-829"]))
Country.put(Country("DZ", "DZA", "012", "AG", "AF", "DZD", ".dz",
                    "Algeria", "Algiers",
                    "#####", "^(\d{5})$", ["213"]))
Country.put(Country("EC", "ECU", "218", "EC", "SA", "USD", ".ec",
                    "Ecuador", "Quito",
                    "@####@", "^([a-zA-Z]\d{4}[a-zA-Z])$", ["593"]))
Country.put(Country("EE", "EST", "233", "EN", "EU", "EUR", ".ee",
                    "Estonia", "Tallinn",
                    "#####", "^(\d{5})$", ["372"]))
Country.put(Country("EG", "EGY", "818", "EG", "AF", "EGP", ".eg",
                    "Egypt", "Cairo",
                    "#####", "^(\d{5})$", ["20"]))
Country.put(Country("EH", "ESH", "732", "WI", "AF", "MAD", ".eh",
                    "Western Sahara", "El-Aaiun",
                    "", "", ["212"]))
Country.put(Country("ER", "ERI", "232", "ER", "AF", "ERN", ".er",
                    "Eritrea", "Asmara",
                    "", "", ["291"]))
Country.put(Country("ES", "ESP", "724", "SP", "EU", "EUR", ".es",
                    "Spain", "Madrid",
                    "#####", "^(\d{5})$", ["34"]))
Country.put(Country("ET", "ETH", "231", "ET", "AF", "ETB", ".et",
                    "Ethiopia", "Addis Ababa",
                    "####", "^(\d{4})$", ["251"]))
Country.put(Country("FI", "FIN", "246", "FI", "EU", "EUR", ".fi",
                    "Finland", "Helsinki",
                    "#####", "^(?:FI)*(\d{5})$", ["358"]))
Country.put(Country("FJ", "FJI", "242", "FJ", "OC", "FJD", ".fj",
                    "Fiji", "Suva",
                    "", "", ["679"]))
Country.put(Country("FK", "FLK", "238", "FK", "SA", "FKP", ".fk",
                    "Falkland Islands", "Stanley",
                    "", "", ["500"]))
Country.put(Country("FM", "FSM", "583", "FM", "OC", "USD", ".fm",
                    "Micronesia", "Palikir",
                    "#####", "^(\d{5})$", ["691"]))
Country.put(Country("FO", "FRO", "234", "FO", "EU", "DKK", ".fo",
                    "Faroe Islands", "Torshavn",
                    "FO-###", "^(?:FO)*(\d{3})$", ["298"]))
Country.put(Country("FR", "FRA", "250", "FR", "EU", "EUR", ".fr",
                    "France", "Paris",
                    "#####", "^(\d{5})$", ["33"]))
Country.put(Country("GA", "GAB", "266", "GB", "AF", "XAF", ".ga",
                    "Gabon", "Libreville",
                    "", "", ["241"]))
Country.put(Country("GB", "GBR", "826", "UK", "EU", "GBP", ".uk",
                    "United Kingdom", "London",
                    "@# #@@|@## #@@|@@# #@@|@@## #@@|@#@ #@@|@@#@ #@@|GIR0AA",
                    "^(([A-Z]\d{2}[A-Z]{2})|"
                    "([A-Z]\d{3}[A-Z]{2})|"
                    "([A-Z]{2}\d{2}[A-Z]{2})|"
                    "([A-Z]{2}\d{3}[A-Z]{2})|"
                    "([A-Z]\d[A-Z]\d[A-Z]{2})|"
                    "([A-Z]{2}\d[A-Z]\d[A-Z]{2})|"
                    "(GIR0AA))$", ["44"]))
Country.put(Country("GD", "GRD", "308", "GJ", "NA", "XCD", ".gd",
                    "Grenada", "St. George's",
                    "", "", ["1-473"]))
Country.put(Country("GE", "GEO", "268", "GG", "AS", "GEL", ".ge",
                    "Georgia", "Tbilisi",
                    "####", "^(\d{4})$", ["995"]))
Country.put(Country("GF", "GUF", "254", "FG", "SA", "EUR", ".gf",
                    "French Guiana", "Cayenne",
                    "#####", "^((97)|(98)3\d{2})$", ["594"]))
Country.put(Country("GG", "GGY", "831", "GK", "EU", "GBP", ".gg",
                    "Guernsey", "St Peter Port",
                    "@# #@@|@## #@@|@@# #@@|@@## #@@|@#@ #@@|@@#@ #@@|GIR0AA",
                    "^(([A-Z]\d{2}[A-Z]{2})|([A-Z]\d{3}[A-Z]{2})|"
                    "([A-Z]{2}\d{2}[A-Z]{2})|([A-Z]{2}\d{3}[A-Z]{2})|"
                    "([A-Z]\d[A-Z]\d[A-Z]{2})|([A-Z]{2}\d[A-Z]\d[A-Z]{2})|"
                    "(GIR0AA))$", ["44-1481"]))
Country.put(Country("GH", "GHA", "288", "GH", "AF", "GHS", ".gh",
                    "Ghana", "Accra",
                    "", "", ["233"]))
Country.put(Country("GI", "GIB", "292", "GI", "EU", "GIP", ".gi",
                    "Gibraltar", "Gibraltar",
                    "", "", ["350"]))
Country.put(Country("GL", "GRL", "304", "GL", "NA", "DKK", ".gl",
                    "Greenland", "Nuuk",
                    "####", "^(\d{4})$", ["299"]))
Country.put(Country("GM", "GMB", "270", "GA", "AF", "GMD", ".gm",
                    "Gambia", "Banjul",
                    "", "", ["220"]))
Country.put(Country("GN", "GIN", "324", "GV", "AF", "GNF", ".gn",
                    "Guinea", "Conakry",
                    "", "", ["224"]))
Country.put(Country("GP", "GLP", "312", "GP", "NA", "EUR", ".gp",
                    "Guadeloupe", "Basse-Terre",
                    "#####", "^((97)|(98)\d{3})$", ["590"]))
Country.put(Country("GQ", "GNQ", "226", "EK", "AF", "XAF", ".gq",
                    "Equatorial Guinea", "Malabo",
                    "", "", ["240"]))
Country.put(Country("GR", "GRC", "300", "GR", "EU", "EUR", ".gr",
                    "Greece", "Athens",
                    "### ##", "^(\d{5})$", ["30"]))
Country.put(Country("GS", "SGS", "239", "SX", "AN", "GBP", ".gs",
                    "South Georgia and the South Sandwich Islands",
                    "Grytviken",
                    "", "", [""]))
Country.put(Country("GT", "GTM", "320", "GT", "NA", "GTQ", ".gt",
                    "Guatemala", "Guatemala City",
                    "#####", "^(\d{5})$", ["502"]))
Country.put(Country("GU", "GUM", "316", "GQ", "OC", "USD", ".gu",
                    "Guam", "Hagatna",
                    "969##", "^(969\d{2})$", ["1-671"]))
Country.put(Country("GW", "GNB", "624", "PU", "AF", "XOF", ".gw",
                    "Guinea-Bissau", "Bissau",
                    "####", "^(\d{4})$", ["245"]))
Country.put(Country("GY", "GUY", "328", "GY", "SA", "GYD", ".gy",
                    "Guyana", "Georgetown",
                    "", "", ["592"]))
Country.put(Country("HK", "HKG", "344", "HK", "AS", "HKD", ".hk",
                    "Hong Kong", "Hong Kong",
                    "", "", ["852"]))
Country.put(Country("HM", "HMD", "334", "HM", "AN", "AUD", ".hm",
                    "Heard Island and McDonald Islands", "",
                    "", "", [""]))
Country.put(Country("HN", "HND", "340", "HO", "NA", "HNL", ".hn",
                    "Honduras", "Tegucigalpa",
                    "@@####", "^([A-Z]{2}\d{4})$", ["504"]))
Country.put(Country("HR", "HRV", "191", "HR", "EU", "HRK", ".hr",
                    "Croatia", "Zagreb",
                    "HR-#####", "^(?:HR)*(\d{5})$", ["385"]))
Country.put(Country("HT", "HTI", "332", "HA", "NA", "HTG", ".ht",
                    "Haiti", "Port-au-Prince",
                    "HT####", "^(?:HT)*(\d{4})$", ["509"]))
Country.put(Country("HU", "HUN", "348", "HU", "EU", "HUF", ".hu",
                    "Hungary", "Budapest",
                    "####", "^(\d{4})$", ["36"]))
Country.put(Country("ID", "IDN", "360", "ID", "AS", "IDR", ".id",
                    "Indonesia", "Jakarta",
                    "#####", "^(\d{5})$", ["62"]))
Country.put(Country("IE", "IRL", "372", "EI", "EU", "EUR", ".ie",
                    "Ireland", "Dublin",
                    "", "", ["353"]))
Country.put(Country("IL", "ISR", "376", "IS", "AS", "ILS", ".il",
                    "Israel", "Jerusalem",
                    "#####", "^(\d{5})$", ["972"]))
Country.put(Country("IM", "IMN", "833", "IM", "EU", "GBP", ".im",
                    "Isle of Man", "Douglas, Isle of Man",
                    "@# #@@|@## #@@|@@# #@@|@@## #@@|@#@ #@@|@@#@ #@@|GIR0AA",
                    "^(([A-Z]\d{2}[A-Z]{2})|([A-Z]\d{3}[A-Z]{2})|"
                    "([A-Z]{2}\d{2}[A-Z]{2})|([A-Z]{2}\d{3}[A-Z]{2})|"
                    "([A-Z]\d[A-Z]\d[A-Z]{2})|([A-Z]{2}\d[A-Z]\d[A-Z]{2})|"
                    "(GIR0AA))$", ["44-1624"]))
Country.put(Country("IN", "IND", "356", "IN", "AS", "INR", ".in",
                    "India", "New Delhi",
                    "######", "^(\d{6})$", ["91"]))
Country.put(Country("IO", "IOT", "086", "IO", "AS", "USD", ".io",
                    "British Indian Ocean Territory", "Diego Garcia",
                    "", "", ["246"]))
Country.put(Country("IQ", "IRQ", "368", "IZ", "AS", "IQD", ".iq",
                    "Iraq", "Baghdad",
                    "#####", "^(\d{5})$", ["964"]))
Country.put(Country("IR", "IRN", "364", "IR", "AS", "IRR", ".ir",
                    "Iran", "Tehran",
                    "##########", "^(\d{10})$", ["98"]))
Country.put(Country("IS", "ISL", "352", "IC", "EU", "ISK", ".is",
                    "Iceland", "Reykjavik",
                    "###", "^(\d{3})$", ["354"]))
Country.put(Country("IT", "ITA", "380", "IT", "EU", "EUR", ".it",
                    "Italy", "Rome",
                    "#####", "^(\d{5})$", ["39"]))
Country.put(Country("JE", "JEY", "832", "JE", "EU", "GBP", ".je",
                    "Jersey", "Saint Helier",
                    "@# #@@|@## #@@|@@# #@@|@@## #@@|@#@ #@@|@@#@ #@@|GIR0AA",
                    "^(([A-Z]\d{2}[A-Z]{2})|([A-Z]\d{3}[A-Z]{2})|"
                    "([A-Z]{2}\d{2}[A-Z]{2})|([A-Z]{2}\d{3}[A-Z]{2})|"
                    "([A-Z]\d[A-Z]\d[A-Z]{2})|([A-Z]{2}\d[A-Z]\d[A-Z]{2})|"
                    "(GIR0AA))$", ["44-1534"]))
Country.put(Country("JM", "JAM", "388", "JM", "NA", "JMD", ".jm",
                    "Jamaica", "Kingston",
                    "", "", ["1-876"]))
Country.put(Country("JO", "JOR", "400", "JO", "AS", "JOD", ".jo",
                    "Jordan", "Amman",
                    "#####", "^(\d{5})$", ["962"]))
Country.put(Country("JP", "JPN", "392", "JA", "AS", "JPY", ".jp",
                    "Japan", "Tokyo",
                    "###-####", "^(\d{7})$", ["81"]))
Country.put(Country("KE", "KEN", "404", "KE", "AF", "KES", ".ke",
                    "Kenya", "Nairobi",
                    "#####", "^(\d{5})$", ["254"]))
Country.put(Country("KG", "KGZ", "417", "KG", "AS", "KGS", ".kg",
                    "Kyrgyzstan", "Bishkek",
                    "######", "^(\d{6})$", ["996"]))
Country.put(Country("KH", "KHM", "116", "CB", "AS", "KHR", ".kh",
                    "Cambodia", "Phnom Penh",
                    "#####", "^(\d{5})$", ["855"]))
Country.put(Country("KI", "KIR", "296", "KR", "OC", "AUD", ".ki",
                    "Kiribati", "Tarawa",
                    "", "", ["686"]))
Country.put(Country("KM", "COM", "174", "CN", "AF", "KMF", ".km",
                    "Comoros", "Moroni",
                    "", "", ["269"]))
Country.put(Country("KN", "KNA", "659", "SC", "NA", "XCD", ".kn",
                    "Saint Kitts and Nevis", "Basseterre",
                    "", "", ["1-869"]))
Country.put(Country("KP", "PRK", "408", "KN", "AS", "KPW", ".kp",
                    "North Korea", "Pyongyang",
                    "###-###", "^(\d{6})$", ["850"]))
Country.put(Country("KR", "KOR", "410", "KS", "AS", "KRW", ".kr",
                    "South Korea", "Seoul",
                    "SEOUL ###-###", "^(?:SEOUL)*(\d{6})$", ["82"]))
Country.put(Country("XK", "XKX", "0", "KV", "EU", "EUR", "",
                    "Kosovo", "Pristina",
                    "", "", [""]))
Country.put(Country("KW", "KWT", "414", "KU", "AS", "KWD", ".kw",
                    "Kuwait", "Kuwait City",
                    "#####", "^(\d{5})$", ["965"]))
Country.put(Country("KY", "CYM", "136", "CJ", "NA", "KYD", ".ky",
                    "Cayman Islands", "George Town",
                    "", "", ["1-345"]))
Country.put(Country("KZ", "KAZ", "398", "KZ", "AS", "KZT", ".kz",
                    "Kazakhstan", "Astana",
                    "######", "^(\d{6})$", ["7"]))
Country.put(Country("LA", "LAO", "418", "LA", "AS", "LAK", ".la",
                    "Laos", "Vientiane",
                    "#####", "^(\d{5})$", ["856"]))
Country.put(Country("LB", "LBN", "422", "LE", "AS", "LBP", ".lb",
                    "Lebanon", "Beirut",
                    "#### ####|####", "^(\d{4}(\d{4})?)$", ["961"]))
Country.put(Country("LC", "LCA", "662", "ST", "NA", "XCD", ".lc",
                    "Saint Lucia", "Castries",
                    "", "", ["1-758"]))
Country.put(Country("LI", "LIE", "438", "LS", "EU", "CHF", ".li",
                    "Liechtenstein", "Vaduz",
                    "####", "^(\d{4})$", ["423"]))
Country.put(Country("LK", "LKA", "144", "CE", "AS", "LKR", ".lk",
                    "Sri Lanka", "Colombo",
                    "#####", "^(\d{5})$", ["94"]))
Country.put(Country("LR", "LBR", "430", "LI", "AF", "LRD", ".lr",
                    "Liberia", "Monrovia",
                    "####", "^(\d{4})$", ["231"]))
Country.put(Country("LS", "LSO", "426", "LT", "AF", "LSL", ".ls",
                    "Lesotho", "Maseru",
                    "###", "^(\d{3})$", ["266"]))
Country.put(Country("LT", "LTU", "440", "LH", "EU", "LTL", ".lt",
                    "Lithuania", "Vilnius",
                    "LT-#####", "^(?:LT)*(\d{5})$", ["370"]))
Country.put(Country("LU", "LUX", "442", "LU", "EU", "EUR", ".lu",
                    "Luxembourg", "Luxembourg",
                    "####", "^(\d{4})$", ["352"]))
Country.put(Country("LV", "LVA", "428", "LG", "EU", "LVL", ".lv",
                    "Latvia", "Riga",
                    "LV-####", "^(?:LV)*(\d{4})$", ["371"]))
Country.put(Country("LY", "LBY", "434", "LY", "AF", "LYD", ".ly",
                    "Libya", "Tripolis",
                    "", "", ["218"]))
Country.put(Country("MA", "MAR", "504", "MO", "AF", "MAD", ".ma",
                    "Morocco", "Rabat",
                    "#####", "^(\d{5})$", ["212"]))
Country.put(Country("MC", "MCO", "492", "MN", "EU", "EUR", ".mc",
                    "Monaco", "Monaco",
                    "#####", "^(\d{5})$", ["377"]))
Country.put(Country("MD", "MDA", "498", "MD", "EU", "MDL", ".md",
                    "Moldova", "Chisinau",
                    "MD-####", "^(?:MD)*(\d{4})$", ["373"]))
Country.put(Country("ME", "MNE", "499", "MJ", "EU", "EUR", ".me",
                    "Montenegro", "Podgorica",
                    "#####", "^(\d{5})$", ["382"]))
Country.put(Country("MF", "MAF", "663", "RN", "NA", "EUR", ".gp",
                    "Saint Martin", "Marigot",
                    "### ###", "", ["590"]))
Country.put(Country("MG", "MDG", "450", "MA", "AF", "MGA", ".mg",
                    "Madagascar", "Antananarivo",
                    "###", "^(\d{3})$", ["261"]))
Country.put(Country("MH", "MHL", "584", "RM", "OC", "USD", ".mh",
                    "Marshall Islands", "Majuro",
                    "", "", ["692"]))
Country.put(Country("MK", "MKD", "807", "MK", "EU", "MKD", ".mk",
                    "Macedonia", "Skopje",
                    "####", "^(\d{4})$", ["389"]))
Country.put(Country("ML", "MLI", "466", "ML", "AF", "XOF", ".ml",
                    "Mali", "Bamako",
                    "", "", ["223"]))
Country.put(Country("MM", "MMR", "104", "BM", "AS", "MMK", ".mm",
                    "Myanmar", "Nay Pyi Taw",
                    "#####", "^(\d{5})$", ["95"]))
Country.put(Country("MN", "MNG", "496", "MG", "AS", "MNT", ".mn",
                    "Mongolia", "Ulan Bator",
                    "######", "^(\d{6})$", ["976"]))
Country.put(Country("MO", "MAC", "446", "MC", "AS", "MOP", ".mo",
                    "Macao", "Macao",
                    "", "", ["853"]))
Country.put(Country("MP", "MNP", "580", "CQ", "OC", "USD", ".mp",
                    "Northern Mariana Islands", "Saipan",
                    "", "", ["1-670"]))
Country.put(Country("MQ", "MTQ", "474", "MB", "NA", "EUR", ".mq",
                    "Martinique", "Fort-de-France",
                    "#####", "^(\d{5})$", ["596"]))
Country.put(Country("MR", "MRT", "478", "MR", "AF", "MRO", ".mr",
                    "Mauritania", "Nouakchott",
                    "", "", ["222"]))
Country.put(Country("MS", "MSR", "500", "MH", "NA", "XCD", ".ms",
                    "Montserrat", "Plymouth",
                    "", "", ["1-664"]))
Country.put(Country("MT", "MLT", "470", "MT", "EU", "EUR", ".mt",
                    "Malta", "Valletta",
                    "@@@ ###|@@@ ##", "^([A-Z]{3}\d{2}\d?)$", ["356"]))
Country.put(Country("MU", "MUS", "480", "MP", "AF", "MUR", ".mu",
                    "Mauritius", "Port Louis",
                    "", "", ["230"]))
Country.put(Country("MV", "MDV", "462", "MV", "AS", "MVR", ".mv",
                    "Maldives", "Male",
                    "#####", "^(\d{5})$", ["960"]))
Country.put(Country("MW", "MWI", "454", "MI", "AF", "MWK", ".mw",
                    "Malawi", "Lilongwe",
                    "", "", ["265"]))
Country.put(Country("MX", "MEX", "484", "MX", "NA", "MXN", ".mx",
                    "Mexico", "Mexico City",
                    "#####", "^(\d{5})$", ["52"]))
Country.put(Country("MY", "MYS", "458", "MY", "AS", "MYR", ".my",
                    "Malaysia", "Kuala Lumpur",
                    "#####", "^(\d{5})$", ["60"]))
Country.put(Country("MZ", "MOZ", "508", "MZ", "AF", "MZN", ".mz",
                    "Mozambique", "Maputo",
                    "####", "^(\d{4})$", ["258"]))
Country.put(Country("NA", "NAM", "516", "WA", "AF", "NAD", ".na",
                    "Namibia", "Windhoek",
                    "", "", ["264"]))
Country.put(Country("NC", "NCL", "540", "NC", "OC", "XPF", ".nc",
                    "New Caledonia", "Noumea",
                    "#####", "^(\d{5})$", ["687"]))
Country.put(Country("NE", "NER", "562", "NG", "AF", "XOF", ".ne",
                    "Niger", "Niamey",
                    "####", "^(\d{4})$", ["227"]))
Country.put(Country("NF", "NFK", "574", "NF", "OC", "AUD", ".nf",
                    "Norfolk Island", "Kingston",
                    "", "", ["672"]))
Country.put(Country("NG", "NGA", "566", "NI", "AF", "NGN", ".ng",
                    "Nigeria", "Abuja",
                    "######", "^(\d{6})$", ["234"]))
Country.put(Country("NI", "NIC", "558", "NU", "NA", "NIO", ".ni",
                    "Nicaragua", "Managua",
                    "###-###-#", "^(\d{7})$", ["505"]))
Country.put(Country("NL", "NLD", "528", "NL", "EU", "EUR", ".nl",
                    "Netherlands", "Amsterdam",
                    "#### @@", "^(\d{4}[A-Z]{2})$", ["31"]))
Country.put(Country("NO", "NOR", "578", "NO", "EU", "NOK", ".no",
                    "Norway", "Oslo",
                    "####", "^(\d{4})$", ["47"]))
Country.put(Country("NP", "NPL", "524", "NP", "AS", "NPR", ".np",
                    "Nepal", "Kathmandu",
                    "#####", "^(\d{5})$", ["977"]))
Country.put(Country("NR", "NRU", "520", "NR", "OC", "AUD", ".nr",
                    "Nauru", "Yaren",
                    "", "", ["674"]))
Country.put(Country("NU", "NIU", "570", "NE", "OC", "NZD", ".nu",
                    "Niue", "Alofi",
                    "", "", ["683"]))
Country.put(Country("NZ", "NZL", "554", "NZ", "OC", "NZD", ".nz",
                    "New Zealand", "Wellington",
                    "####", "^(\d{4})$", ["64"]))
Country.put(Country("OM", "OMN", "512", "MU", "AS", "OMR", ".om",
                    "Oman", "Muscat",
                    "###", "^(\d{3})$", ["968"]))
Country.put(Country("PA", "PAN", "591", "PM", "NA", "PAB", ".pa",
                    "Panama", "Panama City",
                    "", "", ["507"]))
Country.put(Country("PE", "PER", "604", "PE", "SA", "PEN", ".pe",
                    "Peru", "Lima",
                    "", "", ["51"]))
Country.put(Country("PF", "PYF", "258", "FP", "OC", "XPF", ".pf",
                    "French Polynesia", "Papeete",
                    "#####", "^((97)|(98)7\d{2})$", ["689"]))
Country.put(Country("PG", "PNG", "598", "PP", "OC", "PGK", ".pg",
                    "Papua New Guinea", "Port Moresby",
                    "###", "^(\d{3})$", ["675"]))
Country.put(Country("PH", "PHL", "608", "RP", "AS", "PHP", ".ph",
                    "Philippines", "Manila",
                    "####", "^(\d{4})$", ["63"]))
Country.put(Country("PK", "PAK", "586", "PK", "AS", "PKR", ".pk",
                    "Pakistan", "Islamabad",
                    "#####", "^(\d{5})$", ["92"]))
Country.put(Country("PL", "POL", "616", "PL", "EU", "PLN", ".pl",
                    "Poland", "Warsaw",
                    "##-###", "^(\d{5})$", ["48"]))
Country.put(Country("PM", "SPM", "666", "SB", "NA", "EUR", ".pm",
                    "Saint Pierre and Miquelon", "Saint-Pierre",
                    "#####", "^(97500)$", ["508"]))
Country.put(Country("PN", "PCN", "612", "PC", "OC", "NZD", ".pn",
                    "Pitcairn", "Adamstown",
                    "", "", ["870"]))
Country.put(Country("PR", "PRI", "630", "RQ", "NA", "USD", ".pr",
                    "Puerto Rico", "San Juan",
                    "#####-####", "^(\d{9})$", ["1-787", "1-939"]))
Country.put(Country("PS", "PSE", "275", "WE", "AS", "ILS", ".ps",
                    "Palestinian Territory", "East Jerusalem",
                    "", "", ["970"]))
Country.put(Country("PT", "PRT", "620", "PO", "EU", "EUR", ".pt",
                    "Portugal", "Lisbon",
                    "####-###", "^(\d{7})$", ["351"]))
Country.put(Country("PW", "PLW", "585", "PS", "OC", "USD", ".pw",
                    "Palau", "Melekeok",
                    "96940", "^(96940)$", ["680"]))
Country.put(Country("PY", "PRY", "600", "PA", "SA", "PYG", ".py",
                    "Paraguay", "Asuncion",
                    "####", "^(\d{4})$", ["595"]))
Country.put(Country("QA", "QAT", "634", "QA", "AS", "QAR", ".qa",
                    "Qatar", "Doha",
                    "", "", ["974"]))
Country.put(Country("RE", "REU", "638", "RE", "AF", "EUR", ".re",
                    "Reunion", "Saint-Denis",
                    "#####", "^((97)|(98)(4|7|8)\d{2})$", ["262"]))
Country.put(Country("RO", "ROU", "642", "RO", "EU", "RON", ".ro",
                    "Romania", "Bucharest",
                    "######", "^(\d{6})$", ["40"]))
Country.put(Country("RS", "SRB", "688", "RI", "EU", "RSD", ".rs",
                    "Serbia", "Belgrade",
                    "######", "^(\d{6})$", ["381"]))
Country.put(Country("RU", "RUS", "643", "RS", "EU", "RUB", ".ru",
                    "Russia", "Moscow",
                    "######", "^(\d{6})$", ["7"]))
Country.put(Country("RW", "RWA", "646", "RW", "AF", "RWF", ".rw",
                    "Rwanda", "Kigali",
                    "", "", ["250"]))
Country.put(Country("SA", "SAU", "682", "SA", "AS", "SAR", ".sa",
                    "Saudi Arabia", "Riyadh",
                    "#####", "^(\d{5})$", ["966"]))
Country.put(Country("SB", "SLB", "090", "BP", "OC", "SBD", ".sb",
                    "Solomon Islands", "Honiara",
                    "", "", ["677"]))
Country.put(Country("SC", "SYC", "690", "SE", "AF", "SCR", ".sc",
                    "Seychelles", "Victoria",
                    "", "", ["248"]))
Country.put(Country("SD", "SDN", "729", "SU", "AF", "SDG", ".sd",
                    "Sudan", "Khartoum",
                    "#####", "^(\d{5})$", ["249"]))
Country.put(Country("SS", "SSD", "728", "OD", "AF", "SSP", "",
                    "South Sudan", "Juba",
                    "", "", ["211"]))
Country.put(Country("SE", "SWE", "752", "SW", "EU", "SEK", ".se",
                    "Sweden", "Stockholm",
                    "SE-### ##", "^(?:SE)*(\d{5})$", ["46"]))
Country.put(Country("SG", "SGP", "702", "SN", "AS", "SGD", ".sg",
                    "Singapore", "Singapur",
                    "######", "^(\d{6})$", ["65"]))
Country.put(Country("SH", "SHN", "654", "SH", "AF", "SHP", ".sh",
                    "Saint Helena", "Jamestown",
                    "STHL 1ZZ", "^(STHL1ZZ)$", ["290"]))
Country.put(Country("SI", "SVN", "705", "SI", "EU", "EUR", ".si",
                    "Slovenia", "Ljubljana",
                    "SI- ####", "^(?:SI)*(\d{4})$", ["386"]))
Country.put(Country("SJ", "SJM", "744", "SV", "EU", "NOK", ".sj",
                    "Svalbard and Jan Mayen", "Longyearbyen",
                    "", "", ["47"]))
Country.put(Country("SK", "SVK", "703", "LO", "EU", "EUR", ".sk",
                    "Slovakia", "Bratislava",
                    "###  ##", "^(\d{5})$", ["421"]))
Country.put(Country("SL", "SLE", "694", "SL", "AF", "SLL", ".sl",
                    "Sierra Leone", "Freetown",
                    "", "", ["232"]))
Country.put(Country("SM", "SMR", "674", "SM", "EU", "EUR", ".sm",
                    "San Marino", "San Marino",
                    "4789#", "^(4789\d)$", ["378"]))
Country.put(Country("SN", "SEN", "686", "SG", "AF", "XOF", ".sn",
                    "Senegal", "Dakar",
                    "#####", "^(\d{5})$", ["221"]))
Country.put(Country("SO", "SOM", "706", "SO", "AF", "SOS", ".so",
                    "Somalia", "Mogadishu",
                    "@@  #####", "^([A-Z]{2}\d{5})$", ["252"]))
Country.put(Country("SR", "SUR", "740", "NS", "SA", "SRD", ".sr",
                    "Suriname", "Paramaribo",
                    "", "", ["597"]))
Country.put(Country("ST", "STP", "678", "TP", "AF", "STD", ".st",
                    "Sao Tome and Principe", "Sao Tome",
                    "", "", ["239"]))
Country.put(Country("SV", "SLV", "222", "ES", "NA", "USD", ".sv",
                    "El Salvador", "San Salvador",
                    "CP ####", "^(?:CP)*(\d{4})$", ["503"]))
Country.put(Country("SX", "SXM", "534", "NN", "NA", "ANG", ".sx",
                    "Sint Maarten", "Philipsburg",
                    "", "", ["599"]))
Country.put(Country("SY", "SYR", "760", "SY", "AS", "SYP", ".sy",
                    "Syria", "Damascus",
                    "", "", ["963"]))
Country.put(Country("SZ", "SWZ", "748", "WZ", "AF", "SZL", ".sz",
                    "Swaziland", "Mbabane",
                    "@###", "^([A-Z]\d{3})$", ["268"]))
Country.put(Country("TC", "TCA", "796", "TK", "NA", "USD", ".tc",
                    "Turks and Caicos Islands", "Cockburn Town",
                    "TKCA 1ZZ", "^(TKCA 1ZZ)$", ["1-649"]))
Country.put(Country("TD", "TCD", "148", "CD", "AF", "XAF", ".td",
                    "Chad", "N'Djamena",
                    "", "", ["235"]))
Country.put(Country("TF", "ATF", "260", "FS", "AN", "EUR", ".tf",
                    "French Southern Territories", "Port-aux-Francais",
                    "", "", [""]))
Country.put(Country("TG", "TGO", "768", "TO", "AF", "XOF", ".tg",
                    "Togo", "Lome",
                    "", "", ["228"]))
Country.put(Country("TH", "THA", "764", "TH", "AS", "THB", ".th",
                    "Thailand", "Bangkok",
                    "#####", "^(\d{5})$", ["66"]))
Country.put(Country("TJ", "TJK", "762", "TI", "AS", "TJS", ".tj",
                    "Tajikistan", "Dushanbe",
                    "######", "^(\d{6})$", ["992"]))
Country.put(Country("TK", "TKL", "772", "TL", "OC", "NZD", ".tk",
                    "Tokelau", "",
                    "", "", ["690"]))
Country.put(Country("TL", "TLS", "626", "TT", "OC", "USD", ".tl",
                    "East Timor", "Dili",
                    "", "", ["670"]))
Country.put(Country("TM", "TKM", "795", "TX", "AS", "TMT", ".tm",
                    "Turkmenistan", "Ashgabat",
                    "######", "^(\d{6})$", ["993"]))
Country.put(Country("TN", "TUN", "788", "TS", "AF", "TND", ".tn",
                    "Tunisia", "Tunis",
                    "####", "^(\d{4})$", ["216"]))
Country.put(Country("TO", "TON", "776", "TN", "OC", "TOP", ".to",
                    "Tonga", "Nuku'alofa",
                    "", "", ["676"]))
Country.put(Country("TR", "TUR", "792", "TU", "AS", "TRY", ".tr",
                    "Turkey", "Ankara",
                    "#####", "^(\d{5})$", ["90"]))
Country.put(Country("TT", "TTO", "780", "TD", "NA", "TTD", ".tt",
                    "Trinidad and Tobago", "Port of Spain",
                    "", "", ["1-868"]))
Country.put(Country("TV", "TUV", "798", "TV", "OC", "AUD", ".tv",
                    "Tuvalu", "Funafuti",
                    "", "", ["688"]))
Country.put(Country("TW", "TWN", "158", "TW", "AS", "TWD", ".tw",
                    "Taiwan", "Taipei",
                    "#####", "^(\d{5})$", ["886"]))
Country.put(Country("TZ", "TZA", "834", "TZ", "AF", "TZS", ".tz",
                    "Tanzania", "Dodoma",
                    "", "", ["255"]))
Country.put(Country("UA", "UKR", "804", "UP", "EU", "UAH", ".ua",
                    "Ukraine", "Kiev",
                    "#####", "^(\d{5})$", ["380"]))
Country.put(Country("UG", "UGA", "800", "UG", "AF", "UGX", ".ug",
                    "Uganda", "Kampala",
                    "", "", ["256"]))
Country.put(Country("UM", "UMI", "581", "", "OC", "USD", ".um",
                    "United States Minor Outlying Islands", "",
                    "", "", ["1"]))
Country.put(Country("US", "USA", "840", "US", "NA", "USD", ".us",
                    "United States", "Washington",
                    "#####-####", "^(\d{9})$", ["1"]))
Country.put(Country("UY", "URY", "858", "UY", "SA", "UYU", ".uy",
                    "Uruguay", "Montevideo",
                    "#####", "^(\d{5})$", ["598"]))
Country.put(Country("UZ", "UZB", "860", "UZ", "AS", "UZS", ".uz",
                    "Uzbekistan", "Tashkent",
                    "######", "^(\d{6})$", ["998"]))
Country.put(Country("VA", "VAT", "336", "VT", "EU", "EUR", ".va",
                    "Vatican", "Vatican City",
                    "", "", ["379"]))
Country.put(Country("VC", "VCT", "670", "VC", "NA", "XCD", ".vc",
                    "Saint Vincent and the Grenadines", "Kingstown",
                    "", "", ["1-784"]))
Country.put(Country("VE", "VEN", "862", "VE", "SA", "VEF", ".ve",
                    "Venezuela", "Caracas",
                    "####", "^(\d{4})$", ["58"]))
Country.put(Country("VG", "VGB", "092", "VI", "NA", "USD", ".vg",
                    "British Virgin Islands", "Road Town",
                    "", "", ["1-284"]))
Country.put(Country("VI", "VIR", "850", "VQ", "NA", "USD", ".vi",
                    "U.S. Virgin Islands", "Charlotte Amalie",
                    "", "", ["1-340"]))
Country.put(Country("VN", "VNM", "704", "VM", "AS", "VND", ".vn",
                    "Vietnam", "Hanoi",
                    "######", "^(\d{6})$", ["84"]))
Country.put(Country("VU", "VUT", "548", "NH", "OC", "VUV", ".vu",
                    "Vanuatu", "Port Vila",
                    "", "", ["678"]))
Country.put(Country("WF", "WLF", "876", "WF", "OC", "XPF", ".wf",
                    "Wallis and Futuna", "Mata Utu",
                    "#####", "^(986\d{2})$", ["681"]))
Country.put(Country("WS", "WSM", "882", "WS", "OC", "WST", ".ws",
                    "Samoa", "Apia",
                    "", "", ["685"]))
Country.put(Country("YE", "YEM", "887", "YM", "AS", "YER", ".ye",
                    "Yemen", "Sanaa",
                    "", "", ["967"]))
Country.put(Country("YT", "MYT", "175", "MF", "AF", "EUR", ".yt",
                    "Mayotte", "Mamoudzou",
                    "#####", "^(\d{5})$", ["262"]))
Country.put(Country("ZA", "ZAF", "710", "SF", "AF", "ZAR", ".za",
                    "South Africa", "Pretoria",
                    "####", "^(\d{4})$", ["27"]))
Country.put(Country("ZM", "ZMB", "894", "ZA", "AF", "ZMK", ".zm",
                    "Zambia", "Lusaka",
                    "#####", "^(\d{5})$", ["260"]))
Country.put(Country("ZW", "ZWE", "716", "ZI", "AF", "ZWL", ".zw",
                    "Zimbabwe", "Harare",
                    "", "", ["263"]))
Country.put(Country("CS", "SCG", "891", "YI", "EU", "RSD", ".cs",
                    "Serbia and Montenegro", "Belgrade",
                    "#####", "^(\d{5})$", ["381"]))
Country.put(Country("AN", "ANT", "530", "NT", "NA", "ANG", ".an",
                    "Netherlands Antilles", "Willemstad",
                    "", "", ["599"]))
