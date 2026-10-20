import json,sys
def add(items):
    with open('hl/g_16.jsonl','a') as f:
        for v,t0,t1,s,e,tags,label,why,app in items:
            f.write(json.dumps({"v":v,"t0":t0,"t1":t1,"start":s,"end":e,"tags":tags,"label":label,"why":why,"app":app},ensure_ascii=False)+"\n")
