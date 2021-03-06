# snorkel_app

## Cấu trúc
```
├── data                        # Folder dữ liệu
|   ├── train.csv
|   ├── test.csv
├── LFs                         # Folder chứa Labeling Functions
|   ├── n0_bat_dong_san.py
|   ├── ...
|   └── util.py
├── data.py                     # Module load dữ liệu (có thể thêm xử lý, v.v...)
├── main.py                     # Train, Analyst
├── parameter.py                # Module chứa các tham số cần khi chạy
└── README.md
```

## Cách viết LFs:
* Tạo file LFs với nhãn tương ứng: n{số nhãn theo LabelEncoder}_tên nhãn.py (ví dụ: n0_bat_dong_san.py)
* Comment trên đầu các LFs tên của mình để dễ quản lý
* Tên LFs nên đặt dễ hiểu, và gán số nhãn ở cuối cho dễ quản lý
* Có một list nhỏ ở cuối file, điền tên lfs bạn viết vào list đó là được (ví dụ: lfs = [keyword_0])
* Hãy nhớ Try-Catch để tránh lỗi nhé
```
from . import *

# Huy
@labeling_function()
def keyword_0(x):
    try:
        if x['check_btype'] == 'Bất động sản':
            keyword = ['tiền thuế', 'phí']
            keyword.extend(convert(keyword))
            for i in keyword:
                if i in x['name_cleaned']: 
                    return 0
        elif x['check_btype'] != 'Bất động sản':
            pass
    except: 
        # print(x)
        pass
        
    return -1

lfs = [keyword_0]

def get_lfs():
    return lfs
```
## Thêm params:
* Chỉnh trong file parameter.py
## Cách chạy:
```
python main.py --data_path {đường dẫn đến file chứa dữ liệu, default='data/'} --file_name {tên file trong data_path, default: 'train.csv'}
```
