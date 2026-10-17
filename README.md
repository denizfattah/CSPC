# CSPC Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW 1 /Lab A/.

## Setup
Create the environment for a given lab:
conda env create -f PW 1 /Lab\ A/environment.yml
conda activate cspc

## PW1
Lab A: Reproducible Foundations

*What I built:* 
A personal course repository with version control, a Conda environment, and automated tests.

*Speed comparison (loop vs NumPy):* 
- loop: 0.485 s
- numpy: 0.016 s[cite: 35]
- speed-up: ~29x faster

*Tests:* all passing? yes

*Conclusion:* 
Successfully configured Miniconda and Git workflow. Observed that NumPy executes simulations much faster than standard Python loops. Handled repository constraints by omitting large files.
