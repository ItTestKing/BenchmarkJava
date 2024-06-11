import os
import xml.etree.ElementTree as ET
import pandas as pd
import shutil

def get_cwe():
    # 指定文件夹路径
    folder_path = '../testcode'
    # 指定输出Excel文件的路径
    output_excel_path = 'output_results.xlsx'

    # 初始化一个空的字典来存储数据
    data = {
        'Filename': [],
        'Test Number': [],
        'Vulnerability': [],
        'CWE': []
    }

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件扩展名是否为.xml
        if filename.endswith('.xml'):
            file_path = os.path.join(folder_path, filename)
            # 解析XML文件
            tree = ET.parse(file_path)
            root = tree.getroot()

            # 提取所需信息
            test_number = root.find('test-number').text if root.find('test-number') is not None else ''
            vulnerability = root.find('vulnerability').text if root.find('vulnerability') is not None else ''
            cwe = root.find('cwe').text if root.find('cwe') is not None else ''

            # 将提取的数据添加到字典中
            data['Filename'].append(filename.replace("xml","java"))
            data['Test Number'].append(test_number)
            data['Vulnerability'].append(vulnerability)
            data['CWE'].append(cwe)

    # 将字典转换为pandas DataFrame
    df = pd.DataFrame(data)

    # 将DataFrame保存到Excel文件
    df.to_excel(output_excel_path, index=False)

    print(f"Results have been saved to {output_excel_path}")

def good_or_bad(name):
    # Excel文件路径
    excel_path = '{}\{}.xlsx'.format(name,name)
    # Excel中包含文件名的列的列名或索引，这里假设为第一列，索引为0
    column_index = 0
    # 源目录，即文件当前所在的目录
    source_dir = 'testcode'
    # 目标目录，即你想要复制文件到的目录
    target_dir = '{}'.format(name)

    # 读取Excel文件
    df = pd.read_excel(excel_path)

    # 确保目标目录存在
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # 遍历第一列中的所有文件名
    for filename in df.iloc[:, column_index]:
        # 构建文件的完整源路径
        src_file_path = os.path.join(source_dir, filename)
        # 构建文件的完整目标路径
        dst_file_path = os.path.join(target_dir, filename)

        # 检查文件是否存在
        if os.path.exists(src_file_path):
            # 复制文件
            shutil.copy(src_file_path, dst_file_path)
            print(f"Copied: {filename}")
        else:
            print(f"File not found: {filename}")
if __name__ == '__main__':
    # sum()
    good_or_bad("bad")