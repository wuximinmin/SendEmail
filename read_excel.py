import pandas as pd


def read_excel_file(excel_file_path):
    try:
        # 假设列名位于第二行，所以header=1
        df = pd.read_excel(excel_file_path, sheet_name=0, header=1)  # sheet_name=0, header=1
        return df
    except Exception as e:
        print(f"读取Excel文件时出错: {e}")
        return None
