import machine as ma

def main():
    x_train_us, x_test_us, y_train_us, y_test_us =  ma.preprocess()
   
    model = ma.train(x_train_us,y_train_us)
    
    
if __name__ == "__main__":
    main()
