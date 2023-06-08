import shutil
import os

src_path = r"F:\OJT\pythonProject\Assignment05\02.py"
dst_path = r"F:\OJT\pythonProject\02.py"
shutil.copy(src_path, dst_path)
os.remove("F:02.py")
print('Copied')
