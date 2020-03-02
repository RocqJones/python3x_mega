"""
    This is documentation
"""

filename = "sample.txt"

# create empty file
def create_file():
    """ This function creates empty file """
    with open(filename,"w") as file:
        file.write("Write in me") # write empty string

create_file()