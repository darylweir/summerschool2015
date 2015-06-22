import numpy as np

prefix = ['Simon_Two_Thumbs/simon_twothumbs-0-','Hugues 2thumbs/h-0-','Markus-myphone/markus-0-', 'Hannah/hannah-0-','Chris_thumbs/chrisagain-0-','Data_Daryl_Two_Thumbs/dwls-0-','Katrin/kathrin-0-','Rebecca/rebeccathumbs-0-']

users = []
for pref in prefix:
   fname = '/Users/wa.weird1/Dropbox/2DGP/logs_noacc/' + pref + 'n9-0.log'
   with open(fname,'r') as f:
      pos = np.loadtxt(f,delimiter=',')

   fname = '/Users/wa.weird1/Dropbox/2DGP/logs_noacc/' + pref + 'true-0.log'
   with open(fname,'r') as f:
      target = np.loadtxt(f,delimiter=',')

   pos[:,0] = pos[:,0]/480 - 0.5
   pos[:,1] = pos[:,1]/854 - 0.5

   target[:,0] = target[:,0]/480 - 0.5
   target[:,1] = target[:,1]/854 - 0.5

   s = np.sum((pos-target)**2,1)
   ind = s < 0.01
   pos = pos[ind,:]

   target = target[ind,:]

   user = {}
   user['pos'] = pos
   user['target'] = target

   users.append(user)

import pickle
with open('touchdata.obj','w') as f:
   pickle.dump(users,f) 

