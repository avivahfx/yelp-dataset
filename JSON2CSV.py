import pandas as pd
import json
import time

def json_parser(filename):
    start = time.time()
    print(filename)
    csv_file = filename[0:filename.rindex(".")] + ".csv"
    
    # if error please change to open(filename, "r")
    json_file = open(filename, "rb")
   
    value_list = []
    columns = []
    df = pd.DataFrame()

    for line in json_file:
        Obj = json.loads(line)
        values = Obj.values()
        value_list.append(values)
        columns = Obj.keys()
        if(len(value_list)%10000==0):
            df_temp = pd.DataFrame(columns = columns, data = value_list)
            df = df.append(df_temp)
            value_list = []
            print(len(df))

    df_temp = pd.DataFrame(columns = columns, data = value_list)
    df = df.append(df_temp)
    df.to_csv(csv_file, index=False, encoding="UTF-8" )
    
    # only for monitor. could be deleted.
    print("==============================================")
    print(df.iloc[0])
    print("Cost time %d seconds." %(time.time()-start))
    print("==============================================")

# if yelp change filename, you can change/add it here.
json_parser("data/yelp_academic_dataset_tip.json")
json_parser("data/yelp_academic_dataset_business.json")
json_parser("data/yelp_academic_dataset_review.json")
json_parser("data/yelp_academic_dataset_checkin.json")
json_parser("data/yelp_academic_dataset_user.json")
