#plotData

#PCA_FullTstat.py


from sklearn import cluster, datasets
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import os
from sklearn import preprocessing



from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA, IncrementalPCA


label_file = os.path.join("../resultsc.csv")



#results2.csv")
#cleanDataPCATest.csv")

#raw_data={'Average rtt C2S', 'Average rtt S2C','target'}
#df=pd.DataFrame(raw_data, columns = ['Sent','Received','Lost','Duplicated','Reordered'])

df=pd.read_csv(label_file)


# load dataset into Pandas DataFrame
#df = pd.read_csv(label_file, names=['Average rtt C2S','rtt min',
#	'rtt max','max seg size','min seg size','win max','win min','cwin max',
#	'cwin min','initial cwin','rtx RTO','rtx FR','reordering','unnece rtx RTO','target'])

df = pd.read_csv(label_file, names=['Xvalue', 'Yvalue','target'])

print("*******")
#print df

#extracting features
features = ['Xvalue', 'Yvalue']


targets = ['Normal', 'NoFlow', 'Loss1%','Loss5%', 'pDup1%', 'pDup5%','reord25-50%','reord50-50%']


colors = ['g', 'r', 'b', 'black', 'lime', 'yellow', 'cyan', 'coral']

# Separating out the features
x = df.loc[:, features].values
# Separating out the target
y = df.loc[:,['target']].values
print(y)
# Standardizing the features
x = StandardScaler().fit_transform(x)


pd.set_option('display.max_columns', None)




pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['component 1', 'component 2'])

finalDf = pd.concat([principalDf, df[['target']]], axis = 1)

#printing feature values


#plot PCA

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
#ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('x component', fontsize = 10)
ax.set_ylabel('y component', fontsize = 10)

#ax.set_title('2 component PCA', fontsize = 15)
#targets = ['-1', '1']


#colors = ['r', 'g']
for target, color in zip(targets,colors):
	indicesToKeep = finalDf['target'] == target
	ax.scatter(finalDf.loc[indicesToKeep, 'component 1']
		, finalDf.loc[indicesToKeep, 'component 2']
		, c = color
		, s = 50)
ax.legend(targets)
ax.grid()
plt.show()

print("explained_variance_")
print(pca.explained_variance_)  
print("singular values")
print(pca.singular_values_) 

print("variance ratio")
print(pca.explained_variance_ratio_)

print("mean")
print(pca.mean_)



#print "PCA has been conducted, with 2 component as a parameter and we fit the data"

#print "now view the new features, number of rows and 2 features" 
print(principalComponents.shape)

#print "new feature data"
print(principalComponents)

#print "columns"
intermediary=pd.DataFrame(pca.components_, columns=list(features)).values
print(intermediary.reshape(2,26).tolist())


# n_components = 2
# ipca = IncrementalPCA(n_components=n_components, batch_size=10)
# X_ipca = ipca.fit_transform(x)

# pca = PCA(n_components=n_components)
# X_pca = pca.fit_transform(x)

# colors = ['r', 'g', 'b', 'black', 'lime', 'yellow', 'cyan', 'coral']

# for X_transformed, title in [(X_ipca, "Incremental PCA"), (X_pca, "PCA")]:
#     plt.figure(figsize=(8, 8))
#     for color, i, target_name in zip(colors, [0, 1], targets):
#         plt.scatter(X_transformed[y == i, 0], X_transformed[y == i, 1],
#                     color=color, lw=2, label=target_name)

#     if "Incremental" in title:
#         err = np.abs(np.abs(X_pca) - np.abs(X_ipca)).mean()
#         plt.title(title + " of tstat dataset\nMean absolute unsigned error "
#                   "%.6f" % err)
#     else:
#         plt.title(title + " of tstat dataset")
#     plt.legend(loc="best", shadow=False, scatterpoints=1)
#     plt.axis([-4, 4, -1.5, 1.5])

# plt.show()
n_samples = x.shape[0]
# We center the data and compute the sample covariance matrix.
x -= np.mean(x, axis=0)
cov_matrix = np.dot(x.T, x) / n_samples
for eigenvector in pca.components_:
    print(np.dot(eigenvector.T, np.dot(cov_matrix, eigenvector)))




