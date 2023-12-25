#RegExpr25.py
#This program k? means searching zero k or one k  only.
import re
mat=re.finditer("k?" , "kvkkvkkkvkv")
print("="*50)
for m in mat:
	print("start index:{}   End Index:{}  Value:{}".format(m.start(),m.end(),m.group()))
print("="*50)

"""
E:\KVR-PYTHON-9AM\REGULAR EXPRESSIONS>py RegExpr26.py
==================================================
start index:0   End Index:1  Value:k
start index:1   End Index:1  Value:
start index:2   End Index:3  Value:k
start index:3   End Index:4  Value:k
start index:4   End Index:4  Value:
start index:5   End Index:6  Value:k
start index:6   End Index:7  Value:k
start index:7   End Index:8  Value:k
start index:8   End Index:8  Value:
start index:9   End Index:10  Value:k
start index:10   End Index:10  Value:
start index:11   End Index:11  Value:
=================================================="""