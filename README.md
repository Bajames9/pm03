# PM03 Starter Package

This package contains the Canopy support case data, a Python application framework, a development notebook, and a packaging utility. The assignment instructions describe the business problem, the requirements, and the grading.

## Contents

```text
pm03_start/
|-- README.md
|-- data/
|   +-- support_cases.csv
|-- src/
|   |-- tree_pipeline.py      <- implement the functions marked TODO
|   +-- main.py               <- provided: runs the complete pipeline
|-- notebooks/
|   +-- pm03_development_notebook.ipynb
+-- tools/
    +-- package_submission.py <- provided: creates pm03_submission.zip
```

## Choose an Environment

Use Colab with Google Drive or Jupyter Lab on your computer.

| | Colab with Google Drive | Jupyter Lab |
|---|---|---|
| Setup | Nothing to install | Install Python, pandas, scikit-learn, and Jupyter Lab |
| Files | Stored in a Google Drive folder; edits are saved | Stored on your computer |
| Editing `.py` files | Colab's built-in file editor | Jupyter Lab's editor or any code editor |
| Teamwork | Share the Drive folder | Share files or use Git |

### Colab Setup

1. Extract `pm03_start.zip` and upload the `pm03_start` folder to **My Drive** in Google Drive.
2. In Google Drive, open `pm03_start/notebooks/pm03_development_notebook.ipynb` with Google Colaboratory.
3. Run the setup cell. Approve the Google Drive connection when Colab asks.
4. To edit `src/tree_pipeline.py`, open the Files panel in Colab, browse to `drive/MyDrive/pm03_start/src`, and double-click the file. Colab saves the file to Drive.

If the folder is not directly under My Drive, change the folder path in the setup cell.

### Jupyter Lab Setup

1. Extract `pm03_start.zip` on your computer.
2. Install the packages once: `pip install pandas scikit-learn jupyterlab`
3. Start Jupyter Lab in the `pm03_start` folder and open `notebooks/pm03_development_notebook.ipynb`.
4. Run the setup cell.

## Implement the Functions

Implement every function marked `TODO` in `src/tree_pipeline.py`. Keep the function names, parameters, and return values. The docstring of each function defines the required behavior, column names, sort order, and rounding. You may add helper functions.

Use the development notebook to test each function as you implement it. The notebook reloads `tree_pipeline.py` automatically, so a saved change takes effect the next time a cell runs.

## Run the Pipeline

Run the complete pipeline from the notebook:

```
!python src/main.py
```

In Jupyter Lab, the same command also works in a terminal opened in the `pm03_start` folder (without the `!`).

`main.py` writes five files to the `output` folder:

| File | Contents |
|---|---|
| `depth_comparison.csv` | Training and validation accuracy for depths 1 through 8 |
| `test_results.csv` | Test results for the chosen tree |
| `business_value.csv` | Dissatisfied customers reached by 100 tree-guided calls versus 100 random calls |
| `follow_up_list.csv` | December cases without a survey response, ranked by probability of dissatisfaction |
| `tree_rules.txt` | The rules of the chosen tree |

Running `main.py` again replaces the outputs.

## Package the Submission

1. Run `main.py` and confirm that all five output files exist.
2. Complete and save the development notebook.
3. Complete the **Team Notes** section at the end of this README.
4. Run `!python tools/package_submission.py` from the notebook.
5. Submit the resulting `pm03_submission.zip`. Do not submit the data file.

## Team Notes

**How the team ran the application:**
group shared it through github
Nathaniel ran it the program on vs code 

**Known limitations or unresolved issues:**
