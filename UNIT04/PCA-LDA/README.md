## Dimensionality reduction

##### where: https://courses.thinkful.com/data-001v2/assignment/4.7.2

Performed tasks:

1. For Principal Component Analysis (PCA)
    - Perform PCA in the Iris dataset
    - Plot the PCA sample. How does it compare to the  original plot?
    - Train the k-nearest neighbors algorithm on the decomposed dataset.

2. For Linear Discriminant Analysis (LDA)
    - Perform LDA in the Iris dataset
    - Plot the LDA sample. How does it compare to the  original plot?
    - Retrain the k-means algorithm from Lesson 4 on the decomposed dataset.
    - Compare the performance on the decomposed dataset to the performance on the raw dataset. Does anything stand out? Did you get the same class prediction?

Comments:

1. PCA
    - For original data set kNN classify always correctely for k=1:19 expecting if we change the metric distance method
    - For decomposed data set the best results is obtained with k =3

2. LDA
    - If we compare the k-means clustered original data with the k-means clusterd LDA decomposed the class 2 and 3 (versicolor and virginica) are switched.
