import sys, argparse
import numpy as np
import nibabel as nib

# def binary_mask(dat): return np.where(dat!= 0, 1, 0) # ifelse
# returns nifti data as binary mask; unnecessary for us bc we will recieve masks for the LC region

# get_data(args):
# checks validity of provided files (must be a nifti image)
# args: arguments recieved by argparse
def get_data(args):
    f1, f2 = args.filename
    try: 
        img1 = nib.load(f1)
        img2 = nib.load(f2) # nibabel image objects

        img1_data = img1.get_fdata()
        img2_data = img2.get_fdata()

        # nifti_data = []
        # for file in args.filenames:
        #   nifti_img = lib.load(file)
        #   nifti_data.append(nifti_img) # for 2+ arguments
 
        return img1_data, img2_data
    except nib.filebasedimages.ImageFileError:
        print("Unable to read one or more file. Ensure file types are in NIfTI-1 or NIfTI-2 format and try again.")
        sys.exit(1)
    except: 
        print("Something went wrong reading your files. Make sure the file exists, re-check file types, and try again.")
        sys.exit(2)

# dice_coefficient(dat1, dat2)
# calculates dice coefficient between two binary masked nifti files
# dice = (2 * area of overlap) / (total area)
# dat1, dat2: binary masked nifti files (see binary_mask())
def dice_coefficient(dat1, dat2):
     overlap = np.sum(np.logical_and(dat1, dat2)) 
     return (2 * overlap) / (np.sum(dat1) + np.sum(dat2))


def main():
    # ensure we recieve 2 file names as arguments
    parser = argparse.ArgumentParser(
        description="Returns Dice Similarity Coefficient (DSC) between two (2) segmentations.")
    parser.add_argument("filename", 
                        nargs = 2,
                        help = "File names of the two (2) .nii binary masks you hope to calculate the Dice Coefficient for, separated by a space.") 
    
    # features for later?
    """parser.add_argument("--save",
                        nargs = 1, 
                        help = "Allows you to save the intersection of your volumes to a file. You must specify a filename after this argument.", 
                        required = False)"""
    
    args = parser.parse_args()
    
    dat1, dat2 = get_data(args)
    print(dice_coefficient(dat1, dat2))
    

if __name__ == "__main__":
    main()