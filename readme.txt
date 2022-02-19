1. The code is design based on Python 2.7.15 and Scikit-learn 0.20.4 with the dependence of Biopython 1.72,Numpy 1.16.5,Pandas 0.24.2.
2. The input sequence should be fasta format with 40 amino acids£¬
3. "BIVPred_FL.py" is the main file.
4. "predicting_results.csv" is the result file for virulence.
5. The folder "feature" contains all of the 67 features of your sequences.
6. The folder "model" contains the trained model based on random forest algorism and our dataset.
7. The predicted label for 'P' means the pandemic risk, while label for 'N' means not.