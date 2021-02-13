from django.apps import AppConfig
from threading import Thread
from urllib.request import urlopen, Request
from bhavcopyservice.redis_client import redis_client
import bhavcopyservice.utils as utils
import schedule, time

class BhavcopyserviceConfig(AppConfig):
    name = 'bhavcopyservice'

def triggerDatabaseSync():
    baseUrl = 'http://www.bseindia.com/download/BhavCopy/Equity'
    zipLocation = './tmp/equity_bhav.zip'
    fileDir = './tmp'

    print('Checkpoint: Database Sync Initiated!')

    req = Request(utils.generateBhavSourceUrl(baseUrl), headers={'User-Agent': 'PostmanRuntime/7.26.8'})
    try:
        response = urlopen(req)
        data = response.read()

        print('Checkpoint: Fetched sources successfully!')

        utils.writeToZip(zipLocation, data)
        utils.unzipAndSave(zipLocation, fileDir)

        r = redis_client()
        r.set("Equities", utils.parseCSVToJSON(fileDir + '/EQ' + utils.getcurrentDate() + '.CSV'))
        
    except Exception as e:
        print('Oops! Failed to fetch sources. Reason :', e)

    print('Checkpoint: Database sync complete!')
    utils.cleanUpDirectory(fileDir)

def scheduleSync():
    schedule.every().monday.at('18:00').do(triggerDatabaseSync)
    schedule.every().tuesday.at('18:00').do(triggerDatabaseSync)
    schedule.every().wednesday.at('18:00').do(triggerDatabaseSync)
    schedule.every().thursday.at('18:00').do(triggerDatabaseSync)
    schedule.every().friday.at('18:00').do(triggerDatabaseSync)
    while True:
        schedule.run_pending()
        time.sleep(1)

def detachAndRun():
    thread = Thread(target = scheduleSync, args = ())
    thread.start()