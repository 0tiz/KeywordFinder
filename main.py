
import saveHtml
import keywordfinder
url = "https://www.spiegel.de/"
path = "./cache/"
saveHtml.saveUrl(url)
keywordfinder.readFiles(path)