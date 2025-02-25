import os
from pathlib import Path
import argparse

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_dir', type=Path, required="True", help="Path to the MSLesSeg-RAW dataset")
    parser.add_argument('--ref_template', type=Path, default = "./resources/MNI152_T1_1mm.nii", help="Path to the MNI152 template")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse()
    for root, dirs, files in os.walk(args.dataset_dir):
        path_replace = root.replace("MSLesSeg_RAW", "MSLesSeg_registered")
        os.makedirs(path_replace, exist_ok=True)
        template = args.ref_template
        
        if len(files)>0:
            for filename in files: 
                print(filename)
                if filename.endswith("FLAIR.nii.gz"):
                    path_flair = os.path.join(root, filename)
                    path_flair_registered = os.path.join(path_replace, filename)
                elif filename.endswith("T1.nii.gz"):
                    path_t1 = os.path.join(root, filename)
                    path_t1_registered = os.path.join(path_replace, filename)
                elif filename.endswith("T2.nii.gz"):
                    path_t2 = os.path.join(root, filename)
                    path_t2_registered = os.path.join(path_replace, filename)
            
            #REGISTRATION
            os.system(f'flirt -in {path_flair} -ref {template} -out {path_flair_registered} -omat {path_replace}/flair_matrix.mat')
            os.system(f'flirt -in {path_t1} -ref {template} -out {path_t1_registered} -omat {path_replace}/t1_matrix.mat')
            os.system(f'flirt -in {path_t2} -ref {template} -out {path_t2_registered} -omat {path_replace}/t2_matrix.mat')

            #BRAIN-EXTRACTION
            os.system(f"bet {path_flair_registered} {path_flair_registered}")
            os.system(f"bet {path_t1_registered} {path_t1_registered}")
            os.system(f"bet {path_t2_registered} {path_t2_registered}")
            