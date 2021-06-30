import pandas as pd
import numpy as np

df = pd.read_excel('dataset.xlsx')


age = df['age']
bp = df['bp']
sg = df['sg']
al = df['al']
su = df['su']
rbc = df['rbc']
pc = df['pc']
pcc = df['pcc']
ba = df['ba']
bgr = df['bgr']
bu = df['bu']
sc = df['sc']
sod = df['sod']
pot = df['pot']
hemo = df['hemo']
pcv = df['pcv']
wc = df['wc']
rc = df['rc']
htn = df['htn']
dm = df['dm']
cad = df['cad']
appet = df['appet']
pe = df['pe']
ane = df['ane']

ages = np.std(age)
bps = np.std(bp)
sgs = np.std(sg)
als = np.std(al)
sus = np.std(su)
rbcs = np.std(rbc)
pcs = np.std(pc)
pccs = np.std(pcc)
bas = np.std(ba)
bgrs = np.std(bgr)
bus = np.std(bu)
scs = np.std(sc)
sods = np.std(sod)
pots = np.std(pot)
hemos = np.std(hemo)
pcvs = np.std(pcv)
wcs = np.std(wc)
rcs = np.std(rc)
htns = np.std(htn)
dms = np.std(dm)
cads = np.std(cad)
appets = np.std(appet)
pes = np.std(pe)
anes = np.std(ane)

dataset=[]

for i,row in df.iterrows():
		temp = {
			'age':row['age'] ,
			'bp':row['bp'],
			'sg':row['sg'],
			'al':row['al'],
			'su':row['su'] ,
			'rbc':row['rbc'],
			'pc':row['pc'],
			'pcc':row['pcc'],
			'ba':row['ba'],
			'bgr':row['bgr'],
			'bu':row['bu'],
			'sc':row['sc'] ,
			'sod':row['sod'],
			'pot':row['pot'],
			'hemo' : row['hemo'],
			'pcv':row['pcv'],
			'wc':row['wc'],
			'rc':row['rc'],
			'htn':row['htn'],
			'dm':row['dm'],
			'cad':row['cad'],
			'appet':row['appet'],
			'pe':row['pe'],
			'ane':row['ane']
		}
		dataset.append(temp)



for i in range(10):
	for i,row in df.iterrows():
		temp = {
			'age':row['age'] + round(np.random.uniform(ages),1),
			'bp':row['bp'] + round(np.random.uniform(bps),1),
			'sg':row['sg'] + round(np.random.uniform(sgs),1),
			'al':row['al'] + round(np.random.uniform(als),1),
			'su':row['su'] + round(np.random.uniform(sus),1),
			'rbc':row['rbc'] + round(np.random.uniform(rbcs),0),
			'pc':row['pc'] + round(np.random.uniform(pcs),0),
			'pcc':row['pcc'] + round(np.random.uniform(pccs),0),
			'ba':row['ba'] + round(np.random.uniform(bas),0),
			'bgr':row['bgr'] + round(np.random.uniform(bgrs),1),
			'bu':row['bu'] + round(np.random.uniform(bus),1),
			'sc':row['sc'] + round(np.random.uniform(scs),1),
			'sod':row['sod'] + round(np.random.uniform(sods),1),
			'pot':row['pot'] + round(np.random.uniform(pots),1),
			'hemo':row['hemo']+ round(np.random.uniform(hemos),1),
			'pcv':row['pcv'] + round(np.random.uniform(pcvs),1),
			'wc':row['wc'] + round(np.random.uniform(wcs),1),
			'rc':row['rc'] + round(np.random.uniform(rcs),1),
			'htn':row['htn'] + round(np.random.uniform(htns),0),
			'dm':row['dm'] + round(np.random.uniform(dms),0),
			'cad':row['cad'] + round(np.random.uniform(cads),0),
			'appet':row['appet'] + round(np.random.uniform(appets),0),
			'pe':row['pe'] + round(np.random.uniform(pes),0),
			'ane':row['ane'] + round(np.random.uniform(anes),0)
		}
		dataset.append(temp)
print(len(dataset))
df = pd.DataFrame(dataset)
df.to_csv('newdataset3.csv')
