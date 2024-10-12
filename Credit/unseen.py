import numpy as np
import pandas as pd

num_samples = 1000

time = np.random.randint(0, 1, num_samples)
V1 = np.random.normal(loc=0, scale=1, size=num_samples)
V2 = np.random.normal(loc=0, scale=1, size=num_samples)
V3 = np.random.normal(loc=0, scale=1, size=num_samples)
V4 = np.random.normal(loc=0, scale=1, size=num_samples)
V5 = np.random.normal(loc=0, scale=1, size=num_samples)
V6 = np.random.normal(loc=0, scale=1, size=num_samples)
V7 = np.random.normal(loc=0, scale=1, size=num_samples)
V8 = np.random.normal(loc=0, scale=1, size=num_samples)
V9 = np.random.normal(loc=0, scale=1, size=num_samples)
V10 = np.random.normal(loc=0, scale=1, size=num_samples)
V11 = np.random.normal(loc=0, scale=1, size=num_samples)
V12 = np.random.normal(loc=0, scale=1, size=num_samples)
V13 = np.random.normal(loc=0, scale=1, size=num_samples)
V14 = np.random.normal(loc=0, scale=1, size=num_samples)
V15 = np.random.normal(loc=0, scale=1, size=num_samples)
V16 = np.random.normal(loc=0, scale=1, size=num_samples)
V17 = np.random.normal(loc=0, scale=1, size=num_samples)
V18 = np.random.normal(loc=0, scale=1, size=num_samples)
V19 = np.random.normal(loc=0, scale=1, size=num_samples)
V20 = np.random.normal(loc=0, scale=1, size=num_samples)
V21 = np.random.normal(loc=0, scale=1, size=num_samples)
V22 = np.random.normal(loc=0, scale=1, size=num_samples)
V23 = np.random.normal(loc=0, scale=1, size=num_samples)
V24 = np.random.normal(loc=0, scale=1, size=num_samples)
V25 = np.random.normal(loc=0, scale=1, size=num_samples)
V26 = np.random.normal(loc=0, scale=1, size=num_samples)
V27 = np.random.normal(loc=0, scale=1, size=num_samples)
V28 = np.random.normal(loc=0, scale=1, size=num_samples)
amount = np.random.exponential(scale=100, size=num_samples)
class_labels = np.random.randint(0, 2, num_samples)

unseen_data = pd.DataFrame(
    {
        "Time": time,
        "V1": V1,
        "V2": V2,
        "V3": V3,
        "V4": V4,
        "V5": V5,
        "V6": V6,
        "V7": V7,
        "V8": V8,
        "V9": V9,
        "V10": V10,
        "V11": V11,
        "V12": V12,
        "V13": V13,
        "V14": V14,
        "V15": V15,
        "V16": V16,
        "V17": V17,
        "V18": V18,
        "V19": V19,
        "V20": V20,
        "V21": V21,
        "V22": V22,
        "V23": V23,
        "V24": V24,
        "V25": V25,
        "V26": V26,
        "V27": V27,
        "V28": V28,
        "Amount": amount,
        "Class": class_labels,
    }
)

unseen_data.to_csv("synthetic_unseen_credit_data.csv", index=False)
