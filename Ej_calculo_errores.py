import numpy as np
import tensorflow as tf
import pandas as pd

data = pd.read_excel('Table_3_fretting_fatigue_life_estimates.xlsx')

y_V = data.iloc[:, 2].values
y_P = data.iloc[:, 1].values
y_exp1 = data.iloc[:, -2].values 
y_exp2 = data.iloc[:, -1].values
y_exp = np.concatenate((y_exp1, y_exp2))
y_predV = np.concatenate((y_V, y_V))
y_predP = np.concatenate((y_P, y_P))
 

def desv(y_true, y_pred):
    
    alpha = np.zeros(len(y_true))
    S_alpha = np.zeros(len(y_true))
    for i in range(len(y_true)):
        alpha[i] = np.log10(y_pred[i]/ y_true[i]).item()
    alpha_av = tf.reduce_sum(alpha) / len(alpha)
    for i in range(len(y_true)):   
        S_alpha[i] = (alpha[i] - alpha_av)**2
    x_av = tf.pow(10,alpha_av)
    S_x = tf.pow(10,(tf.sqrt(1 / (len(alpha) - 1) * tf.reduce_sum(S_alpha))))
    return x_av, S_x

x_V , S_V = desv(y_exp, y_predV)
x_P , S_P = desv(y_exp, y_predP)

print(f"Valores para Vallellano: x_av = {x_V}, S_x = {S_V}")
print(f"Valores para Paris: x_av = {x_P}, S_x = {S_P}")