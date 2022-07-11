#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    k=[]
    arr=[]
    r=data.split()
    for i in r :
        k.append(i)
    return k[0].split(',')


# Read the csv file
f=open("data.csv")
data=f.read()
print(get_column_names(data))
