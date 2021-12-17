# coding=utf8
import os
# os.system("fsutil file createnew background.jpg 10000")
image = open(r'background.jpg', 'w', encoding="utf-8")
data = open(r'black_jack.jpg', 'r', encoding="utf8", errors='ignore')

data_to_write = data.read()
image.write(data_to_write)
