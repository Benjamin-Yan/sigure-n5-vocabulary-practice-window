"""
此程式用於爬取並處理所有單字的資料。

作者: 太陽餅
日期: 3.6.2024

"""
import pandas as pd

N5CLASSNUM = 21
n5data = [[] for _ in range(N5CLASSNUM)] # 分課資料用
n5kans = list()
n5dic = [{} for _ in range(N5CLASSNUM)] # 考試字典(分課,對答案)

class VocabularyClass:
    def __init__(self, url, index_to_change, class_idx):
        self.url = "https://www.sigure.tw/learn-japanese/vocabulary/" + url
        self.index_to_change = index_to_change
        self.get_all_vocabulary(class_idx)
    
    def get_all_vocabulary(self, class_idx):
        _source = pd.read_html(self.url)[0]
        kan_list = list(_source.loc[: self.index_to_change-2, "日文"]) + list(_source.loc[self.index_to_change-1: , "假名"])
        jap_list = list(_source.loc[: self.index_to_change-2, "假名"]) + list(_source.loc[self.index_to_change-1: , "日文"])
        chi_list = list(_source.loc[: , "中文"])

        for i, j in zip(jap_list, kan_list):
            n5data[class_idx-1].append(f"{i} ({j})")
        n5kans.append(chi_list)
        n5dic[class_idx-1] = dict(zip(jap_list, chi_list))


def get_n5_data():
    """
    Initial the data of N5 vocabulary.

    Parameters:
    None # 未來=> x (int): 表示n5
    
    Returns:
    None (n5data, n5kans, n5dic are global variable, so after initialization, you can use it directly in main)
    """
    n5_4 = VocabularyClass("n5/04-noun-job.php", 18, 4)
    n5_5 = VocabularyClass("n5/05-noun-place.php", 49, 5)


# get_n5_data()
# print(n5data)

