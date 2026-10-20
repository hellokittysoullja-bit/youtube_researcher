# Workflows at Scale: Design Systems, Platform Engineering, and the AI Workflows that scale

**Канал:** Design Systems London · 16 мин · субтитры: en (авто YouTube) · https://youtu.be/pI12krTC5n8

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. ИИ не чинит сломанную систему, а усиливает то, что есть
`ИИ · дизайн-система · процесс` · [10:28](https://youtu.be/pI12krTC5n8?t=628)

**Мысль:** Несогласованная система даст несогласованность в масштабе, а ИИ при хардкоде токенов будет уверенно ошибаться. При структурной системе ИИ становится множителем.

**Слова автора:**

> AI doesn't fix a broken design system. It amplifies what's already there. If your system is inconsistent, AI will generate inconsistency at scale. If your tokens are hard-coded and your components undocumented, AI will guess and AI will guess wrong confidently. But if your system is structured, your tokens semantic, your APIs consistent, and your documentation clear, AI becomes a genuine multiplier.

**Для Напарника:** Перед генерацией UI через ИИ в Напарнике держать токены и компоненты упорядоченными; CLAUDE.md выполняет роль такого брифа.


---

## 2. Не промпт, а бриф: дай ИИ токены, компоненты и гайдлайны
`ИИ · процесс · дизайн-система` · [11:13](https://youtu.be/pI12krTC5n8?t=673)

**Мысль:** Агент хорош ровно настолько, насколько хорош контекст; ему нужны файл токенов, компоненты, бренд-гайд, как новому дизайнеру, а не весь код без ограничений.

**Слова автора:**

> Most people think scaling with AI is about writing better prompts. It isn't. It's about context. The agent is only as good as what you give it to work with. If you're If you give it your entire codebase without constraints, it will produce something that technically works but visually fails. If you give it your token file, your component file, or your brand guidelines, you're not prompting, you're briefing. And that's a very different thing. Think of it like you're onboarding a new designer. You don't just give them a laptop and say, "Good luck." Well, I hope that's not what you do. You'd give them the brand guidelines, the component library, the do's, the don'ts. AI needs the same briefing.

**Для Напарника:** Системные промпты api/companion и api/session-voice: передавать краткий бриф тона и запретов (без стыда, без вины), а не только просьбу.


---

## 3. Ограждения, а не запрет: ограничения делают автономию безопасной
`ИИ · этика · доверие · тексты` · [13:21](https://youtu.be/pI12krTC5n8?t=801)

**Мысль:** Агентам не запрещают генерировать, а делают невозможным выход за границы: токены, API компонентов, где неправильное использование труднее правильного, ясная документация.

**Слова автора:**

> This isn't a reason to panic, but it is a reason to build guardrails. Guardrails that are baked into your platform that agents can so that agents can generate freely within your system without breaking it. They are constraints that make autonomy safe. Token boundaries that tokens cannot that agents cannot cross. API component APIs designed to make misuse harder than correct use. And documentation written clearly that an agent not only understands what a component does, but where to use it. The goal isn't to stop AI from generating, but to stop AI or to make it impossible for AI to generate off-brand.

**Для Напарника:** Реплики ИИ-напарника: жёсткие границы тона на уровне промпта и пост-фильтра (никаких упрёков), внутри них свободная генерация.
