from lxml import html
from lxml.etree import XPath

url = "http://cytatybaza.pl/autorzy/karl-heinrich-marx-karol-marks.html?ppn={}"
zakres = range(1, 13)
quotes_xpath = XPath("//p[@class='qt']/text()")

quotes = []

for pageno in zakres:
    sauce = html.parse(url.format(pageno))
    quotes.extend(quotes_xpath(sauce))

print(quotes)
