#%%
import json 
#%%
with open('states.json') as f:
    data=json.load(f) 
print(type(data))
#%%
print(data)
# %%
for state in data['states']:
    del state['area_codes']
# %%
print(data)

