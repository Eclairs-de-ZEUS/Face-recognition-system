from bs4 import BeautifulSoup as bs
import urllib.request
import unidecode

def detect_sign(month: int, day: int) -> str:
    sign = ""
    if month == 1:
        if 0 <= day <= 20:
            sign = "capricorne"
        else:
            sign = "verseau"
    if month == 2:
        if 0 <= day <= 19:
            sign = "verseau"
        else:
            sign = "poissons"
    if month == 3:
        if 0 <= day <= 20:
            sign = "poissons"
        else:
            sign = "belier"
    if month == 4:
        if 0 <= day <= 19:
            sign = "belier"
        else:
            sign = "taureau"
    if month == 5:
        if 0 <= day <= 20:
            sign = "taureau"
        else:
            sign = "gemeaux"
    if month == 6:
        if 0 <= day <= 21:
            sign = "gemeaux"
        else:
            sign = "cancer"
    if month == 7:
        if 0 <= day <= 22:
            sign = "cancer"
        else:
            sign = "lion"
    if month == 8:
        if 0 <= day <= 22:
            sign = "lion"
        else:
            sign = "vierge"
    if month == 9:
        if 0 <= day <= 22:
            sign = "vierge"
        else:
            sign = "balance"
    if month == 10:
        if 0 <= day <= 23:
            sign = "balance"
        else:
            sign = "scorpion"
    if month == 11:
        if 0 <= day <= 22:
            sign = "scorpion"
        else:
            sign = "sagittaire"
    if month == 12:
        if 0 <= day <= 22:
            sign = "saggitaire"
        else:
            sign = "capricorne"
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
