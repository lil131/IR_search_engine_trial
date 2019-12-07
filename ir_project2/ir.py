import csv
import requests
from lxml import html


#w = open('unstructuredata.txt','w')
#w1 = open('description.txt','w')
w2 = open('irdata.txt','w')
#csv_storyline = open('story.csv', 'w', newline='')
#csv_poster = open('poster.csv', 'w', newline='')
#csv_title = open('title.csv', 'w', newline='')
#csv_descrip = open('description.csv', 'w', newline='')
csv_database = open('datahouse.csv', 'w', newline='')
dic_poster = {}
dic_descirp = {}
dic_title = {}
dic_story = {}
#writer_storyline = csv.writer(csv_storyline)
#writer_poster = csv.writer(csv_poster)
#writer_desc = csv.writer(csv_descrip)
#writer_title = csv.writer(csv_title)
writer_data = csv.writer(csv_database)

csv_file = csv.reader(open('title.ratings.csv','r'))
next(csv_file, None)
count = 1
for line in csv_file:


    web = 'https://www.imdb.com/title/' + line[0]
    rate = line[1]
    #print(web)
    htmls = requests.get(web)
    etree_html = html.etree.HTML(htmls.text)
    storyline = etree_html.xpath('//*[@id="titleStoryLine"]/div[1]/p/span/text()')
    title = etree_html.xpath('//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[2]/div[2]/h1/text()')
    posterlink = etree_html.xpath('//*[@id="title-overview-widget"]/div[1]/div[3]/div[1]/a/img/@src')
    description = etree_html.xpath('/html/head/meta[15]/@content')


    if title:
        title = title[0].rstrip('\xa0')
    else:
        title = ' '
    # dic_title[line[0]]= title
    # dic_descirp[line[0]] = description[0]
    # dic_poster[line[0]] = posterlink[0]
    # dic_story[line[0]] = storyline[0]
    if description:
        descript = description[0]
        #writer_desc.writerow([line[0],description[0]])
        #w1.write('<titleid> ' + line[0] + '\n')
        #w1.write('<description> ' + description[0] + '\n')
    else:
        descript = ' '
    if posterlink:
        poster = posterlink[0]
    else:
        poster = 'https://thefittingsource.com/wp-content/uploads/2017/12/temp-inventory-landing.jpg'
        #writer_poster.writerow([line[0], posterlink[0]])
    if storyline:
        story = storyline[0]
        #writer_storyline.writerow([line[0], storyline[0]])
        #w.write('<titleid> ' + line[0] + '\n')
        #w.write('<storyline> ' + storyline[0] + '\n')
    else:
        story = ' '
    #writer_title.writerow([line[0], title])
    writer_data.writerow([line[0], title, rate, descript, story, web, poster])
    content = descript + ' ' + story + ' ' + (title + ' ') * 4
    w2.write('<titleid> ' + line[0] + '</titleid>' + '\n')
    w2.write('<content> ' + content + '</content>' + '\n')

    # for each in content:
    #     print(each)
    count += 1
    if count % 200 == 2:

        print(title)
        print(storyline)

    # print html.text

#csv_title.close()
csv_file.close()
#csv_storyline.close()
#csv_descrip.close()
#csv_poster.close()
csv_database.close()
#w.close()
#w1.close()
w2.close()

