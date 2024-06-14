# Calculate Dice Similarity Coefficients for 2 NIfTI Masks

Given two binary segmentation masks $X$ and $Y$ (which in our case, were created manually), dice.py calculates the following: 
$$D = \frac{2 |X \cap Y|}{|X + Y|}$$
The numerator can be thought of as "2 * (area of overlap)" and the denominator can be thought of as "(total area)".

## Usage
You can download and run either dice.py (helpful if you'd like to edit it locally) or the executable (ready to go, requires no packages to run). For example, if you're currently in the folder with your masks, you can run either of the following from the command line:
```
# dice.py
python /path/to/dice.py mask1.nii mask2.nii 
```
```
# dice executable
/path/to/dice mask1.nii mask2.nii 
```

The package requirements for running dice.py are in requirements.txt. If you use python regularly, you could probably get away with installing nibabel and calling it a day. Otherwise, any one of the following lines will install the required packages; the last one will create a whole new conda environment.
```
pip install -r requirements.txt

# use if you're currently in a conda environment
conda install --file requirements.txt

# creates a new conda environment with required packages
conda create --name nki-dice --file requirements.txt
```





