#----import----#
import pandas as pd
import html5lib
from openpyxl import load_workbook
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#------------------------------------
dfs = pd.read_html('https://rate.bot.com.tw/xrt?Lang=zh-TW')
currency = dfs[0]
#------------------------------------
#去除不必要的欄位
currency = currency.ix[:, 0:5]

#------------------------------------
#修正欄位名稱
#[u'欄位名稱']用意：將欄位設成unicode
currency.columns = [u'幣別', u'現金匯率-本行買入', u'現金匯率-本行賣出', u'即期匯率-本行買入', '即期匯率-本行賣出']

#------------------------------------
#修正幣別欄位
currency[u'幣別'] = currency[u'幣別'].str.extract('\((\w+)\)')
print(currency)

#------------------------------------
#將爬下來的資料存成excel檔
try:
    writer = pd.ExcelWriter('other file/currency.xlsx', engine = 'openpyxl')
    writer.book = load_workbook('other file/currency.xlsx')
    currency.to_excel(writer, sheet_name = 'Sheet 2')
    writer.save()
    writer.close()
except Exception as e:
    print(e)
    writer = pd.ExcelWriter('other file/currency.xlsx', engine = 'openpyxl')
    currency.to_excel(writer, sheet_name = 'Sheet 1')
    writer.save()
    writer.close()
