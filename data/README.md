# Data

This is where all my data is collected, stored, processed, etc.

Data is first collected using `data_collection.py` and various other helper functions stored in other files. This data is then stored in `data.txt`. I then run another script called `simplify_data.py` to remove useless/repetitive information, reorganise data and make some minor extraplotions to reduce the number of data points that need to be processed. This is then all stored in `simpData.txt`. To speed up data collection, I seperated this into several different processes and files that could all run in parallel. The final cleaned data is then combined together in a single text document called `cleanData.txt` that is then fed to the models.

For ease of use, `make_frame.py` provides a function that takes this data and turns it into a pandas dataframe so that I can easily request for it in the future. Depending on the format and type of data requested, I can return different formatted dataframes.
