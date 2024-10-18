For this assignment, you will be creating a binary search tree that allows the user to search for records from `fish.csv`

You should use the following files and modify them slightly as required:

`BST.c`

`BST.h`

`main.c`

`makefile`

The program should do the following:

    Open the fish.csv 

    Download fish.csv file.
    Read the file one line at a time. Separate each line into a number (which we will use as a key for searching) and the rest of the record, which will be the data(value in Node struct in BST.h).

    Insert the data from each line into a binary search tree. 
    Print the count of nodes in the tree using the count() method. 
    Print the tree keys 1)in preorder,2) inorder, and 3)postorder traversal. 
    Allow the user to search for numbers in the binary search tree repeatedly. If the number exists, the program should print the rest of the data associated with the number. If the number does exist, the program should print "<number> not found."
    If the user enters nothing for the number, the program should exit.
    Sample output:

Main program 

        The main program should read in the data file one line at a time. Each line should strip off the number, then call the insert function to insert the number and associated data/value into the tree.
        The main program should allow the user to search for a number and call the search function. If the number is in the tree, the main program should print the associated data or enter nothing to exit.

Testing: 

To test the program's search for the following numbers: 22, 80,  2, 35, 70. Make sure the output is clear and easy to read. (include the test in the sample output).

Turn in:

The source code files ( BST.h, BST.c, main.c, and makefile) and the sample output that tests the program.

 

 

strtok():

https://stackoverflow.com/questions/26443492/read-comma-separated-values-from-a-text-file-in-c

