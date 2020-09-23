import pandas as pd
my_url = 'https://raw.githubusercontent.com/taroyabuki/rp/master/data/exam.json'
my_data = pd.read_json(my_url)
#my_data = pd.read_json('exam.json') # （ファイルを使う場合）
my_data
#>   name  english  math gender
#> 0    A       60    70      f
#> 1    B       90    80      m
#> 2    C       70    90      m
#> 3    D       90   100      f

from urllib.request import urlopen
import xml.etree.ElementTree as ET
import pandas as pd

my_url = 'https://raw.githubusercontent.com/taroyabuki/rp/master/data/exam.xml'
with urlopen(my_url) as f:
    my_tree = ET.parse(f)       # XMLデータの読み込み

#my_tree = ET.parse('exam.xml') # （ファイルを使う場合）
my_ns = '{https://www.example.net/ns/1.0}' # 名前空間

my_records = my_tree.findall(f'.//{my_ns}record')

def f(record):
    my_dic1 = record.attrib # 属性を取り出す．
    # 子要素の名前と内容のペアを辞書にする．
    my_dic2 = {child.tag.replace(my_ns, ''):child.text for child in list(record)}
    return {**my_dic1, **my_dic2} # 辞書を結合する．

my_data = pd.DataFrame([f(record) for record in my_records])
my_data['english'] = pd.to_numeric(my_data['english'])
my_data['math']    = pd.to_numeric(my_data['math'])
my_data
#>    english  math gender name
#> 0       60    70      f    A
#> 1       90    80      m    B
#> 2       70    90      m    C
#> 3       90   100      f    D

