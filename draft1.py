import pandas as pd
df=pd.read_csv("./data/shinyMetadat.csv")
byGroup=df.groupby('State').size().to_frame()
mapping = {byGroup.columns[0]: 'State', byGroup.columns[1]: 'Freq'}
byStateDf=byGroup.rename(columns=mapping)

print(list(byStateDf.columns))