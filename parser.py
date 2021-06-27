from json import encoder
from os import error
from bs4 import BeautifulSoup
import requests
import csv


def parse(URL):
    response = requests.get(URL)
    file_name = str(URL[37:-5])
    finish_file_name = file_name.replace('/', '_')+'.csv'

    soup = BeautifulSoup(response.text, 'lxml')

    click_area = soup.find('div', id='click_area')
    text_original = click_area.find_all('div', class_='original')
    text_translate = click_area.find_all('div', class_='translate')
    file(finish_file_name, text_original, text_translate)


def file(name, text_original, text_translate):
    with open(name, mode='w+', newline='', encoding='utf-8')as test1:
        test1 = csv.writer(test1, delimiter=',',
                           quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(text_original)):
            test1.writerow(text_original[i])
            test1.writerow(text_translate[i])


parse('https://www.amalgama-lab.com/songs/j/juice_wrld/robbery.html')
parse('https://www.amalgama-lab.com/songs/h/hurlement/inquisition.html')
parse('https://www.amalgama-lab.com/songs/b/billie_eilish/lovely.html')
parse('https://www.amalgama-lab.com/songs/d/dr_dre/i_need_a_doctor.html')
