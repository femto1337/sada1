api_id   = '1588403'
api_hash = '7c8874eadd64b088e2e797f39c215974'
username = 'EzPosterBot'

from selenium import webdriver
import time
from time import gmtime, strftime
import re
from telethon.sync import TelegramClient, events

act_band = [] 

band_browser = webdriver.Chrome()
band_browser.get("https://csgo.band/")
time.sleep(1)

options = webdriver.ChromeOptions()
options.add_extension('proxy.zip')

band1_browser = webdriver.Chrome(chrome_options=options)
band1_browser.get("https://csgo.band/")
input('После авторизации нажмите любую клавишу.')

def get_promo(promo, site):
    if site == 'run':
        promo = promo.replace('ран', '')
        promo = promo.replace('run', '')
        promo = promo.replace('Run', '')
        promo = promo.replace('hfy', '')
        promo = promo.replace('HFY', '')
        promo = promo.replace('-', '')
        promo = promo.replace('#ob', '')
        promo = promo.replace('#sp', '')
        promo = promo.replace(r"\s\(.*\)\s","")
        promo = re.sub(r'\([^)]*\)', '', promo)
        promo = promo.lstrip(' ') 
        promo = promo.rstrip(' ') 
    elif site == 'band':
        promo = promo.replace('бенд', '')
        promo = promo.replace('БЕНД', '')
        promo = promo.replace('Бэнд', '')
        promo = promo.replace('band', '')
        promo = promo.replace('Band', '')
        promo = promo.replace('BAND', '')
        promo = promo.replace('BANd', '')
        promo = promo.replace('-', '')
        promo = promo.replace('#ob', '')
        promo = promo.replace('#sp', '')
        promo = promo.replace(r"\s\(.*\)\s","")
        promo = re.sub(r'\([^)]*\)', '', promo)
        promo = promo.lstrip(' ') 
        promo = promo.rstrip(' ') 
        
    return promo


def activate_promo(promo, site):
    print(f'\n\n{strftime("%H:%M:%S", gmtime())} {site} Активирую промокод {promo} \n{strftime("%H:%M:%S", gmtime())} {site} Активирую промокод {promo} \n\n')
    if site == 'band':
        if not promo in act_band:
            band_browser.find_element_by_xpath('//*[@id="profile-promo-input"]').send_keys(promo)
            band1_browser.find_element_by_xpath('//*[@id="profile-promo-input"]').send_keys(promo)
            time.sleep(0.2)
            band_browser.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/button').click()
            band1_browser.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/button').click()
            time.sleep(7)
            act_band.append(promo)
        else:
            print('Промокод уже был активирован')


with TelegramClient(username, api_id, api_hash) as client:
    promchen = str(client.get_entity('https://t.me/Promchen').id)
    csgoband = str(client.get_entity('https://t.me/csgoband').id)
    chepsa = str(client.get_entity('https://t.me/ChepsaBand').id)
    

    @client.on(events.NewMessage())
    async def handler(event):
        message = event.message.message
        message_id = str(event.message.to_id)
        message_len = len(message.split(' '))
        promo = get_promo(message, 'band')
        activate_promo(promo, 'band')



    client.run_until_disconnected()
