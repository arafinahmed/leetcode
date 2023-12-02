def fetch_code_from_db():
    code =  """
print(len(mystring))
print(mystring)
for i in range(10):
    print(i)
    for j in range(10):
        print(j)
            """
    
    code_2 =  """
print(len(mystring))
print(mystring)
            """
    
    return [code, code_2]

# Fetch the code from the database
code_to_run = fetch_code_from_db()
print(code_to_run)

mystring = "arafin ahmed"

# Execute the fetched code
try:
    for code in code_to_run:
        exec(code)
except Exception as e:
    print(f"An error occurred while executing the code: {e}")