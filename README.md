# FP26: Fundamentals of Programming for Digital Health

Course project for *Fundamentals of Programming for Digital Health*
(HPI, WS 2026/27). The project is a Quarto document that renders a short
data analysis, kept in a self-contained git repository.

## Contents

| Path                  | Purpose                                                |
|-----------------------|--------------------------------------------------------|
| `main_file.qmd`       | the Quarto document                                    |
| `functions.py`        | data handling and plotting helpers                     |
| `data/data_small.csv` | small derived data set (tracked)                       |
| `raw_data_large/`     | large raw data (local only, listed in `.gitignore`)    |
| `figures/`            | figures written when the document is rendered          |

## Render

```bash
quarto render
```

Requires [Quarto](https://quarto.org) and Python 3 with `matplotlib`.

The rendered document is written to `main_file.html` and is included in the
repository so it can be read without installing anything.

## Workflow

```bash
git pull            # update from GitHub
quarto render       # rebuild the document
git add -A
git commit -m "..."
git push
```

Author: AmunRaPtah · Course page: <https://brry.github.io/course/>
