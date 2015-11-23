#Extract data from XML
'''This program is reading xml from the url, extracting the "count" tags present in it, and giving total sum of them. '''

import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_188471.xml'
uh = urllib.urlopen(url)
xml_read = uh.read()
print type(uh)
#print xml_read
tree = ET.fromstring(xml_read)
count_tag_list = tree.findall('.//count')
sumCounts = 0
for count in count_tag_list:
    sumCounts += int(count.text)
    
print sumCounts
