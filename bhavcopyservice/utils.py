import datetime
import csv, json, zipfile
import os, shutil

def parseCSVToJSON(path):
    with open(path, 'rU') as csvf:
        data = []
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            data.append(row)
    return json.dumps(data)

def unzipAndSave(zipLocation, fileDir):
    with zipfile.ZipFile(zipLocation, 'r') as zip_ref:
        zip_ref.extractall(fileDir)

def writeToZip(zipLocation, data):
    with open(zipLocation, 'wb') as file:
        file.write(data)

def cleanUpDirectory(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def generateBhavSourceUrl(baseUrl):
    return baseUrl + '/EQ' + getcurrentDate() + '_CSV.ZIP'

def getcurrentDate():
    return datetime.date.today().strftime('%d%m%y')