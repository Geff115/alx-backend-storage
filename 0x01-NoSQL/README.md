0x01. NoSQL
Back-end
NoSQL
MongoDB
 Weight: 1


Requirements:

    MongoDB Command File:
        - All my files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2)
        - The first line of all my files should be a comment: // my comment
        - The length of my files will be tested using wc
    

    Python Scripts:
        - All my files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7) and PyMongo (version 3.10)
        - The first line of all my files should be exactly #!/usr/bin/env python3
        - My code should use the pycodestyle style (version 2.5.*)
        - The length of my files will be tested using wc
        - All my modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
        - All my functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
        - My code should not be executed when imported (by using if __name__ == "__main__":)


Learning Objectives:

    - What NoSQL means
    - What is difference between SQL and NoSQL
    - What is ACID
    - What is a document storage
    - What are NoSQL types
    - What are benefits of a NoSQL database
    - How to query information from a NoSQL database
    - How to insert/update/delete information from a NoSQL database
    - How to use MongoDB


Installation:

1. Remove the previous MongoDB list and key:    sudo rm <mongodb-4.2.gpg>

2. install the correct gpg key:       curl -fsSL https://pgp.mongodb.com/server-6.0.asc | sudo gpg --dearmor -o /usr/share/keyrings/mongodb-server-6.0.gpg

3. Readd the MongoDB repository:         echo "deb [signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list

4. update package list:      sudo apt-get update

5. Install MongoDB:      sudo apt-get install -y mongodb-org


To start MongoDB:

1. mongod --dbpath ~/data/db

2. Then open a new terminal and run:      mongosh

NB:  /data/db is a directory you could create if it doesn't exist.  (i.e  sudo mkdir -p ~/data/db ).