"""
Iegūt ziņas, izmantojot RSS plūsmu no google.lv
"""
import feedparser

#1) Norādīt RSS plūsmas URL(vietrādis), kas satur google.lv ziņas

rss_url='https://news.google.com/rss?hl=lv&gl=LV&ceid=LV:lv'
#2)lejupieladeju un analizeju RSS plūsmu
feed=feedparser.parse(rss_url)
for entry in feed.entries:
    print("Virsraksts", entry.title)
    print("Saite",entry.link)
    print("/n")