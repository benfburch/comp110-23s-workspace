from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str,str]]:
    """Read csv file and return as a list of dicts with header keys"""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_vals(table: list[dict[str,str]], header: str) -> list[str]:
    """Returns values in a table under a specific header."""
    result: list[str] = []
    #step through table 
    for row in table: 
        #save every value under key "header"
        result.append(row[header])
    return result

def columnar(table: list[dict[str,str]]) -> dict[str,list[str]]:
    """Reforms data so that its a dictionary with column headers."""
    results: dict[str, list[str]] = {}
    #loop through keys of one row of table
    first_row: dict[str,str] = table[0]
    for key in first_row:
        #for each key, make a dict entry with all column values
        results[key] = column_vals(table, key)
    return results

def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column whose name is the second parameter."""
    empty: list[str] = list()
    for elem in table:
        for key in elem:
            if key == column:
                empty.append(elem[key])
    return empty

def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produces a new column based dict with only the first N rows of data for each column."""
    empty: dict[str, list[str]] = dict()
    for n in table:
        empty_list: list[str] = []
        data: list[str] = table[n]
        idx: int = 0
        while idx < rows and idx < len(data):
            empty_list.append(data[idx])
            idx += 1
        empty[n] = empty_list
    return empty

def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produce a new column based table with only a specific subset of the original columns."""
    empty: dict[str, list[str]] = dict()
    for column in columns:
        empty[column] = table[column]
    return empty

def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new colum-based table with two column based tables combined."""
    empty: dict[str, list[str]] = dict()
    for n in table1:
        empty[n] = table1[n]
    for n in table2:
        if n in empty:
            empty[n] += table2[n]
        else:
            empty[n] = table2[n]
    return empty

def count(list: list[str]) -> dict[str, int]:
    """Creates a dict of the counts of each item in the input list."""
    empty: dict[str, list[str]] = dict()
    for n in list:
        if n in empty:
            empty[n] += 1
        else:
            empty[n] = 1
    return empty