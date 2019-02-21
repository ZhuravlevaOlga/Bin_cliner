import os
import shutil

path = os.path.join(os.getcwd(), 'Data')
files = os.listdir(path)
for f in files:
    p = os.path.join(path, f)
    p_files_trashbin = os.path.join(p, 'files_trashbin')
    for root, subdirs, files in os.walk(p_files_trashbin):
        for i in subdirs:
            shutil.rmtree(os.path.join(root, i))
        for file in files:
            p_files_trashbin_file = os.path.join(p_files_trashbin, file)
            os.remove(p_files_trashbin_file)
print('Удаление завершено')