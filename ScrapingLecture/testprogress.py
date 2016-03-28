from tqdm import tqdm
from time import sleep
lv = True
ns = True
for i in tqdm(range(2), desc='outer0 loop', leave=True):
	for j in tqdm(range(4), desc='inner1 loop', leave=lv, nested=ns):
		for k in tqdm(range(100), desc='inner2 loop', leave=lv, nested=ns):
			sleep(0.01)
