# Airbnb Interview Question: Least # of Activities
Intuting Studio · 7 мин · 1591 просмотров · en · https://youtu.be/Moo1_s7ezzI



[00:00] [Music] hey everyone today we'll go over another Airbnb phone screen interview question the question is given a list of activities find the minimum number of activities to fully occupy the target hours you can repeat the same activity more than once let's 

[00:32] get started let's say we have the following activities hiking VR game and movie and they take one hour two hours and three hours respectively if our target hours is three a single movie activity would give the minimum number of activities if our target hours is seven two movies and hiking activities would give the minimum number of activities similar story when our target 

[01:02] hours is eight let's see how we can do this programmatically one easiest way to do this is to look at all possible combination that adds up to the target hour and see what's the minimum number of activities this is the brute force approach during the actual interview I started with this per this brute-force approach and actually failed one of their test cases because the algorithm simply took too long to complete another approach is to use dynamic programming we can start by finding the minimum number of activities required to occupy 

[01:33] one hour two hours three hours and up to the target hours in every time we find the minimum number to occupy X hours we store the result in this map so we can look it up and constant time so when we fill everything out this map will pretty much tells you that for the given hours X what's the minimum number of activities to perform let me illustrate how we can exactly accomplish this let's start with one hour as our target we go through all the given set of 

[02:05] activities and see if including any one of them would ill the minimum number in total the formula to find the minimum number of activities would look something like this all right let's start with hiking so our target hours is 1 and activity hours is 1 so remaining hours become 0 so map of 0 is 0 just right here plus 1 so our minute count becomes 1 for this and 

[02:36] let's look at the or game and movie target hours still one activity hours is 2 this becomes a negative number it means with a given target hour it's not possible to perform either sorry it's not possible to perform this particular activity that's this case the VR game or a similar story for a movie so these two would be simply impossible so you update the target hour with one 

[03:10] from here all right let's do something similar for target hours equals 2 when we choose to do hiking target hours just to activity hours is 1 so remaining hours 1 the mapup remaining 1 so map up 1 is 1 so 1 plus 1 is 2 so the min count is 2 when we choose to add hiking let's do the same for VR game the target hours as 2 activity hour is 2 so this becomes 

[03:42] 0 map of 0 is 0 0 plus 1 is 1 so the mint count becomes 1 for this a movie it's similar so it's impossible so out of these two main counts 1 it's a small smaller one so you update it here what that can let's continue to fill our app map for a three and four hours for three hours let's say we choose to do hiking then our remaining hour so target hours is 

[04:12] three in this case and activity hours is 1 so the remaining hours is 2 so map up 2 is 1 1 + 1 is 2 so if you choose to include hiking then the number of minimum count becomes 2 let's look at the VR game so target hours is 3 again 3 again and activity hours is 2 so this becomes 1 and member 1 is 1 so 1 plus 1 

[04:43] is 2 again so if you choose to include the our game the minimum count becomes 2 and let's say for the movie the movie takes 3 hours so the target hours just 3 activity hours just 3 so this becomes 0 and mem pup 0 is 0 so 0 plus 1 is 1 alright so out of all these options one is the smallest so the mid for target I was 3 the minimum number of activity is once again 1 right let's look at target hours 

[05:17] equals 4 when we choose to do hiking once again remain target hours to spawn remaining the activity hours just 1 so the remaining hours is 3 so minimum count so map of 3 is 1 and 1 plus 1 is 2 so hiking becomes 2 let's save the organ the our game is 2 hours the target is for activity ours is 2 so 

[05:48] this becomes 2 so minimum count map of 2 is 1 so 1 plus 1 is 2 again a similar story for the movie this becomes 2 so these are all the same so the target R is equal 4 it will be 2 all right I hope this makes sense and then you continue doing this until your target hour in and this should give it this should give you the minimum number of activities you can perform to fully occupy target our end i've pre 

[06:22] calculated the numbers up to target hours equals 7 as we discuss in our example slide we can see that the minimum number to occupy the target hours 3 & 7 matches what the answer we had earlier it would take order of K times n to complete this where a case the target hours and n is the number of activities spend some time to understand this algorithm and translate this idea into code if you're done compare with the full solution I included in the description section below 

[06:53] I hope this video helped you to prepare for technical interviews do not forget to Like and subscribe I'll see you in the next video [Music] 
