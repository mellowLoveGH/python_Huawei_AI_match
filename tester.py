import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import seaborn as sns
import datetime


import time 
start=time.time() 
jdata_action=pd.read_csv("user_app_usage.csv") 
end=time.time() 
print("time cost: ",end-start)
#print(jdata_action.head())
jdata_action.shape
jdata_action_sample=jdata_action.sample(100000) 
jdata_action_sample.to_csv("sample.csv")
