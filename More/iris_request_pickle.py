import requests
import pickle

"""" Indirect method reading from ".txt file """

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
    # print(my_data)
    md = [list_lines for list_lines in my_data if len(list_lines) != 0]
    print(md)


""" 
Direct method without reading from ".txt" file

"""

# data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text

""" 
print(data)
l1 = data.split("\n") # not in use Just for understanding
print(l1)
"""
# l2 = [item.split() for item in data.split("\n") if len(item)!=0]

# print(l2)

# with open("my_iris_pickle.pkl", "wb") as f:
#     pickle.dump(l2, f)


# with open("my_iris_pickle.pkl",'rb') as f:
#     print(pickle.load(f))

