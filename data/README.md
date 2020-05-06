# Data

This is where all my data is collected, stored, processed, etc.

Data is first collected using `data_collection.py` and various other helper functions stored in other files. This data is then stored in `data.txt`. I then run another script called `simplify_data.py` to remove useless/repetitive information, reorganise data and make some minor extraplotions to reduce the number of data points that need to be processed. This is then all stored in `simpData.txt`.

For ease of use, `make_frame.py` provides a function that takes this data and turns it into a pandas dataframe so that I can easily request for it in the future.
