import os

os.system("python src/data_ingistion.py")

os.system("python src/data_preprocess.py")

os.system("python src/feature_engineering.py")

os.system("python src/model_bulding.py")

os.system("python src/model_evaluation.py")