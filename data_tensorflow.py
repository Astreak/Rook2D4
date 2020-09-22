import tensorflow as tf
import numpy as np
import pandas as pd

def process(data,stamp=1):
	X=[]
	y=[]
	for i in range(stamp,len(data)):
		X.append(data[i-stamp:i])
		y.append(data[i:])
	from sklearn.preprocessing import MinMaxScaler
	sc=MinMaxScaler()
	
	X,y=np.array(X),np.array(y)
	return (X,y)

def build_cell(X,y):
	X=X.astype("float64")
	model=tf.keras.models.Sequential()
	model.add(tf.keras.layers.GRU(12,activation="sigmoid",return_sequences=True,input_shape=(None,X.shape[-1])))
	model.add(tf.keras.layers.Dropout(0.2))
	model.add(tf.keras.layers.GRU(12,activation="sigmoid"))
	model.add(tf.keras.layers.Dropout(0.2))
	model.add(tf.keras.layers.Dense(units=1))
	model.compile(loss="mean_squared_error",optimizer=tf.keras.optimizers.Adam(lr=0.12))
	model.fit(X,y,epochs=100)
	return model






X=np.array([i for i in range(0,10000)]).reshape(-1,1)
X,y=process(X,30)
g=build_cell(X)
print(g)

