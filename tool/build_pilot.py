"""Пилот «дословной выжимки»: фрагменты автора + проверка, что ни одно слово не добавлено и не изменено."""
import difflib, json, re, sqlite3, sys
sys.path.insert(0, ".")
from extract import raw, norm

VID = "3aH--S3r9n4"
HEAD = {
    "title": "Designing for Neurodiversity — Treyce Meredith (Config 2022)",
    "who": "Treyce Meredith — продуктовый дизайнер Dropbox (mobile growth), дислексик; рассылка «Designing for Neurodiversity»",
    "length": "19 мин, английский, авто-субтитры YouTube",
}

ITEMS = [
    dict(t0=487, t1=572, tags="избыточность · модалки · выход",
         label="Две кнопки закрытия — это не избыточность, а помощь (Pinterest)",
         why="Дублирование привычных мест выхода снимает вопрос «где тут закрыть» — человеку не надо думать.",
         app="Во всех модалках и шагах Напарника выход в двух привычных местах: крестик сверху + «Не сейчас» снизу. Меньше решений в момент, когда сил и так мало.",
         text="I wanted to really zoom in on a very small way that you can bring abundance to your interface. This is a modal from Pinterest when you're creating a new board. The thing I absolutely love about this modal is it has a close button in the bottom left and in the top right. Now, these buttons essentially do the same thing: there's a cancel button, it'll stop this workflow, close the modal; the X at the top will also do the same thing. This is probably my favorite example in my talk today because it's so simple, but yet it actually will help anyone who's using this modal who needs to get out of it. They don't have to think, 'Oh, where's the close button?' It's in two spots that these buttons are commonly placed, so people will easily be able to find them and achieve their goal. I can't tell you how many times I've had this discussion with fellow designers where they think, again, this might — these two buttons are a little redundant. But I think that a certain amount of redundancy can really just help people. I don't think any user will look at this modal, notice both close buttons, and be offended or disappointed. I think it will only help them achieve their goals faster and with less frustration."),
    dict(t0=319, t1=423, tags="доступность · инклюзивный дизайн · метрика успеха",
         label="Доступ (access) и успех (success) — две стороны одной медали",
         why="Доступность — это «могу войти и пользоваться без бремени». Успех — «понял ценность и получил результат». Второе — настоящая цель.",
         app="Контраст, reduced-motion и размеры касаний — это только «доступ». Метрика Напарника — человек реально сделал первый старт и вернулся; проверять надо её, а не галочку WCAG.",
         text="I think there's two sides of the same coin, basically. The first thing that I think we need is what I'm calling access, which is, I think, boiled down, really, digital accessibility. So this is providing users with essential engagement in your product, right, so they can navigate, they can use your features, they can log in, you know, they can do the table-stakes things that every website and every person using a website needs to do, and they can do those things without burden. The other side of the coin is something I like to call success. And I think if you boil this down you can think of it as inclusive design, or more on the inclusive design spectrum. So this is that users can have really valuable engagement with your product: they can not only navigate around, but they can understand and achieve the value you're trying to bring them. They can have a meaningful experience and build strong proficiency with these products."),
    dict(t0=572, t1=657, tags="прощающий интерфейс · отмена · предупреждение до ошибки",
         label="Прощающий интерфейс: отмена отправки и «забыл вложение» (Gmail)",
         why="Отмена после действия и подсказка до него добавляют «трение», но дают чувство безопасности: если ошибся — это чинится.",
         app="Напарнику: «вернуть шаг» после случайного тапа и мягкое предупреждение до потери введённого текста. Безопасность ошибки снижает страх старта.",
         text="The next principle I want to introduce is that your interfaces should be forgiving. We should be forgiving users. The first example I have comes from Gmail. I absolutely love both of these things. The first one is that you can simply undo an email that is sent. I don't know how many of us have sent emails that we regret, but Gmail has a feature that we can change our minds very quickly — super useful, easy, and helpful. In even more detail, they're helping us before we send as well, with the forgot-attachment alert. I constantly forget to attach things to emails before I send them, and this alert gives me some feedback before I send. I think both of these examples you could say perhaps are unnecessary, or maybe add more friction to the user experience, but at the same time they forgive users and make them feel safe and comfort them that if they do happen to do something wrong, there are ways to fix and remedy those things."),
    dict(t0=657, t1=742, tags="прощающий интерфейс · история · конкурентное преимущество",
         label="Прощение как конкурентное преимущество: удалённые файлы и история версий (Dropbox)",
         why="Dropbox позиционирует себя «не корзиной на рабочем столе, где всё пропадает навсегда». Фичу можно было не делать — её сделали из заботы о чувствах пользователя.",
         app="Прощение — продуктовая позиция, а не мелочь: пропавшее дело и сброшенный шаг должны быть возвращаемы («история стартов», очередь шагов). Это и есть «без стыда» в механике.",
         text="My next example comes from Dropbox. This is my absolute favorite feature of Dropbox, I use it constantly at work, and it is the deleted files and version history feature. On Dropbox you can easily navigate to this tab in the main navigation and look back, see all your deleted files and version history of those files. I think this really creates a competitive advantage for Dropbox, because they are positioning themselves as a really forgiving storage platform. They're not the trash can on your desktop, that if you empty, everything's gone forever. When you store things with Dropbox, you just don't have to worry about that. They have really taken a bold approach to forgiving their users and allowing them to have access to their deleted files. This is a feature that Dropbox could easily have never built. They don't have to have this, but because they want to optimize workflows, because they're thinking about their users and their feelings, they want to forgive them. They want to make sure that everyone storing files there can make a mistake and come back."),
    dict(t0=870, t1=953, tags="ИИ · редактирование · взращивание",
         label="ИИ делает черновик, человек правит: автосубтитры TikTok",
         why="Нажал кнопку — субтитры готовы (это уже впечатляет). Но «гениально» то, что их можно отредактировать: человек сохраняет авторство и говорит то, что имеет в виду.",
         app="Разбиение задачи (api/breakdown) должно быть черновиком, который правится на месте: переименовать, удалить, склеить шаг. ИИ предлагает — человек решает.",
         text="TikTok actually introduced a feature where creators, people making videos on their platform, can just tap a button and captions are automatically generated to those videos. Now, I think we would all say that's impressive enough. That's really cool technology. It's a super simple and easy user experience just to be able to tap a button and bam, there's captions. But they took it one step further, which is really the thing I want to call out about the genius of this feature: which is that they allow you to then, once the captions are generated, go into what they've auto generated for you and edit them. So if they've made a mistake, if you want to rephrase or re-clarify something, they give you that power. And so this feature really nurtures accurate but also very expressive closed captioning for anyone who's making a TikTok video. They are actively allowing you to say what you mean."),
    dict(t0=997, t1=1100, tags="комплаенс · приёмка · зрелость доступности",
         label="Не останавливаться на комплаенсе: после «доступа» нужен «успех»",
         why="Команды доступности сейчас сфокусированы на соответствии стандартам (это хорошо), но автор просит балансировать комплаенс с вопросом «стал ли пользователь успешным».",
         app="Критерий «готово» для экрана Напарника — не «прошёл контраст и reduced-motion», а «человек с СДВГ смог начать и вернуться завтра». Проверять на реальном сценарии, а не списком.",
         text="Access is really trending, which makes me so happy. I'm thrilled to see more designers, engineers, product people care about accessibility in a deep enough way that it is really become an essential skill set, or table-stakes functionality, that every product needs to have. It's really exciting. But talking through to my friends and colleagues in the industry who are actively working in accessibility, their teams are really focused on compliance right now, which is honestly a wonderful thing. I'm so grateful that we have laws and guidelines and legislation that require digital tools on the internet to reach a certain level of accessibility. But these teams are really focused on compliance for that business case. And what I would really like to see in the future is that they're able to balance this need for compliance and access, but also be able to focus on success. Any team out there that's working on accessibility right now, I really hope this talk will empower your team to think outside of just compliance and start thinking about how you can make your product more forgiving, more abundant, or nurture."),
]


