# Election_Analysis

## Project Overview

A Colorado Board of Elections employee has given the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.]
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.9, Visual Studio Code 1.68.1

## Summary 

The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
    -   Charles Casper Stockham
    -   Diana DeGette
    -   Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
    - Diana DeGette received 73.8% of the vote and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes
- The winner of the election was:
    - Diana DeGette who received 73.8% of the vote and 272,892 votes.

## Challenge Overview

The election commission has requested some additional data to complete the audit:

1. The voter turnout for each county
2. The percentage of votes from each county out of the total count
3. The county with the highest turnout

## Challenge Summary 

The analysis of the election show that:
- There were 3 counties that participated in the election.
- The counties were:
    -   Jefferson
    -   Denver
    -   Arapahoe
- The county results were:
    - Jefferson county cast 10.5% of the vote with 38,855 votes.
    - Denver county cast 82.8% of the vote with 306,055 votes.
    - Arapahoe county cast 6.7% of the vote with 24,801 votes.
- The county with the largest voter turnout:
    - Denver


## Note to Election Committee

This script can be adapted to obtain the results for any future election including national and state elections (not just an audit of one of the precincts). For state elections you would have to modify the script in two ways:

1. Create an empty dictionary to hold states (keys) and states' number of votes (values) as well as an empty list to hold the States. Then create an if statement in a for loop to obtain the list of states who participated as well as initialize the number of votes per state to zero. Below is an example of the if statement used to obtain the list of counties. The if statement for states would mimic this logic but would point to the row in the new dataset that is aligned to states. Outside of the if statement, you would add a vote to that state's vote count.

![](/Resources/ReadMe_County_IfStatement.png)

2. The second modification would be another for loop to iterate through the States dictionary to calculate the percentage of voters per state who participated in the election. This would also mimic a for loop done in this project for the counties (image provided below).

![](/Resources/ReadMe_forloop_election.png)




