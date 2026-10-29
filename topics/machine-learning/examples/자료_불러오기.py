"""노트북에서 숫자 상수만 읽음. 노트북 코드는 실행하지 않음."""
from pathlib import Path
import ast, json, os
from urllib.request import urlopen
import numpy as np
import pandas as pd

BASE = "https://raw.githubusercontent.com/rickiepark/hg-mldl/master/"
def read_source(name):
    local = os.environ.get("ML_NOTEBOOK_DIR")
    if local:
        return (Path(local) / name).read_bytes()
    with urlopen(BASE + name, timeout=30) as response:
        return response.read()

def arrays(notebook, names):
    result = {}
    for cell in json.loads(read_source(notebook))["cells"]:
        if cell["cell_type"] != "code":
            continue
        try:
            tree = ast.parse("".join(cell["source"]))
        except SyntaxError:
            continue
        for node in tree.body:
            if not isinstance(node, ast.Assign) or len(node.targets) != 1:
                continue
            target = node.targets[0]
            if not isinstance(target, ast.Name) or target.id not in names:
                continue
            value = node.value
            if isinstance(value, ast.Call) and isinstance(value.func, ast.Attribute) and value.func.attr == "array":
                value = value.args[0]
            try:
                result[target.id] = np.array(ast.literal_eval(value))
            except (ValueError, TypeError):
                continue
    if set(result) != set(names):
        raise ValueError("필요한 데이터 상수를 찾지 못함")
    return result

def fish():
    return arrays("1-3.ipynb", ["bream_length", "bream_weight", "smelt_length", "smelt_weight"])
def perch():
    return arrays("3-1.ipynb", ["perch_length", "perch_weight"])
def perch_frame():
    import io
    return pd.read_csv(io.BytesIO(read_source("perch_full.csv")), skipinitialspace=True)
