import shutil

shutil.copyfile("prog40-cadenas.py", "hola2/p40.py")
shutil.rmtree("backup")
shutil.copytree(".", "backup")