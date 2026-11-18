"""Run the PM03 pipeline and write the outputs. Provided: do not change the processing logic."""
from pathlib import Path

import tree_pipeline as tp

PROJECT = Path(__file__).resolve().parent.parent
DATA = PROJECT / "data" / "support_cases.csv"
OUT = PROJECT / "output"
DEPTHS = range(1, 9)
CALLS = 100


def main():
    OUT.mkdir(exist_ok=True)
    cases = tp.load_cases(DATA)
    training, validation, test = tp.split_by_date(tp.select_responders(cases))

    X_train = tp.prepare_features(training)
    X_valid = tp.prepare_features(validation, X_train.columns)
    X_test = tp.prepare_features(test, X_train.columns)
    y_train, y_valid, y_test = training[tp.LABEL], validation[tp.LABEL], test[tp.LABEL]

    comparison = tp.compare_depths(X_train, y_train, X_valid, y_valid, DEPTHS)
    depth = tp.choose_depth(comparison)
    tree = tp.train_tree(X_train, y_train, depth)

    december = cases[(cases["survey_responded"] == "No") & (cases["closed_date"] >= "2025-12-01")]

    comparison.to_csv(OUT / "depth_comparison.csv", index=False)
    tp.evaluate_model(tree, X_test, y_test).to_csv(OUT / "test_results.csv", index=False)
    tp.evaluate_business_value(tree, test, X_train.columns, CALLS).to_csv(OUT / "business_value.csv", index=False)
    tp.score_cases(tree, december, X_train.columns).to_csv(OUT / "follow_up_list.csv", index=False)
    (OUT / "tree_rules.txt").write_text(tp.extract_rules(tree, X_train.columns))

    print("Training / validation / test cases:", len(training), "/", len(validation), "/", len(test))
    print("Chosen depth:", depth)
    print("Outputs written to:", OUT)


if __name__ == "__main__":
    main()
