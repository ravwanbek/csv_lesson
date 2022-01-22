
def get_column(data):
    column_name = []
    a=f.readline()
    column_name.append(a)
    return column_name

data = open('data.csv').read()
print(type(data))
