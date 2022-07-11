def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    k=[]
    r=data.split()
    for i in r :
        k=i.split(',')
    return type(len(k))

# Read the csv file
f=open('data.csv')
data= f.read()
print(find_number_of_columns(data))
