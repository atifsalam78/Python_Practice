import requests
import pickle

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
re = requests.get(url=url)
with open("iris_data.txt","wb") as pfd:
    for ir_lines in re.iter_content(chunk_size=128):
        pfd.write(ir_lines)

with open("iris_data.txt") as pfd:
    data_set = [lines.split() for lines in pfd.readlines()]
    my_file = "iris_data_pickle.pkl"
    with open (my_file, "wb") as file_object:
        pickle.dump(data_set, file_object)

my_file = "iris_data_pickle.pkl"
with open (my_file,"rb") as file_object:
    my_data = pickle.load(file_object)
    for list_lines in my_data:
        print(list_lines)