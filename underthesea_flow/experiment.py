from numpy import mean
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import accuracy_score, f1_score, make_scorer
from sklearn.preprocessing import MultiLabelBinarizer
import time

from underthesea_flow.validation.validation import TrainTestSplitValidation, \
    CrossValidation

def _flat(l):
    """
    :type l: list of list
    """
    return [item for sublist in l for item in sublist]

class Experiment:
    def __init__(self, X, y, estimator, scores, validation=None):
        self.estimator = estimator
        self.X = X
        self.y = y
        self.scores = scores
        self.validation = validation

    def run(self):

        start = time.time()

        # def score_func(y_true, y_pred, **kwargs):
        #     accuracy_scores.append(accuracy_score(y_true, y_pred, **kwargs))
        #     f1_scores.append(
        #         f1_score(y_true, y_pred, average='micro', **kwargs))

        try:
            # scorer = make_scorer(score_func)
            if isinstance(self.validation, TrainTestSplitValidation):
                X_train, X_test, y_train, y_test = train_test_split(self.X,
                                                                    self.y,
                                                                    test_size=self.validation.test_size)
                self.estimator.fit(X_train, y_train)
                y_pred = self.estimator.predict(X_test)
                y_pred = _flat(y_pred)
                y_test = _flat(y_test)
                print("Accuracy :", accuracy_score(y_test, y_pred))
                print("F1 (micro) :", f1_score(y_test, y_pred, average='micro'))
                print("F1 (macro) :", f1_score(y_test, y_pred, average='macro'))
                print("F1 (weighted):", f1_score(y_test, y_pred, average='weighted'))
                # score_func(Y_test, Y_pred)
            # elif isinstance(self.validation, CrossValidation):
            #     cross_val_score(self.clf, self.X.toarray(), self.Y,
            #                     cv=self.validation.cv, scoring=scorer)
            # f1 = mean(f1_scores)
            # accuracy = mean(accuracy_scores)
            # print("")
            # print("F1: {:.4f}".format(f1))
            # print(f1_scores)
            # print("Accuracy: {:.4f}".format(accuracy))
            # print(accuracy_scores)
            end = time.time()
            train_time = end - start
            print("Running Time: {:.2f} seconds.".format(train_time))
            time_result = {
                "train": train_time
            }
        except Exception as e:
            raise (e)
            print("Error:", e)
            # f1 = 0
            # accuracy = 0
        return time_result

    def save_model(self, filename=None):
        self.estimator.fit(self.X, self.y, filename=filename)
