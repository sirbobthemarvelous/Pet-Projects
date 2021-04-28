import numpy as np
import sklearn
from sklearn.preprocessing import scale
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
from sklearn import metrics

digits = load_digits()
data = scale(digits.data)
#   scaling features down to between -1 to 1
y = digits.target

k = 10
# k = len(np.unique(y))
# randomly generated
samples, features = data.shape

def bench_k_means(estimator, name, data):
    estimator.fit(data)
    print('%-9s\t%i\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f'
          % (name, estimator.inertia_,
             metrics.homogeneity_score(y, estimator.labels_),
             metrics.completeness_score(y, estimator.labels_),
             metrics.v_measure_score(y, estimator.labels_),
             metrics.adjusted_rand_score(y, estimator.labels_),
             metrics.adjusted_mutual_info_score(y,  estimator.labels_),
             metrics.silhouette_score(data, estimator.labels_,
                                      metric='euclidean')))
# no test, training data distinction, euclidean distance is absolute distance


clifford = KMeans(n_clusters=k, init="random", n_init=10)
# init makes sure the centroids are equidistant from start, n_init decides how many times the centroids are different
# default max iterations of centroid changes is 300, u can make it different
bench_k_means(clifford, "1", data)