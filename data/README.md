# Data

This is where all my data is collected, stored, processed, etc.

Data is first collected using `data_collection.py` and various other helper functions stored in other files. This data is then stored in `data.txt`. I then run another script called `simplify_data.py` to remove useless/repetitive information, reorganise data and make some minor extraplotions to reduce the number of data points that need to be processed. This is then all stored in `simpData.txt`. To speed up data collection, I seperated this into several different processes and files that could all run in parallel. The final cleaned data is then combined together in a single text document called `cleanData.txt` that is then fed to the models.

For ease of use, `make_frame.py` provides a function that takes this data and turns it into a pandas dataframe so that I can easily request for it in the future. Depending on the format and type of data requested, I can return different formatted dataframes.


## Data Collected
I will average each of these across a season to get a better idea. (Future version: try median as well?)

**Wins/Losses/Ties**: These are the W/L/T of a team for a specific tournament. 

**Rank**: Their final placement at the end of a tournament. (1st, 2nd, 3rd etc.) 

**WP**: Win Points, a measure of how much you beat the other team by in a specific match. These points are awarded based of the point difference between the two teams at the end of a match.

**AP**: Autonomous Points, the number of points scored by a team during the autonomous period in a specific match.

**SP**: Schedule Points, a measure of the difficulty of a teams schedule in a tournament. Strength of Schedule Points are awarded in the amount of the score of the losing alliance in a Qualifying Match.

**TRSP**: Truly Representative Schedule Points, a (usually) better measure of the difficulty of a teams schedule in a tournament. It takes into account your teammates and opponants strength to hopefully better gauge schedule difficulty.

**Max Score**: The the maximum score a team acheived in a tournament.

**OPR**: Offensive Power Rating, a measure of how offensive a team is in a specific match. Calculated by the number of points scored by that team.

**DPR**: Defffensive Power Rating, a measure of how defensive a team is in a specific match. Calculated by the number of points scored by the other team.

**VRating and VRating-Rank**: These are a collection of scoring and ranking methods originally devised by the well known team BNS. Although I could not find exactly how they were calculated (it is not publically available), it is known that it uses a combination of factors including score, ranking and many other factors. It is not uncommon for some teams to base their analysis and predictions of other teams off of these scores. There is some debate in the community surrounding the effectiveness of these numbers in actually being able to determine the outcome of matches as well as the performance of teams. Using statistical analysis to determine this once and for all is an interesting secondary goal.

**Red Score/Blue Score**: These are the raw final scores of a team at the end of a match.
