from PIL import Image
import pytesseract
import pandas as pd

# 設定 Tesseract 的安裝路徑


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # 使用原始字符串
# 開啟圖片
img = Image.open('S29343763.jpg')

# 使用 Tesseract 進行文字辨識
text = pytesseract.image_to_string(img, lang='chi_tra')  # 設定語言為繁體中文

# 將辨識的文字轉換成 DataFrame
data = {'Text': [text]}
df = pd.DataFrame(data)

# 將 DataFrame 寫入 Excel 檔案
df.to_excel('output.xlsx', index=False)

print('文字辨識結果已轉換成 Excel 檔案')