# Designing AI Allies - How Games Create Great Party Members and Companions ~ Design Doc

**Канал:** Design Doc · 12 мин · субтитры: en (ручные) · https://youtu.be/tIze-mre0ss

> «Слова автора» — дословный текст из транскрипта (убраны только um/uh и заикания; в авто-субтитрах мало знаков препинания). «Мысль» и «Для Напарника» — вывод разметчика, это не речь автора.


---

## 1. Компаньон должен вносить вклад, не забирая игру у игрока
`маскот · персонаж · игровой-дизайн` · [00:48](https://youtu.be/tIze-mre0ss?t=48)

**Мысль:** Слишком полезный союзник играет вместо игрока, слишком слабый становится обузой или забывается.

**Слова автора:**

> So you need to rely on AI to control your allies. Designing and fine tuning their automated behavior can make or break an entire game. If they’re too useful or powerful you risk them playing the game for you. If they’re too weak or ineffective they could become an unintentional liability or you might forget that they're even there. In a perfect world these characters should feel like they make a real contribution without stealing the fun from the player.

**Для Напарника:** Кот-напарник присутствует и поддерживает, но не делает задачу за человека.


---

## 2. Палико: компаньон как источник бонусов, а не опоры; автономия без обузы
`маскот · игровой-дизайн · психология · награды` · [01:22](https://youtu.be/tIze-mre0ss?t=82)

**Мысль:** Позиционирование союзника как дающего бонусы вместо ключевого помощника меняет ожидания; нет серьёзного штрафа за потерю здоровья; и это милый кот.

**Слова автора:**

> There's an idea in psychology called Loss Aversion that says that losing something feels more negative than gaining it feels positive. One way to design an AI around Loss Aversion is instead of depending on a character and being disappointed if they fail to help, switch it up and have an AI character occasionally give out bonuses. Just framing the player’s expectations differently can make them happier, even if they’re getting the same benefits on average either way. The palicos of Monster Hunter World are a good example of how to design around Loss Aversion. Palicos are great at distracting monsters and creating opportunities during fights. They don’t do much damage, but they make up for it in utility and customization. They can be equipped with status-inflicting weapons and special palico tools that can heal you, give you buffs, set up traps, or they can even steal monster materials. They will use these skills on their own but you can command them manually if you want to. There’s no major penalty if they run out of health, either. They have autonomy without being a liability. Some palico equipment loadouts are better than others, but they all provide at least SOME benefit, but never so much that they make the monster hunting at the core of the game too easy. If Monster Hunter framed palicos as allies that did a major part of the monster hunting, the same behaviors would feel disappointing. But since they're more of a companion that gives out bonuses, and they only show up when you don’t have many actual players in your party, they feel like good partners. They're great during the beginning of the game while you figure out the ropes, and they don't get in the way of high-end monster hunting. And above all, it’s a cat. It’s adorable. Don’t overthink it.

**Для Напарника:** Кот как приятный бонус (находки, реплики) без вины, если он «не помог»; смерть и штрафы исключены.


---

## 3. Расхождение между заявленной ролью союзника и тем, что он делает
`маскот · игровой-дизайн · доверие` · [05:12](https://youtu.be/tIze-mre0ss?t=312)

**Мысль:** Если игра говорит «команда», а делает «шоу одного героя», создаётся разочарование.

**Слова автора:**

> Ally design can also become a problem if you don't properly frame what the AI members should be responsible for. In Star Fox Assault, there's a disconnect between what the game SAYS the AI characters are there for and what the game actually DOES with them.

**Для Напарника:** Роль кота (присутствие, а не надзор) должна совпадать с его поведением на всех экранах.


---

## 4. Микроменеджмент приемлем, когда он заявлен как часть игры (gambits в FFXII)
`игровой-дизайн · психология · мотивация` · [07:11](https://youtu.be/tIze-mre0ss?t=431)

**Мысль:** Одна и та же ручная настройка раздражает в одной игре и радует в другой: решает ожидание игрока.

**Слова автора:**

> Just make the AI yourself, you should try Final Fantasy XII. The gambit system in FFXII lets you program exactly the steps, or ‘gambits’, that your AI party members will take in battle in a kind of Lego brick sort of way. For example, you can set a gambit to have a character cast healing spells whenever someone’s HP drops below a set threshold, or automatically cast Haste on the party whenever you can. More advanced and specific conditions for gambits can be found in shops as the game progresses. You also have to consider the priorities of your gambits, placing more situational instructions at the top and common ones at the bottom. If you have attacking nearby enemies as a top priority, the other gambits will never be used. It's not that far off in concept from what an actual AI programmer might code, but this way you feel like you’re in control if the AI screws something up. Even though the gambit system needs micromanaging like in Kingdom Hearts the framing is completely different. Managing gambits is a huge part of the game, so it's not as frustrating as the micromanaging was in Kingdom Hearts. Players expect it, so they’re OK with putting in the time.

**Для Напарника:** Настройки Напарника скрыты по умолчанию; кому нужно, найдёт, и не будет раздражаться.


---

## 5. Атрей: всегда ощущается как вклад, одна кнопка, не нужно микроменеджмента
`маскот · персонаж · игровой-дизайн` · [08:33](https://youtu.be/tIze-mre0ss?t=513)

**Мысль:** Помощник стреляет, оглушает, подсказывает и решает головоломки, не превращаясь в эскорт; нарушение послушности подаётся как осмысленный сюжетный ход.

**Слова автора:**

> God of War 4’s story is all about the father-son relationship between Kratos and Atreus. The developers at Santa Monica designed Atreus to always feel like he was contributing during combat. He can shoot arrows and summon creatures on your command with a single button. He’ll follow up on your attacks when he’s nearby and he can distract and stun enemies and open them up for you. You don’t have to micromanage him beyond equipping stat boosting gear and occasionally saving him when he gets caught by an enemy. Atreus also acts as your hint guide and helps you solve puzzles. He’s not treated like an escort character but the game does turn him into a liability in combat to fit with some of the story beats. In a later section of the game, Atreus won’t always listen to your commands and will recklessly lead you into bad situations. He’ll even start using the special summon attacks on his own regardless if it's well timed or not. For some this sequence can come off as rushed, but it's a deliberate choice and it's an effective way to tie together an antagonistic AI character in the story with their behavior in the gameplay.

**Для Напарника:** Кот реагирует на события по одному касанию; необычное поведение допустимо только как заслуженный сюжетный момент.


---

## 6. Неконтролируемые раздражающие действия союзника оправданы только сюжетной причиной
`маскот · игровой-дизайн · психология` · [10:21](https://youtu.be/tIze-mre0ss?t=621)

**Мысль:** Без причины ничто не уравновешивает раздражение от плохих действий, которыми нельзя управлять.

**Слова автора:**

> With a good story driven reason, even the most annoying character actions can have purpose and make the game better. But without a reason there's nothing left to counter the raw annoyance that uncontrollable bad actions inherently have.

**Для Напарника:** Кот не должен делать то, что нельзя отключить или управлять (звук, реплики).


---

## 7. Баланс: помощь без захвата игры и ввод без постоянного ведения за руку
`маскот · ИИ · игровой-дизайн` · [11:48](https://youtu.be/tIze-mre0ss?t=708)

**Мысль:** Ожидания игрока и корректная рамка превращают ИИ в союзника.

**Слова автора:**

> AI design is hard to do. Developers have to find the balance between an AI that feels like a help without taking over the game, between an AI that takes input from players but still doesn’t need their hand held all the time. Lots of games get the balance wrong for lots of reasons. But by learning from mistakes made in the past, taking some cues from psychology, and setting expectations properly you can turn an AI into an ally.

**Для Напарника:** Чат с котом: просить минимум ввода, давать значимую помощь, не вести за руку.
