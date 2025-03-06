import openpyxl

def read_txt():
    all_results = []
    file_path = "/Users/alex/登陆数据.xlsx"  # 替换为你的文件路径
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active  # 获取活动工作表
    for row in sheet.iter_rows(min_row=2, values_only=True):
        # 将每一行的数据存储在一个小列表中
        result = list(row)
        all_results.append(result)  # 将小列表添加到大列表中

    workbook.close()
    return all_results

data = read_txt()
print(data)