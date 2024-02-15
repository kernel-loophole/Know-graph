import os
import pandas as pd
from json_form import read_json_file
from news_graph import NewsMining
def read_csv_files_from_folder(folder_path):
    # Initialize an empty dictionary to store DataFrames
    dfs = {}
    sublist=[]
    # Walk through all folders and subfolders
    for folder_root, _, files in os.walk(folder_path):
        # Filter CSV files
        csv_files = [file for file in files if file.endswith(".csv")]
        # print(csv_files)
        # Process each CSV file in the current folder
        for csv_file in csv_files:
            file_path = os.path.join(folder_root, csv_file)
            df = pd.read_csv(file_path)
        #     text=df["Detail"]
        #     date=df["CreationDate"]
        #     for text_tmp in text:
        #         try:
        #             Miner.main(text_tmp)
                    
        #         except:
        #             flag=1
        #             pass
        #     try:
        #         merged_string = ''.join(text)
        #     except:
        #         pass
        #     final_text=final_text+str(merged_string)
        #     if flag==0:
        #         data=read_json_file('graph_data.json')
        #         x=data['edges']
        #         for i in x:
        #             # print(i["label"])
        #             sublist.append(i['label'])
                    
        #     else:
        #         sublist.append("None")
        # keywords_list.append(sublist)
        dfs[os.path.relpath(file_path, folder_path)] = df

    return dfs

# Specify the path to the main folder containing CSV files and subfolders
# main_folder_path = "/home/haider/Desktop/Know-graph/Scrapper/2024/2024-01-11"
# main_folder_path_1="/home/haider/Desktop/Know-graph/Scrapper/2024/2024-01-10"
# main_folder_path_2="/home/haider/Desktop/Know-graph/Scrapper/2024/2024-01-17"
# main_folder_path_4="Scrapper/2023/2023-05-13"
# # Call the function to read CSV files from the main folder and its subfolders
# dataframes_1 = read_csv_files_from_folder(main_folder_path)
# dataframes_2 = read_csv_files_from_folder(main_folder_path_1)
# dataframes_3 = read_csv_files_from_folder(main_folder_path_2)
# dataframes_4=read_csv_files_from_folder(main_folder_path_4)
Miner = NewsMining()
keywords_list=[]
def merged_text_hello(dataframes):
    final_text=""
    if dataframes:
        for file, df in dataframes.items():
            flag=0
            sub_list=[]
            #print(f"DataFrame from {file}:")
            text=df["Detail"]
            date=df["CreationDate"]
            for text_tmp in text:
                try:
                    Miner.main(text_tmp)
                    
                except:
                    flag=1
                    pass
            try:
                merged_string = ''.join(text)
            except:
                pass
            final_text=final_text+str(merged_string)
            if flag==0:
                data=read_json_file('graph_data.json')
                x=data['edges']
                for i in x:
                    # print(i["label"])
                    sub_list.append(i['label'])  
            else:
                sub_list.append("None")
                
        keywords_list.append(sub_list)
        df["keywords"]=keywords_list
    return  final_text

# text_to_store_1=merged_text_hello(dataframes_1)
# text_to_store_2=merged_text_hello(dataframes_2)
# text_to_store_3=merged_text_hello(dataframes_3)
# text_to_store_4=merged_text_hello(dataframes_4)
# file_path = "output.txt"
# text_to_store=text_to_store_1+text_to_store_2+text_to_store_3+text_to_store_4
# with open(file_path, "w") as file:
#     # Write the text to the file
#     file.write(text_to_store)

# print(f'Text has been stored in the file: {file_path}')
def merge_text_from_files(file_paths):
    merged_text = ""

    for file_path in file_paths:
        try:
            with open(file_path, "r") as file:
                merged_text += file.read()
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")

    return merged_text

# file_paths = ["/home/haider/Desktop/Know-graph/output.txt"]
# result = merge_text_from_files(file_paths)
# print("=====================================")
# print(keywords_list)

df=pd.read_csv("output/back.csv")
print(df)

flag=0
sub_list=[]
#print(f"DataFrame from {file}:")
text=df["Detail"]
print(text)
date=df["CreationDate"]
for text_tmp in text:
    sub_list=[]
    try:
        data=Miner.main(text_tmp)
        
    except:
        flag=1
        pass
    try:
        merged_string = ''.join(text)
    except:
        pass
    # final_text=final_text+str(merged_string)
    # data=read_json_file('graph_data.json')
    x=data['edges']
    print("==========================")
    print(x)     
    for i in x:
        # print(i["label"])
        sub_list.append(i['label']) 
    # print("===========")
    # print(sub_list)
    keywords_list.append(sub_list)
print(len(x))
# print(keywords_list)
print(len(text))

df["keywords"]=keywords_list
print(df)
df.to_csv("test_output.csv")