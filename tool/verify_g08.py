import json,re,sys
base='/tmp/claude-0/-home-user-Naparnik-Site-ADHD/ef78bace-cd2b-5182-85a8-51b434389524/scratchpad/ytr/'
vids={};cur=None
for line in open(base+'chunks_hl/g_08.md',encoding='utf-8'):
    m=re.match(r'######## VIDEO (\S+) \|',line)
    if m: cur=m.group(1);vids[cur]=[];continue
    m=re.match(r'\[(\d+):(\d+)\] (.*)',line)
    if m and cur:
        t=int(m.group(1))*60+int(m.group(2))
        for w in m.group(3).split(): vids[cur].append((t,w))
norm=lambda w: re.sub(r'[^\w]','',w.lower().replace('’',"'").replace("'",''))
def find(v,phrase,t0,t1,from_end):
    toks=[norm(x) for x in phrase.split()]
    toks=[x for x in toks if x]
    W=vids[v]; n=len(toks); res=None
    for i in range(len(W)-n+1):
        if all(norm(W[i+j][1])==toks[j] for j in range(n)):
            if t0-15<=W[i][0]<=t1+15:
                res=(i,i+n)
                if not from_end: break
    return res
out=[];bad=0
for l in open(base+'hl/g_08.jsonl',encoding='utf-8'):
    d=json.loads(l)
    if 'skip' in d: out.append(d);continue
    v=d['v']
    s=find(v,d['start'],d['t0'],d['t1'],False)
    e=find(v,d['end'],d['t0'],d['t1'],True)
    # dedupe words in toks with empty norm ignored
    if not s or not e or e[1]<=s[0]:
        bad+=1;print('BAD',v,d['t0'],d['t1'],'|',d['start'],'|',d['end'],bool(s),bool(e))
    else:
        W=vids[v]
        d['start']=' '.join(w for _,w in W[s[0]:s[1]])
        d['end']=' '.join(w for _,w in W[e[0]:e[1]])
    out.append(d)
print('bad',bad,'total',len(out))
if len(sys.argv)>1:
    with open(base+'hl/g_08.jsonl','w',encoding='utf-8') as f:
        for d in out: f.write(json.dumps(d,ensure_ascii=False)+'\n')
