def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    r=data.split()[0].split(',')
    return len(r)

# Read the csv file
f=open('data.csv')
data= f.read()
print(find_number_of_columns(data))
