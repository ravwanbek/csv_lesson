
def get_column(data):
    column_name = []
    
    a=data.readline(0)
    column_name.append(a)
    return column_name

data = open('data.csv').read()
print(type(data))
