def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    r=data.split()
    for i in r :
        k=i.split(',')[0]
    return int(k)+1

# Read the csv file
f=open('data.csv')
data= f.read()
print(find_number_of_rows(data))

