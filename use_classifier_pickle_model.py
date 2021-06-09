import pickle
import numpy as np
local_classifier=pickle.load(open('classifier.pickle','rb'))
new_predict=local_classifier.predict(np.array([[3., 3., 0., 1., 0., 3.]]))

