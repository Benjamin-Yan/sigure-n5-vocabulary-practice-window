# sigure-n5-vocabulary-practice-window
You can use this program to practice N5 vocabularies.

---

> To be completed! (施工中)

製作於 `2021.10.1`

URL
- [Main](https://www.sigure.tw)
- [N5 vocabulary](https://www.sigure.tw/learn-japanese/vocabulary/n5/)
- [Copyright](https://www.sigure.tw/learn-japanese/notice/terms-of-service.php#ipc)
    > 未經本網站書面或文字授權，您不得複製、重製、改作、再利用、下載、列印、修改、發布、出版、廣播、傳送、出售、出租、轉移、分發、散播或以任何非於本網站上之其他方式利用本網站的內容。
⇒ 雖然本專案無任何營利行為，且只有用於教學研究用途，但是由於未經過授權，所以將來有可能會於功能完整後轉為 private.

Todo
1. 擴充到*ALL*單元
2. 重新整理程式碼
3. 改成`物件導向`寫法
4. 整合之前打好在手機上的說明文件
5. 擴充到*N4*

---

暫時小記
`kan_list4 = list(sel4.loc[0: 16, "日文"]) + list(sel4.loc[17: , "假名"])`中，會結合假名是因為要針對外來語所做的調整。

```python
from functions import some_function  # 引入副程式的檔案

# 定義主要視窗
def main():
    # 創建主視窗
    root = tk.Tk()
    
    # 調用副程式
    some_function()
    
    # 啟動主視窗的事件迴圈
    root.mainloop()

# 呼叫main函數來執行程式
if __name__ == "__main__":
    main()
```

