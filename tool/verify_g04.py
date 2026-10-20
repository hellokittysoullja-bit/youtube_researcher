import json,re,sys
chunk=open(sys.argv[1],encoding='utf-8').read().split('\n')
vids={};cur=None
for ln in chunk:
    m=re.match(r'######## VIDEO (\S+) \|',ln)
    if m: cur=m.group(1);vids[cur]=[];continue
    m=re.match(r'\[(\d+):(\d+)\] (.*)',ln)
    if m and cur: vids[cur].append((int(m.group(1))*60+int(m.group(2)),m.group(3)))
def norm(s):
    s=re.sub(r'\[[Mm]usic\]|>>|\[Applause\]|\[snorts\]|\[Music\]',' ',s)
    return re.sub(r'\s+',' ',s).strip()
bad=0;n=0;vs=set()
rows=[]
for i,l in enumerate(open(sys.argv[2],encoding='utf-8'),1):
    l=l.strip()
    if not l: continue
    d=json.loads(l);n+=1;vs.add(d['v'])
    if 'skip' in d: continue
    t0,t1=d['t0'],d['t1']
    txt=norm(' '.join(t for s,t in vids[d['v']] if t0-1<=s<t1+1))
    for k in('start','end'):
        if norm(d[k]) not in txt:
            bad+=1;print('MISS',i,d['v'],k,repr(d[k]))
    if t1-t0>240: print('LONG',i,t1-t0)
    rows.append((d['v'],t0,t1))
prev={}
for v,a,b in rows:
    if v in prev and a<prev[v]: print('OVERLAP',v,a,prev[v])
    prev[v]=b
print(n,'lines',len(vs),'videos',bad,'bad')
print(set(vids)-vs)
