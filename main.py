import os, shutil, time
print("drag your file into here or enter path")
pyPath = input()
print("drag your ico into here or enter path") 
ico = input()
os.system(f'pyinstaller "{pyPath}" --icon "{ico}" --onefile')
time.sleep(0.2)
os.remove("main.spec")
shutil.rmtree("build")
print("Sucessfully created your exe in the dist folder")
