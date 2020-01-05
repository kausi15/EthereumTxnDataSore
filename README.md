# EthereumTxnDataSore
This is a python based system which stores specified number of blocks recent blocks from Ethereum chain into MongoDB. We can get all the
transactions of a address using API. 

This system is crated using:-
- Flask
- MongoDB
- web3.py

API guide:-

- URL:- http://127.0.0.1:5000/storeBlocks
  
  Method:- GET
  
  Json Input:- { "number_of_latest_blocks": < specify the number of latest blocks you want to store > }
  

- URL:- http://127.0.0.1:5000/getTransactions
    
  Method:- GET
  
  JSON Input:- {"address": < specify the account address >}
 
 
Setup Guide:-

(1) Pull the code from github.com and open it in an IDE like Pycharm.

(2) You can create virtualenv with python3.7 or install Python3.7 and pip on your machine.

(3) You can install MongoDB on your system and setup it using https://docs.mongodb.com/manual/installation/ 
    or you can subscribe to  MongoDB as a service platform. After Inititation of MongoDB
    copy & paste the MongoDB access Url of your database on line 9 in db_help.py present 
    in app/Helper directory.
    

(4) Open the terminal and install all the requirements using requirements.txt using
      
      $ pip install -r requirements.txt
 
(5) Get into app directory in terminal and execute these two steps:-
        
        (a)  $ export FLASK_APP=app.py
        (b)  $ flask run 
     
  Your system will spin on and you can try both the API's.


 
