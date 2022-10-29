# e-flow energy mix reader

AWS Lambda function to read energy mix data from a Timestream DB. 

Event to be formatted as following: 

    {
    "startTime": 1666803984,
    "endTime": 1667003984
    }
