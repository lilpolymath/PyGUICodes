from urllib import request

file_link = "http://spatialkeydocs.s3.amazonaws.com/FL_insurance_sample.csv.zip" #Goes here

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split('\\n') #this
    dest_url = r'goog.csv'
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + "\n") #and this
    fx.close()

download_stock_data(file_link)
