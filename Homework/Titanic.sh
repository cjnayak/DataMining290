cd
ls
cd DataminingData
ls
head titanic.csv
awk -F, '$2 ==1' titanic.csv | wc -l
awk -F, '$2 ==0' titanic.csv | wc -l
more titanic.csv | wc -l
# Of the 891 passengers on the titanic, 38.4% of passengers survived while 61.6% of passengers died
awk -F, '$2==1 && $3==1' titanic.csv | wc -l
awk -F, '$2==1 && $3==2' titanic.csv | wc -l
awk -F, '$2==1 && $3==3' titanic.csv | wc -l

# Of the 342 passengers that survived the crash, 39.8% were 1st class passengers, 25.42% were 2nd class, and 34.8% were 3rd class passengers.

awk -F, '/female/ && $2==1' titanic.csv | wc -l

# Of the 342 passengers that survived the crash 68.12% were female.

#Questions for Lab: 
# What types of data are avaliable, how many records were there?:  I used Kaggle for my data set and was provided a training data set which included 892 passengers on the Titanic.  

#Provide an "interesting" record, explain its properties and why it is interesting:  One interesting record is the record on class within the data.  This is interesting because it allows a person to initiate a query on the dataset and understand if class on the ship impacted the number of passengers that survived the crash. 

#Three questions I have answered in the data set are (1)What is the percentage of people who survived the crash; (2) How many men versus female survived the crash; (3) What class type was more likely to survive the class.  The answers to these questions are commented out above. 




