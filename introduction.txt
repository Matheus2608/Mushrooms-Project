1 -Read the value of K, an integer.

2 -Read the value of Ntrain, an integer that indicates how many training samples will be given.

3 -Read the value of Ntest, an integer that indicates how many test samples will be given.

4 - Read all Xtrain training vectors, ie read a matrix of Ntrain rows (mushrooms) and D columns (attributes), where each row represents a sample.

5 - In the problem of this project, the data is provided as a sequence of characters separated by space. To use a numeric metric, you must convert these characters to numbers. To do this, use the database of mushrooms features, so that the attribute value listed first is converted to the number 0, the second to 1, and so on. For example, the third attribute of mushrooms (that is, the third column of data) is called cap-color and can take on the following values:

6 -brown='n', buff='b', cinnamon='c', gray='g', green='r', pink='p', purple='u', red='e', white='w', yellow='y'.

7 - Convert the character 'n' to 0, 'b' to 1, 'c' to 2, 'g' to 3 and so on. Do this for all attributes.

8 -Given the coding above, note that each attribute may have a different scale from the other attributes. For example, some attributes can only take 2 values and therefore will take a maximum value of 1, while others can take a value greater than 10. Given the way in which samples are compared, this may unfairly give more value to certain attributes than others, as we do not know what the real relevance of each attribute is. To equal the relevance of attributes, data must be normalized (or standardized). To do so, it is necessary to calculate the vector μ of avarage and the vector σ of standard deviations for all attributes.

9 -Important detail: when calculating the standard deviation, do not use the Bessel correction.

10 -For each attribute, subtract the mean and divide the result by the standard deviation. If an attribute does not vary in the training set (that is, its standard deviation is 0), its value must be set to 0.

11 - Read the Ytrain labels of all training samples, that is, read a vector that contains Ntrain elements, where each line has only one character that indicates the label, which can assume the value 'p' or 'e' (from poisonous/poisonous and edible/edible).

12 -Read all Xtest test vectors, ie read an array of Ntest rows and D columns, where each row represents a mushroom to be sorted.

13 -In the same way as for the training set, normalize the test set data, however, it is important that instead of calculating the avarage and standard deviation again, the same vectors μ and σ calculated shoud be used on training set.

14 -For each test vector, calculate the Euclidean distance between this Xtesti vector and all xtrain training vectors.

16 -For a pair of vectors: a and b, both containing D elements, is calculated the Euclidean distance between them.

18 -Check, among the K closest neighbors of xtesti, if most of them (in the training set) are poisonous ('p') or edible ('e') mushrooms.

19 - Print the label of the majority class obtained in the previous step ('p' or 'e').
