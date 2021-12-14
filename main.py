import os
from filecmp import cmp


# list all documents
all_files = []

# list containing the classes of documents with the same content
duplicates = []

for path, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if not os.path.isdir(file):
            all_files.append(path + f'/{file}')

# comparison of the documents
for file in all_files:

    is_duplicate = False

    for class_ in duplicates:
        is_duplicate = cmp(file, class_[0], shallow=False)
        if is_duplicate:
            class_.append(file)
            break

    if not is_duplicate:
        duplicates.append([file])

# show results
for class_ in duplicates:
    if len(class_) > 1:
        print(class_)
