# Forbes_S2021_randomZeeAssignment
Code to create random groupings for zees in Forbes College, Princeton University.

# Files to use. No argument inputs. Change stuff in the script at the top.
## randomGrouping_getAllParticipants.py 

looks jank since it's generated from a jupyter notebook.

reads from submissions.csv and outputs a .xlsx file of randomized people in groups of 4. Can change the number 
of people per group in the top section of code. The output file is formated so that each row has n (currently 4) email addresses.
The last row has < n people and some number of placeholder addresses. The idea is that we can copy and paste a row into
the recipient field for an email and send emails out to each group. The "stragglers" in the last row can be added to
other groups by hand.
[TODO] probably should add a main function that takes command line arguments.

## generate_people.ipynb

is a jupyter notebook that generates some test data from a random list of names. Randomizes numbers and each person makes 3 submissions.


### Updated 02/21/2021 Robert Shi rs36@princeton.edu
hmu if you have any questions.
