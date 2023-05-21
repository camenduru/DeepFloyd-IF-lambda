import os
os.system(f"git lfs install")
os.system(f"git clone -b lambda https://github.com/camenduru/DeepFloyd-IF-hf /home/demo/source/DeepFloyd-IF-hf")
os.chdir(f"/home/demo/source/DeepFloyd-IF-hf")
os.system(f"pip install -r requirements.txt")
os.system(f"python app.py")
