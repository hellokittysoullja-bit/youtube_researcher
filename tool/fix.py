import json,re
order=[]
for ln in open('chunks_hl/g_04.md',encoding='utf-8'):
    m=re.match(r'######## VIDEO (\S+) \|',ln)
    if m: order.append(m.group(1))
rows=[json.loads(l) for l in open('hl/g_04.jsonl',encoding='utf-8') if l.strip()]
for d in rows:
    v=d['v']
    if v=='1294OUlmwtA' and d['t0']==735: d['t1']=804
    if v=='E455eW6RqPc' and d['t0']==443: d['start']='strategy comes from general behavioral psychology'
    if v=='EAQlXfX4Lnc' and d['t0']==576: d['start']="easier than people think uh there's basically three"
    if v=='YO6uMBAnePE' and d['t0']==477: d['start']="doesn't mean is necessarily bad a lot of"
    if v=='qOzJAdxyzSs' and d['t0']==398: d['start']="recognize is what is your goal when you design"
    if v=='lqoGeieNH7M' and d['t0']==283: d['start']="at a simple gamification examples in and believe me"
rows+= [
{"v":"kdMc7PyBpbo","t0":33,"t1":110,"start":"Here's the reframe. Your brain isn't broken.","end":"most powerful behavior patterns ever discovered.","tags":["дофамин","нейро","СДВГ"],"label":"Мозг не сломан: древняя машина нацелена на стеклянный прямоугольник; опыты Скиннера","why":"Голуби при случайном подкреплении долбили рычаг упорнее, чем при предсказуемом; переменное подкрепление — один из сильнейших паттернов поведения.","app":"Рамка без стыда для текстов: «твой мозг работает как задумано, а среда его перехватила»."},
{"v":"kdMc7PyBpbo","t0":111,"t1":188,"start":"Decades later, a neuroscientist named Wolfram","end":"you built the box yourself and carry it everywhere.","tags":["дофамин","нейро","исследования"],"label":"Шульц: дофамин — химия предсказания, пик не при награде, а в момент «может быть»","why":"Дофамин почти не меняется при полностью предсказуемой награде и вспыхивает до неё, при неопределённости; каждая разблокировка телефона — тот же рычаг.","app":"Понимание механизма для награды: тянет предвкушение, поэтому Напарник показывает «что будет на острове» как мягкое предвкушение завершения сессии, а не как лотерею."},
{"v":"kdMc7PyBpbo","t0":190,"t1":281,"start":"You'd think a phone that always","end":"already leaning toward the next.","tags":["дофамин","тёмные-паттерны","нейро"],"label":"Гарантированная награда успокаивает, неопределённость тянет; pull-to-refresh и «печатает...» — слот-машина; качели Лембке","why":"Если бы каждая проверка гарантированно награждала, тяга бы снизилась; после каждого выброса дофамина идёт просадка ниже базовой линии, и качели не успокаиваются.","app":"Не копировать pull-to-refresh и индикаторы «печатает» в чате с котом; отвечать предсказуемо, без искусственной интриги."},
{"v":"kdMc7PyBpbo","t0":341,"t1":444,"start":"None of this requires you to be","end":"works automatically when it goes unnoticed.","tags":["СДВГ","внимание","стыд"],"label":"Тяга проверять — не слабость, а древний контур поиска; названная тяга теряет автоматизм","why":"Неопределённая награда в природе означала стоящую цель; назвать позыв («это сработал контур предсказания») на секунду достаточно, чтобы вернуть выбор.","app":"Реплика кота при отвлечении: «заметил(а), что рука потянулась?» — мягкое называние импульса без осуждения."},
]
rows.sort(key=lambda d:(order.index(d['v']),d.get('t0',0)))
open('hl/g_04.jsonl','w',encoding='utf-8').write('\n'.join(json.dumps(d,ensure_ascii=False) for d in rows)+'\n')
