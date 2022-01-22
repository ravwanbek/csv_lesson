


def get_column(data):
    column_name=[]
    a=data.split('\n')
    column_name=a[0].split(',')
    return column_name

f=open('data.csv').read()
print(get_column(f))









