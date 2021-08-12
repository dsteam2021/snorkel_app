# snorkel_app

## Cách viết LFs:
* Tạo file LFs với nhãn tương ứng: n{số nhãn theo LabelEncoder}_tên nhãn.py (ví dụ: n0_bat_dong_san.py)
* Comment trên đầu các LFs tên của mình để dễ quản lý
* Có một list nhỏ ở cuối file, điền tên lfs bạn viết vào list đó là được (ví dụ: lfs = [keyword_0])
* Hãy nhớ Try-Catch để tránh lỗi nhé
```
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
```
## Thêm params:
* Chỉnh trong file parameter.py
## Cách chạy:
```
python main.py --data_path {đường dẫn đến file chứa dữ liệu, default='data/'} --file_name {tên file trong data_path, default: 'train.csv'}
```
