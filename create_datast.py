import glob2
import pandas as pd

df_combined = pd.DataFrame()
df2 = pd.DataFrame()


filenames = glob2.glob('sample_Signature333593f/sample_Signature/genuine/*.png')
lst = map(lambda x: x.split('/')[3], filenames)
df_combined['images'] = lst
df_combined['genuine'] = 1

filenames = glob2.glob('sample_Signature333593f/sample_Signature/forged/*.png')
lst = map(lambda x: x.split('/')[3], filenames)
df2['images'] = lst
df2['genuine'] = 0

df_combined = df_combined.append(df2, ignore_index=True)

df_combined['ID'] = map(lambda x: x[4:7],df_combined['images'])
df_combined['ID'] = df_combined['ID'].astype('str')

df_combined.to_csv('combined_dataset.csv',index=None)




