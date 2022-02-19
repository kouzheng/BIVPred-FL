import feature
import predictor
import predic_fl

if __name__ == "__main__":
    fname=raw_input("Fasta file for 40 amino acids:")
    ft_type=raw_input("1 for class;2 for prob:")
    ft_num=int(raw_input("feature number:"))
    pconf=float(raw_input("Prediction confidence 0.5-1.0:"))
    
    feature.ft(fname)
    predictor.pr(ft_type)
    predic_fl.prfl(ft_type,ft_num,pconf)
    

