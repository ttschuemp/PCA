import pandas as pd 
import pyodbc
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
from sklearn.decomposition import PCA



def pca_plot_3d(df, features, components = 3):
    '''
    Plots higher dimensional data in 3 dimensions with PCA. Arg2 list of column names of features to be included from the dataframe.
    Components is the number of principal components. Choose 3 or 2.
    '''

    pca = PCA(n_components=3)
    principalComponents = pca.fit_transform(df[features])
    principalDf = pd.DataFrame(data = principalComponents
                               , columns = ['principal component 1', 'principal component 2', 'principal component 3'])
    
    sns.pairplot(principalDf[['principal component 1', 'principal component 2', 'principal component 3']]
    , vars=principalDf[['principal component 1', 'principal component 2', 'principal component 3']])

    # Create the figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Generate the values
    x_vals = principalDf['principal component 1']
    y_vals = principalDf['principal component 2']
    z_vals = principalDf['principal component 3']
    
    
    # Plot the values
    ax.scatter3D(x_vals, y_vals, z_vals, cmap='jet')
    ax.set_xlabel('principal component 1')
    ax.set_ylabel('principal component 2')
    ax.set_zlabel('principal component 3')
    plt.show()



if __name__ == '__main__':
    
    pca_plot_3d(preprocessed_data, feature_list)