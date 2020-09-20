names_lang = {
    'en': ["Harry Potter and the Philosopher's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Prisoner of Azkaban", "Harry Potter and the Goblet of Fire", "Harry Potter and the Order of the Phoenix", "Harry Potter and the Half-Blood Prince", "Harry Potter and the Deathly Hallows", "The Harry Potter Series"],
    'es': ["Harry Potter y la Piedra Filosofal", "Harry Potter y la Cámara Secreta", "Harry Potter y el Prisionero de Azkaban", "Harry Potter y el Cáliz de Fuego", "Harry Potter y la Orden del Fénix", "Harry Potter y el Misterio del Príncipe", "Harry Potter y las Reliquias de la Muerte", "La Saga de Harry Potter"]
}
def search_in_hp(query, book, lang):
    names = names_lang[lang]
    sorcerer = open(f"{lang}/1.txt").read()
    chamber = open(f"{lang}/2.txt").read()
    prisoner = open(f"{lang}/3.txt").read()
    goblet = open(f"{lang}/4.txt").read()
    order = open(f"{lang}/5.txt").read()
    prince = open(f"{lang}/6.txt").read()
    hallows = open(f"{lang}/7.txt").read()
    _all = ' '.join([sorcerer, chamber, prisoner, goblet, order, prince, hallows])

    books = [sorcerer, chamber, prisoner, goblet, order, prince, hallows, _all]
    b = books[book]
    return b.count(query.lower()), names[book]