def verify(item):
    window = raw(VID, item["t0"] - 15, item["t1"] + 15)
    a, b = norm(item["text"]), norm(window)
    # слова, дублирующие соседа (заикание), в сравнении не учитываем
    dedupe = lambda ws: [w for i, w in enumerate(ws) if i == 0 or w != ws[i - 1]]
    a, b = dedupe(a), dedupe(b)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    matched = sum(m.size for m in sm.get_matching_blocks())
    extra = [w for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag in ("replace", "insert") for w in a[i1:i2]]
    return len(a), matched, extra


def mmss(t):
    return f"{t // 60:02d}:{t % 60:02d}"


ok = True
out = [f"# {HEAD['title']}\n", f"**Кто говорит:** {HEAD['who']}  \n**Видео:** https://youtu.be/{VID} · {HEAD['length']}\n",
       "> Формат «дословная выжимка»: блок **«Слова автора»** — точный текст из транскрипта (убраны только um/uh, заикания, добавлены знаки препинания; "
       "слова не меняются — это проверяется скриптом; единственная поправка — ASR-название «tick tock» → TikTok). Блоки **«Мысль»** и **«Для Напарника»** — мой вывод, они отделены от слов автора.\n"]
for n, it in enumerate(ITEMS, 1):
    total, matched, extra = verify(it)
    status = "✓" if not extra else "✗ ДОБАВЛЕНЫ СЛОВА: " + " ".join(extra)
    if extra:
        ok = False
    print(f"{n}. {it['label'][:60]:62} слов {total:3} совпало {matched:3} {status}")
    out.append(f"\n---\n\n## {n}. {it['label']}\n`{it['tags']}` · [{mmss(it['t0'])}–{mmss(it['t1'])}](https://youtu.be/{VID}?t={it['t0']})\n")
    out.append(f"**Мысль:** {it['why']}\n")
    out.append("**Слова автора:**\n\n" + "\n".join("> " + p for p in [it["text"]]) + "\n")
    out.append(f"**Для Напарника:** {it['app']}\n")
open("pilot/3aH--S3r9n4.md", "w").write("\n".join(out))
print("ALL VERIFIED" if ok else "FIX NEEDED")
