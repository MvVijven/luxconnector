#%%
import os
import time

import cv2

from luxconnector import LuxConnector

result_folder = os.path.join("results", "z_stack")
os.makedirs(result_folder, exist_ok=True)

connector = LuxConnector()

s = time.time()
z_stack = connector.get_z_stack(10, 0, 1)
print(time.time() - s)

for idx, img in enumerate(z_stack):
    cv2.imwrite(os.path.join(result_folder, f"{idx}.png"), img)