import sys
import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/' + ' '.join(sys.argv[1:]))
res.raise_for_status()
# to raise the status code if any error occurs
wiki = bs4.BeautifulSoup(res.text, "html.parser")
for i in wiki.select('p'):
    # append scraped data to .txt file
    sample = open('samplefile.txt', 'a')
    print(i.getText(), file = sample)
    sample.close()