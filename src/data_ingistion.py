import pandas as pd
from sklearn.model_selection import train_test_split

def data_load():
    data = pd.read_csv(r"C:\Users\Mrityunjay\DS-Online\MlOps\Basic_ml_pipeline\ML-pipline-using-DVC\Tweets.csv")


def data_preprocess():
    data = data.drop("textID")
    final_df = data[["selected_text", "sentiment"]]
    
def data_split():
    X = final_df["selected_text"]
    y = final_df["sentiment"]  
    X_train,X_test,y_train,y_test = train_test_split(X,y)

def main():
    data_load()
    data_preprocess()
    data_split()

    
if __name__ == "__main__":
    main()