import os
import xml.etree.ElementTree as ET
import pandas as pd

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
df.to_excel(results, index=False)

print(f"Results have been saved to {output_excel_path}")