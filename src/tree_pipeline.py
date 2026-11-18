"""PM03: decision tree that recognizes dissatisfied support customers.

Implement every function marked TODO. Keep the function names, parameters, and
return values. You may add helper functions.
"""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

LABEL = "dissatisfied"


def load_cases(path):
    """Read the support cases. Provided: blank labels stay empty strings instead of NaN."""
    return pd.read_csv(path, keep_default_na=False)


def select_responders(cases):
    """Return the cases with a known outcome.

    A case has a known outcome when survey_responded is "Yes".
    """
    return cases[cases["survey_responded"] == "Yes"].copy()



def split_by_date(responders):
    """Divide the responders into three slices by closed_date.

    Training:   2025-01-01 through 2025-08-31
    Validation: 2025-09-01 through 2025-10-31
    Test:       2025-11-01 through 2025-12-31

    Returns (training, validation, test) as three DataFrames.
    """
    dates = pd.to_datetime(responders["closed_date"])

    training   = responders[(dates >= "2025-01-01") & (dates <= "2025-08-31")].copy()
    validation = responders[(dates >= "2025-09-01") & (dates <= "2025-10-31")].copy()
    test       = responders[(dates >= "2025-11-01") & (dates <= "2025-12-31")].copy()

    return training, validation, test


def prepare_features(cases, columns=None):
    """Return the features for a decision tree.

    1. Remove every column that must not be a feature.
    2. Convert text categories to 0/1 columns with pd.get_dummies(..., drop_first=True, dtype=int).
    3. When columns is provided, return exactly those columns, in that order,
       filling a missing column with 0.
    """
    drop_cols = [
        "case_id",
        "closed_date",
        "survey_responded",
        "dissatisfied",
    ]

    features = cases.drop(columns=[col for col in drop_cols if col in cases.columns])

    features = pd.get_dummies(features, drop_first=True, dtype=int)

    if columns is not None:
        features = features.reindex(columns=list(columns), fill_value=0)

    return features


def train_tree(X, y, depth):
    """Create a DecisionTreeClassifier(criterion="gini", max_depth=depth, random_state=0),
    fit the tree to X and y, and return the fitted tree."""

    model = DecisionTreeClassifier(criterion="gini", max_depth=depth, random_state=0)
    model.fit(X, y)
    return model


def compare_depths(X_train, y_train, X_valid, y_valid, depths):
    """Train one tree for each depth in depths and measure each tree.

    Returns a DataFrame with one row per depth and the columns:
    depth, training_accuracy, validation_accuracy
    Round each accuracy to 3 decimal places.
    """
    # TODO
    raise NotImplementedError


def choose_depth(comparison):
    """Return the depth with the highest validation_accuracy.

    When two depths tie, return the smaller depth.
    """
    # TODO
    raise NotImplementedError


def evaluate_model(tree, X, y):
    """Measure the tree on labeled data, treating "Yes" as the positive outcome.

    Returns a one-row DataFrame with the columns:
    true_positives, false_positives, false_negatives, true_negatives,
    accuracy, precision, recall
    Round accuracy, precision, and recall to 3 decimal places.
    """
    # TODO
    raise NotImplementedError


def score_cases(tree, cases, columns):
    """Predict the probability that each case is dissatisfied.

    Returns a DataFrame with the columns case_id and dissatisfied_probability
    (the probability of "Yes", rounded to 3 decimal places), sorted by
    dissatisfied_probability from highest to lowest, then by case_id ascending.
    """
    # TODO
    raise NotImplementedError


def evaluate_business_value(tree, test, columns, calls):
    """Compare the follow-up calls guided by the tree with calls chosen at random.

    dissatisfied_reached_by_tree: the number of dissatisfied customers among the
        top-ranked test cases, where calls is the number of cases called.
    dissatisfied_expected_at_random: calls multiplied by the share of dissatisfied
        customers in the test data, rounded to 1 decimal place.

    Returns a one-row DataFrame with the columns:
    calls, dissatisfied_reached_by_tree, dissatisfied_expected_at_random
    """
    # TODO
    raise NotImplementedError


def extract_rules(tree, columns):
    """Return the rules of the tree as text: export_text with show_weights=True."""
    # TODO
    raise NotImplementedError
