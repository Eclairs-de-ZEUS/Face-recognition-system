from bs4 import BeautifulSoup as bs
import urllib.request
import unidecode

def detect_sign(month: int, day: int) -> str:
    sign = ""
    if month == 1:
        sign = "capricorne" if 0 <= day <= 20 else "verseau"
    if month == 2:
        sign = "verseau" if 0 <= day <= 19 else "poissons"
    if month == 3:
        sign = "poissons" if 0 <= day <= 20 else "belier"
    if month == 4:
        sign = "belier" if 0 <= day <= 19 else "taureau"
    if month == 5:
        sign = "taureau" if 0 <= day <= 20 else "gemeaux"
    if month == 6:
        sign = "gemeaux" if 0 <= day <= 21 else "cancer"
    if month == 7:
        sign = "cancer" if 0 <= day <= 22 else "lion"
    if month == 8:
        sign = "lion" if 0 <= day <= 22 else "vierge"
    if month == 9:
        sign = "vierge" if 0 <= day <= 22 else "balance"
    if month == 10:
        sign = "balance" if 0 <= day <= 23 else "scorpion"
    if month == 11:
        sign = "scorpion" if 0 <= day <= 22 else "sagittaire"
    if month == 12:
        sign = "sagittaire" if 0 <= day <= 22 else "capricorne"
    return sign

def horoscope(sign: str) -> str:
    url = 'https://www.lhoroscope.com/horoscope-general/horoscope-' + sign + '-du-jour.asp'
    page = urllib.request.urlopen(url, timeout = 8)
    soup = bs(page, features="html.parser")
    sign = soup.find_all('div', {'class':'panel-body text-justify'})
    for e in sign:
        e = e.text
        e = e.replace('\n', ' ')
        e = e.replace('\t', '')
        e = e.replace('\r', ' ')
    return (e)
