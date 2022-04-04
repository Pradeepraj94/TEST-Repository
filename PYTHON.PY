#Load Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Copying csv dataset in a variable called dataset_file 
#Copying csv output file to output_file
dataset_file = r"youtube_dataset.csv"
output_file = r"youtube_output.csv"

#Loading the datafile in pandas DataFrame (Using L1 encoding)
youtube_data = pd.read_csv(dataset_file, sep=",", encoding='ISO-8859-1')

#Filtering top 1000 rows
top_1000_data = youtube_data.head(1000)

#View filtered data
top_1000_data

#Count plot for top 1000 rows by channeltype
fig, ax = plt.subplots(figsize=(16, 8))
sns.countplot(x ='channeltype', data =top_1000_data , ax=ax)

#histogram for top 1000 rows by subscribers
top_1000_data.hist(column='subscribers')
top_1000_data.plot(kind='hist')

