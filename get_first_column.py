def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    r=data.split()
    k=r[0].split(",")
    return type(k[0])
    
# Read the csv file
f=open("data.csv")
data=f.read()
print(get_first_column(data))