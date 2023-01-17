#FOCP TASK 3
import sys
import random

#checks if the number of command-line passed to the script
if len(sys.argv) != 2:
    print("Error: Missing command-line argument.")
    sys.exit(1)

#trying to open input file 
try:
    with open(sys.argv[1],"r") as input_file:
        lines = input_file.readlines()
except OSError:
    print(f"Error: Cannot open {sys.argv[1]}. Sorry about that.")
    sys.exit(1)


#writing in output file
with open("students_emails.txt", "w") as output_file:
    for line in lines:
#split into two parts
        student_id, name = line.split(None, 1)
#split the surname and firstname
        surname, firstname = name.rsplit(",", 1)
#remove non-alphabetic characters
        surname = "".join(v for v in surname if v.isalpha())
#initials from firstname
        initials = ".".join(v[0] for v in firstname.split())
#generate random number between 0 and 9999       
        random_number = str(random.randrange(10000)).zfill(4)
#create email address      
        email = f"{initials.lower()}.{surname.lower()}{random_number}@poppleton.ac.uk"
        output_file.write(f"{student_id} {email}\n")
















