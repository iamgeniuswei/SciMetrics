
import pandas as pd

def format_str(to_format_str: str) -> str:
    """
    格式化作者名称列表，部分使用','分割，或者包含空格，需要格式化成'A;B;C;D'的标准形式
    @param author_str:
    """
    if pd.isnull(to_format_str):
        return None
    formated_str = to_format_str.replace(' ', '').replace(',', ';').rstrip(';')
    return formated_str