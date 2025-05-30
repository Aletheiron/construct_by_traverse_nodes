How about constructing house with Lego bricks using optimization by voyage through nodes?
I used my ordinary model with traversing nodes and maximization of the utility function.
Now node doesn’t represent math function, but action in the real world. 
For example, “Change position by one step higher and place here a thing of the type A”.
Then we need utility function updates. I will use human-base assessment of the similarity. I give +1 point, if chosen brick and position can theoretically appear. -1 in all other cases.

Then I used modern LLM to assess out steps. And this time I will use Gemini-2.5 Pro.
I will take photo of the offered action, then pass it to the AI and ask digital measure of accordance with reference. 

Prompt will be: “Provide measure from 0 to 10 of similarity of the picture 2 to the picture 1”. Where picture 1 is the model house. 
If this measure growths, I will assign growth to the utility function. Of course we can automatize the whole process. 
So, this is the process.

