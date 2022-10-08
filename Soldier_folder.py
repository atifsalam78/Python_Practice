import os


def soldier_folder(pat, exclude, f_format):
    count = 0
    os.chdir(pat)
    exclude_dir = [exclude]
    current_dir = os.getcwd()
    list_dir = os.listdir()
    for files in list_dir:
        join_path = os.path.join(current_dir, files)
        text_split = os.path.splitext(join_path)
        check_file = os.path.isfile(join_path)
        if check_file == True and text_split[-1] == f_format:
            count += 1
            file_rename = f"{count}{f_format}"
            if os.path.isfile(file_rename):
                continue
            else:
                os.rename(files, file_rename)

    for files in list_dir:
        join_path = os.path.join(current_dir, files)
        check_file = os.path.isfile(join_path)
        if check_file == True and files not in exclude_dir:
            os.rename(files, files.lower())


soldier_folder("/home/atif/Documents/soldier", "python.txt", ".docx")
