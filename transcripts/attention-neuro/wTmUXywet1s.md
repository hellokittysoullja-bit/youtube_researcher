# 1369: A model of selection history in visual attention
CogSci: Interdisciplinary Study of the Mind · 15 мин · 48 просмотров · en · https://youtu.be/wTmUXywet1s



[00:01] hello everyone i'm nadal meibody and i'm presenting a model of selection history and visual attention selective visual attention is a brain function that filters irrelevant sensory inputs to focus on relevant items and it is traditionally known as an interaction between bottom-up and top-down mechanisms later selection history is proposed and it is known as the third category of attention guidance 

[00:32] selection history comes to play when an object is emphasized because of previous attentional deployments in the same context and it includes different different phenomena such as learning priming and also reward-based bias to show how bottom-up top-down and selection history work together to guide visual attention toward a specific target we presented an algorithmic model we call this model algorithmic in sense 

[01:04] of more and the model connects visual stimuli to human behavior by selection history here we mean the effect of learning from previous experience and the current task the behavior the behavioral data of the first experiment that was proposed by feldman and others is used for modeling the experiment was a psychophysical experiment with recording of responses 

[01:34] reaction times and eeg in this experiment an associative learning task was combined with a visual search task as you see here in these examples in all tasks there is a fixation point on a screen and eight different elements around the fixation points experiments has two type of two types of tasks learning and search in learning tasks color or shape had to be categorized based on 

[02:05] participants group membership in search task the orientation of the line in the diamond had to be reported in half of the trial there is a red distractor available participants were randomly divided into two groups color group and shape group in learning tasks participants in color group had to categorize the color singleton blue versus green and participants in shape group had to 

[02:35] respond to the shape singleton triangle versus pentagon participants with left hand pressed one of two buttons placed on the left side of the response pad in search tests all participants reported the orientation of the line in the diamond horizontal or vertical participants with right hand press one of two buttons on the right side of the pad 

[03:08] if the responses were incorrect participants received beep sounds as feedback the experiment was done in two phases practice phase and main phase in practice phase participants had to learn and learn on a trial and error basis that either color or shape was the response to relevant in main phase participants performed 

[03:38] both tasks learning and search in random orders as you see here in this example the assumption was that the learning experience should affect attention deployment in the search task and also a between group difference is in attention deployment was expected to shape target and color distractor the experimental results showed 

[04:09] participants in the color group got distracted by color distractors in the search task much more than participants who had learned about the shape both reaction time analysis and eeg results indicated an attentional bias as you see here for search task the mean the mean of the reaction times for distracted present tasks in color group is higher than the mean of the reaction times for the same 

[04:40] tasks in shape group this attention bias can neither be explained by bottom-up nor by top-down control but is resulting from the participant's individual selection history reaction time database of this experiment is used in current study for modeling as you see here there is our there is the schematic of our model 

[05:12] and the model starts uh by extracting features from the experiment tasks and after taking several steps it predicts the parameters of the reaction time distributions by distributions here we mean exponential gaussian several probability functions were ver were repeated under observed data by maximizing like 

[05:42] likelihood and the best fitted one x gaussian was selected for modeling why exponential gaussian because reaction times are not distributed normally because of the line tail on the right they might have an exponential component x gaussian is a convolution of gaussian and exponential distributions and it has three parameters mu sigma x gaussian has been popular recently in 

[06:15] analyzing psychophysical data in next slides i go step by step through the model to see how our model works this is the first step then by feature extraction feature maps are made color map shape map orientation map based on feature integration theory the theory says in pre-attentive stage stimulus features like color or shape are encoded in parallel 

[06:48] next step is making saliency maps and we used self-information maximization to make our saliency maps it was proposed before in a saliency model that was called attention based on information maximization then later saliency maps and history map are integrated into priority map integrated priority map 

[07:19] is a theoretical framework to explain how selection history and other factors of attention guidance interact priority maps are lean are linear and linearly mapped into reaction time parameters here you see the weights that are actually the model's parameters uh ws is saliency vades and has three 

[07:52] components for color shape and orientation and wh is history rates wd and bd are reaction time distribution parameters and reaction time distribution biases and each of them has three components mu sigma in machine learning part of the model 

[08:22] the model learns to predict the the parameters of reaction time distributions while goal driven information in top top down manner controls the the way that maps are combined into a priority map by affecting the weights to compare how how model predicted 

[08:52] distributions are close to reaction to real distributions we plotted them here on these examples for color group participants and shape group participants and as you see the model predicted one that's it that is in green is uh very close to the real one and fitted well on our reaction time database to quantify how close the the model 

[09:25] predicted distributions are to best fitted distributions we evaluated kl divergence and it returns a very small numbers to see how selection history or history map can affect our model we tested three versions of the model first one in first one that is a feature that has a feature level selection history the 

[09:55] history map contains the response relevant features in the learning phase blue or green for the color group triangle and pentagon for the shape group in second model that that has a dimensional level selection history the history map includes all color singletons for participants in color group and all shape singletons for participants in shape group here on the bar charts you can see the 

[10:26] model evidences for model comparison we used loplast approximation and we also fitted the model for participants and then per groups and in all cases model one scores the best as you remember we talked about the debates ws and wh saliency maps weights and history map weights to to see how 

[10:57] the model learns to predict these weights and how these weights differ between color group and shape group we plotted them here on this bar charts for both color and shape group and then if we look at history and color [Music] color map weights we see that they are higher in color group than the ones in the shape group participants in color group responds to 

[11:28] the learning tasks by relying on history and color and also higher history rates than color weight here shows an effort on red distractor suppression in search task orientation map and shape map in color group as you see orientation map has the highest weight by that participant in color group 

[12:00] responds to the search tasks and also they ignore the irrelevant shape singletons in learning tasks in shape group the highest weight is for shape map by that participants in shape group solve the learning tasks 

[12:30] and also in search task attention can be guided to the shape singleton i mean the diamond that contains the targets so shape map is response relevant in in both tasks if i want to compare the results of the experiments with the model the experiment showed a bottom uh bisphen group difference the model also captures bits from group differences by 

[13:01] giving different weights to the maps in color and shape group the experiment showed attentional bias to the red distractor in color group the model also shows an attentional bias to the distractor in the color group by giving higher weight to the color map in color group while this states in is close to zero in shape group so in general this attention bias can be the result of the participants 

[13:32] individual selection history and also the model shows different selection history effects between groups by giving higher weight to the history map in color group than shape group so in conclusion we presented a model of selection history and visual attention the model successfully predicts the reaction time distribution parameters and the model shows integrated priority map can be a successful 

[14:02] framework to explain how attention mechanisms interact we tested different versions of the model and the model which includes selection history the bottom up and tap down control is the best suited for describing and describing the behavioral results or reaction time results in our next steps we tried to add inter trial priming 

[14:32] effect and task switching effect to the model and also we will make a computational model for both ideal and non-ideal observers to know what the attentional system is trying to achieve thank you for your attention you 
