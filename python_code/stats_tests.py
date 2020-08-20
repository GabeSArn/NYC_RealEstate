from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARMA

def info():
    print('The purpose of this python file is to run statistical test on data files')

def dickey_fuller_test(series):
    dftest = adfuller(series, autolag='AIC', regression='ct')
    print("Test statistic = {:.3f}".format(dftest[0]))
    print("P-value = {:.3f}".format(dftest[1]))
    print("Critical values :")
    for k, v in dftest[4].items():
        print("\t{}: {} - The data is {} stationary with {}% confidence".format(k, v, "not" if v<dftest[0] else "", 100-int(k[:-1])))
        
def run_arma(series, p,q):
    mod_arma = ARMA(series, order=(p,q))
    res_arma = mod_arma.fit()
    return res_arma.summary()

def create_dataset(dataset, look_back=1):
    X, Y = [], []
    for i in range(len(dataset)-look_back-1):
        a = dataset[i:(i+look_back), 0]
        X.append(a)
        Y.append(dataset[i + look_back, 0])
    return np.array(X), np.array(Y)