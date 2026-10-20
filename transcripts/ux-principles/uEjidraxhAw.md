# Why Disabled Buttons Hurt UX (and How to Fix Them)
NNgroup · 4 мин · 15429 просмотров · en · https://youtu.be/uEjidraxhAw



[00:00] -Imagine you are on restaurant website trying to join the waitlist. You spot a big gray Join Waitlist button. Perfect. You click it, but nothing happens. You try again, refresh the page, still nothing. You're left wondering what went wrong. Congratulations, you are fooled by a disabled button. A disabled button is a interface element that is temporarily inactive and can't be clicked. Typically, it's grayed out, 

[00:31] signaling to users that it's not available for interaction. The use of disabled buttons is a infamous debate in UX, sitting a somewhat gray area, just like how the button itself looks. Contrary to popular belief, disabled buttons don't actually violate contrast guidelines. According to WCAG, buttons that can't be interacted with are not required to meet contrast standards. While they may be low contrast, they don't technically break the rule. 

[01:02] Just because disabled buttons don't break the rules, it doesn't mean they are good UX. Let's talk about four reasons why disabled buttons are problematic. First of all, they are deceptive. The call-to-action text draws users to click, but nothing happens. This is also known as a negative affordance, which often causes confusion. Secondly, the low contrast makes the label difficult to see and read. Even if the button is disabled, 

[01:34] the button label is still crucial for understanding the context of the interface. What's more, disabled button don't provide feedback. Without feedback, how would users know what's gone wrong and how to fix the error? Last but not least, disabled buttons add complexity. The intention of disabled button is simple. To prevent users from wasteful clicks when requirements are not met. However, not allowing users to click on the button and receive system feedback 

[02:06] actually puts the pressure back on the design team to create a bulletproof inline validation system. In reality, even the most sophisticated validation systems can fail. When they do, users are left stuck with a disabled button and no way to complete the form. Does that mean we should avoid disabled buttons at all costs? Not necessarily. One useful case is when the button is clicked, and the action is processing or is no longer available. 

[02:38] Here, switching the button to a disabled state acts as a micro-interaction, informing users of the system update and preventing repeated attempts. For example, after a user requests an SMS code, disabling the button stops them from making multiple requests, which can overload the system and cause confusion. What does all these mean to us, as designers? I want to leave you with three actionable tips. 

[03:09] To begin, only use disabled buttons when there is a strong reason, such as to indicate unavailable actions, prevent duplicate submissions, or signal ongoing processes. When you do decide to include a disabled button, design it to be more inclusive, make it focusable for keyboard users, and allow screen readers to announce the element. Most importantly, explain to your users why the button is disabled 

[03:39] and how to proceed. Lastly, avoid making active buttons look disabled. Users tend to associate gray with inactivity. Make sure active buttons are visually distinct from inactive ones to avoid confusion between what can and can't be clicked. Disabled buttons can be useful in specific cases, but they often cause more harm than good. Use them wisely, ensure they are accessible, and always provide clear feedback to your users. 
