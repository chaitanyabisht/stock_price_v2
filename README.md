# Stock Price Reporter V2

This is a completely revamped version of Stock Price Reporter V1. This now uses a database (Amazon DynamoDB) to store the stock symbol and their minimum and maximum prices instead of storing that in the source code itself. 

It uses the boto3 library to access the database.

Also now a client-side script is written to change the values of the database by using making GET requests to Amazon API Gateway. Previously I had to edit the source code in order to add or remove stock symbols but now it can be done easily by just running the script and issuing the commands.
