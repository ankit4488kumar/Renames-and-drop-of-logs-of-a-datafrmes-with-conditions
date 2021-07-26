# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 22:42:44 2021

@author: ankit
"""
#import required library
import pandas as pd
#create a dataframe
out = pd.DataFrame({'index':['L8.BRENT_price','L3.BRENT_CO1','L11.BRENT_CO1']})
print(out)#print output
#drop the value "BRENT_price" from the dataframe
out.drop(out.index[out['index'].str.contains('BRENT_price')], inplace = True)
print(out) #print output
#rename the logs value from "L3.BRENT_CO1" to "BRENT_CO1_lag_3"
out['index'] = out['index'].apply(lambda x: x.split('.')[1]+'_'+'lag'+'_'+x.split('.')[0][1:])
print(out) #print output