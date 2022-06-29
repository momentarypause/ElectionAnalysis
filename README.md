# ElectionAnalysis

## Project Overview
The Colorado Board of Elections has requested a way to automate the following auditing tasks so that the code can be used for the current congressional election results and future elections across the state.

1. Calculate the voter turnout for each county.
2. Calculate the percentage of votes from each county out of the total count.
3. Determine the county with the highest voter turnout.
4. Calculate the total number of votes cast.
5. Get a complete list of candidates who received votes.
6. Calculate the total number of votes each candidate received.
7. Calculate the percentage of votes each candidate won.
8. Determine the winner of the election based on popular vote.

## Resources
-Data Source: election_results.csv-Software: Python 3.6.7, Visual Studio Code 1.68.1

## Summary
The analysis of the election shows that:
- There were 369,711 votes cast in the election consisting of voters from Jefferson, Denver, and Arapahoe counties.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
 ### Results
 #### Counties
- Jefferson County cast 38,855 votes, which was 10.5% of the total votes.
- Denver County cast 306,055 votes, which was 82.8% of the total votes.
- Arapahoe County cast 24,801 votes, which was 6.7% of the total votes.

The Colorado Board of Elections requested to see the county with the highest voter turnout.  With the data provided, we can see that Denver county cast the most votes, but that does not mean they had the highest voter turnout. To know that for sure, we would also need to know how many total registered voters there are in each of the counties so we could calculate how many voters out of the total registered voters cast votes.  If Jefferson or Arapahoe have significantly less registered voters than Denver county, they still may have had a better voter turnout based on the percentage of their registered voters who cast a vote.  The request for "highest voter turnout" cannot be completed as there is critical information missing from the dataset. *Please note that in a real-world situation I would have requested this information from the customer to make a complete analysis.  Seeing that this is pseudodata, that was not possible.*

##### The county with the highest percentage of votes was Denver county with 82.8% of the total votes.

#### Candidates
 - Charles Casper Stockham received 85,213 votes, which was 23.0% of the total votes.
 - Diana DeGette received 272,892 votes, which was 73.8% of the total votes.
 - Raymon Anthony Doane received 11,606 votes, which was 3.1% of the total votes.
 
 ##### The winner of the election was Diana DeGette with 73.8% of the popular vote.
  
 ### Future Reporting
 This code can easily be used for future elections.  Please note the following requirements and updates that will need to be made in Visual Studio Code to allow for it to read and interpret the data:
 - Future election data will need to be in the same file type and format as election_results.csv so that it reads the file correctly and pulls the information from the correct positions in the listed data.
 - The filename and path in line 9 will need to be updated to the new dataset file name and path to where it will be located.
 - The filename and path in line 11 will need to be updated to tell the program where to save the results of the analysis.
 
