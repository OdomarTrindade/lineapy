<div align="center" style="display:flex;flex-direction:column;">
  <a href="https://lineapy.org/">
    <img src="https://user-images.githubusercontent.com/724072/165418570-7338c65b-0fd1-489c-b76a-f03f074f42ca.png" alt="LineaPy" width="500">
  </a>
  <h3>Capture, analyze, and transform messy notebooks into data pipelines
  <br />
  with just two lines of code.</h3>
  <p>
    <a href="https://twitter.com/lineapy_oss">
      <img alt="Follow LineaPy on Twitter!" src="https://img.shields.io/badge/follow-%40lineapy_oss-1DA1F2?logo=twitter">
    </a>
    <a href="https://join.slack.com/t/lineacommunity/shared_invite/zt-18kizfn3b-1Qu_HDT3ahGudnAwoFAw9Q">
      <img alt="Join the LineaPy Slack!" src="https://img.shields.io/badge/slack-@lineapy--community-CF0E5B.svg?logo=slack&logoColor=white&labelColor=3F0E40">
    </a>
  </p>
  <p>
  Ask questions or learn about our workshops on our <a target="_blank" href="https://join.slack.com/t/lineacommunity/shared_invite/zt-18kizfn3b-1Qu_HDT3ahGudnAwoFAw9Q">Slack!</a></p>
</div>

<div align="center" style="display:flex;flex-direction:column;">
    <h3>👇 Try It Out! 👇</h3>
    <div>
        <a href="https://bit.ly/3y5IiSq">
            <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/>
        </a>
    </div>
</div>

<https://user-images.githubusercontent.com/13392380/169427654-487d8d4b-3eda-462a-a96c-51c151f39ab9.mp4>

![Python Versions](https://img.shields.io/badge/Python--versions-3.7%20%7C%203.8%20%7C%203.9-brightgreen)
[![Build](https://github.com/LineaLabs/lineapy/actions/workflows/python-app.yml/badge.svg)](https://github.com/LineaLabs/lineapy/actions/workflows/python-app.yml)
[![Netlify Status](https://api.netlify.com/api/v1/badges/fd4d79de-24d6-4b5b-a525-8e9a48820261/deploy-status)](https://app.netlify.com/sites/lineapy-docs/deploys)
[![License](https://img.shields.io/badge/license-Apache%202-brightgreen.svg?logo=apache)](https://github.com/LineaLabs/lineapy/blob/main/LICENSE.txt)
[![PyPi](https://img.shields.io/pypi/v/lineapy.svg?logo=pypi&logoColor=white)](https://pypi.org/project/lineapy/)

- [What Problems Can LineaPy Solve?](#what-problems-can-lineapy-solve)
  - [Use Case 1: Cleaning Messy Notebooks](#use-case-1-cleaning-messy-notebooks)
  - [Use Case 2: Revisiting Previous Work](#use-case-2-revisiting-previous-work)
  - [Use Case 3: Building Pipelines](#use-case-3-building-pipelines)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Interfaces](#interfaces)
    - [Jupyter and IPython](#jupyter-and-ipython)
    - [CLI](#cli)
  - [Quick Start](#quick-start)
- [Usage Reporting](#usage-reporting)
- [What Next?](#what-next)

## What Problems Can LineaPy Solve?

### Use Case 1: Cleaning Messy Notebooks

When working in a Jupyter notebook day after day, it's easy to write messy code &mdash; You might execute cells out of order, execute the same cell repeatedly, and edit or delete cells until you've acquired good results, especially when generating tables, models, and charts. This highly dynamic and interactive notebook use, however, can introduce some issues. Our colleagues may not be able to reproduce our results by rerunning our notebook, and worse still, we ourselves may forget the steps required to produce our previous results.

One way to avoid this problem is to keep the notebook in sequential order by constantly re-executing
the entire notebook during development. This approach, however, interrupts our natural workflows and stream of
thoughts, decreasing our productivity. Therefore, it is much more common to clean up the notebook after development. This is a time-consuming process that is not immune from the reproducibility issues caused by deleted cells and out-of-order cell executions.

To see how LineaPy can help with messy notebooks, check out [this](https://github.com/LineaLabs/lineapy/blob/v0.2.x/.colab/clean_up_a_messy_notebook/clean_up_a_messy_notebook.ipynb) demo or <a href="https://bit.ly/3SuC4nm"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>.

### Use Case 2: Revisiting Previous Work

Data science is often a team effort where one person's work relies on results from another's. For example, a data scientist building a model may use features engineered by other colleagues. When using results generated by other people, we may encounter data quality issues including missing values, suspicious numbers, and unintelligible variable names. When we encounter these issues, we may need to check how these results came into being in the first place. Often, this means tracing back the code that was used to generate the result in question. In practice, this can be a challenging task because we may not know who produced the result. Even if we know who to ask, that person might not remember where the exact version of the code is stored, or worse, may have overwritten the code without version control. Additionally, the person may no longer be at the organization and may not have handed over the relevant knowledge. In any of these cases, it becomes extremely difficult to identify the root any issues, rendering the result unreliable and even unusable.

To see how LineaPy can help here, check out [this](https://github.com/LineaLabs/lineapy/blob/v0.2.x/.colab/discover_and_trace_past_work/discover_and_trace_past_work.ipynb) demo or <a href="https://bit.ly/3fsA9RL"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>.

### Use Case 3: Building Pipelines

As our notebooks become more mature, we may use them like pipelines. For example, our notebook might process the latest data to update a dashboard, or pre-process data and dump it into the file system for downstream model development. To keep our results up-to-date, we might be expected to re-execute these processes on a regular basis. Running notebooks manually is a brittle process that's prone to errors, so we may want to set up proper pipelines for production. If relevant engineering support is not available, we need to clean up and refactor our notebook code so that it can be used in orchestration systems or job schedulers, such as cron, Apache Airflow, Argo, Kubeflow, DVC, or Ray. Of course, this assumes that we already know how these tools work and how to use them &mdash; If not, we need to spend time learning about them in the first place! All this operational work is time-consuming, and detracts from the time that we can spend on our core duties as a data scientist.

To see how LineaPy can help here, check out [this](https://github.com/LineaLabs/lineapy/blob/v0.2.x/.colab/create_a_simple_pipeline/create_a_simple_pipeline.ipynb) demo or <a href="https://bit.ly/3SJewuO"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>.

## Getting Started

LineaPy is a Python package for capturing, analyzing, and automating data science workflows.
At a high level, LineaPy traces the sequence of code execution to form a comprehensive understanding
of the code and its context. This understanding allows LineaPy to provide a set of tools that help
data scientists bring their work to production more quickly and easily, with just *two lines* of code.

Check this [section](#what-problems-can-lineapy-solve) for types of problems that LineaPy can help to solve.

### Prerequisites

LineaPy runs on `Python>=3.7,<3.11` and `IPython>=7.0.0`. It does not come with a Jupyter installation,
so you will need to [install one](https://jupyter.org/install) for interactive computing.

### Installation

To install LineaPy, run:

```bash
pip install lineapy
```

If you want to run the latest version of LineaPy directly from the source, follow instructions
[here](https://docs.lineapy.org/latest/guides/setup/#installing-lineapy).

LineaPy offers several extras to extend its core capabilities, such as support for PostgreSQL or Amazon S3.
Learn more about these and other installation options [here](https://docs.lineapy.org/latest/guides/setup/#extras).

### Interfaces

#### Jupyter and IPython

To use LineaPy in an interactive computing environment such as Jupyter Notebook/Lab or IPython, load its extension by executing the following command at the top of your session:

```python
%load_ext lineapy
```
Please note:

- You must run this as the first command in a given session. Executing it
in the middle of a session will lead to erroneous behaviors by LineaPy.

- This command loads the extension for the current session only. It does not carry over to different sessions, so you will need to repeat it for each new session.

Alternatively, you can launch the environment with the `lineapy` command, like so:

```bash
lineapy jupyter notebook
```

```bash
lineapy jupyter lab
```

```bash
lineapy ipython
```

This will automatically load the LineaPy extension in the corresponding interactive shell application,
and you will not need to manually load it for every new session.

*NOTE:* If your Jupyter environment has multiple kernels, choose `Python 3 (ipykernel)` which `lineapy`
defaults to.

#### CLI

You can also use LineaPy as a CLI command or runnable Python module. To see available options, run the following commands:

```bash
# LineaPy as a CLI command
lineapy python --help
```

or

```bash
# LineaPy as a runnable Python module
python -m lineapy --help
```

### Quick Start

Once LineaPy is installed and loaded, you are ready to start using the package. Let's look at a simple
example using the [Iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set) to demonstrate
how to use LineaPy to 1) store a variable's history, 2) get its cleaned-up code,
and 3) build an executable pipeline for the variable.

The following development code fits a linear regression model to the Iris dataset:

```python
import lineapy
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load data
url = "https://raw.githubusercontent.com/LineaLabs/lineapy/main/examples/tutorials/data/iris.csv"
df = pd.read_csv(url)

# Map each species to a color
color_map = {"Setosa": "green", "Versicolor": "blue", "Virginica": "red"}
df["variety_color"] = df["variety"].map(color_map)

# Plot petal vs. sepal width by species
df.plot.scatter("petal.width", "sepal.width", c="variety_color")
plt.show()

# Create dummy variables encoding species
df["d_versicolor"] = df["variety"].apply(lambda x: 1 if x == "Versicolor" else 0)
df["d_virginica"] = df["variety"].apply(lambda x: 1 if x == "Virginica" else 0)

# Initiate the model
mod = LinearRegression()

# Fit the model
mod.fit(
    X=df[["petal.width", "d_versicolor", "d_virginica"]],
    y=df["sepal.width"],
)
```

Let's say you're happy with your above code, and you've decided to save the trained model. You can store the model as a LineaPy [artifact](https://docs.lineapy.org/latest/concepts/artifact/) with the following code:

```python
# Save the model as an artifact
lineapy.save(mod, "iris_model")
```

A LineaPy artifact encapsulates both the value *and* code, so you can easily retrieve
the model's code, like so:

```python
# Retrieve the model artifact
artifact = lineapy.get("iris_model")

# Check code for the model artifact
print(artifact.get_code())
```

The print statement will output:

```
import pandas as pd
from sklearn.linear_model import LinearRegression

url = "https://raw.githubusercontent.com/LineaLabs/lineapy/main/examples/tutorials/data/iris.csv"
df = pd.read_csv(url)
color_map = {"Setosa": "green", "Versicolor": "blue", "Virginica": "red"}
df["variety_color"] = df["variety"].map(color_map)
df["d_versicolor"] = df["variety"].apply(lambda x: 1 if x == "Versicolor" else 0)
df["d_virginica"] = df["variety"].apply(lambda x: 1 if x == "Virginica" else 0)
mod = LinearRegression()
mod.fit(
    X=df[["petal.width", "d_versicolor", "d_virginica"]],
    y=df["sepal.width"],
)
```

Note that these are the minimal essential steps to produce the model. That is, LineaPy has automatically
cleaned up the original code by removing extraneous operations that do not affect the model (e.g., plotting).

Let's say you're asked to retrain the model on a regular basis to account for any updates in the source data.
You need to set up a pipeline to train the model &mdash; LineaPy makes this as simple as a single function call:

```python
lineapy.to_pipeline(
    artifacts=["iris_model"],
    input_parameters=["url"],  # Specify variable(s) to parametrize
    pipeline_name="iris_model_pipeline",
    output_dir="output/",
    framework="AIRFLOW",
)
```

This command generates several files that can be used to execute the pipeline from the UI or CLI. (Check this
[tutorial](https://docs.lineapy.org/latest/tutorials/02_pipeline_building/) for more details.)

In short, LineaPy automates time-consuming, manual steps in a data science workflow, helping us get
our work to production more quickly and easily.

## Usage Reporting

LineaPy collects anonymous usage data that helps our team to improve the product.
Only LineaPy's API calls and CLI commands are being reported.
We strip out as much potentially sensitive information as possible, and we will
never collect user code, data, variable names, or stack traces.

You can opt-out of usage tracking by setting environment variable:

```bash
export LINEAPY_DO_NOT_TRACK=true
```

## What Next?

To learn more about LineaPy, please check out the project [documentation](https://docs.lineapy.org/latest/)
which contains many examples you can follow with. Some key resources include:

| Resource            | Description                                                                              |
| ------------------- | ---------------------------------------------------------------------------------------- |
| **[Docs]**          | This is our knowledge hub &mdash; when in doubt, start here!                             |
| **[Concepts]**      | Learn about key concepts underlying LineaPy!                                             |
| **[Tutorials]**     | These notebook tutorials will help you better understand core functionalities of LineaPy |
| **[Use Cases]**     | These domain examples illustrate how LineaPy can help in real-world applications         |
| **[API Reference]** | Need more technical details? This reference may help!                                    |
| **[Contribute]**    | Want to contribute? These instructions will help you get set up!                         |
| **[Slack]**         | Have questions or issues unresolved? Join our community and ask away!                    |

[Docs]: https://docs.lineapy.org/latest/
[Concepts]: https://docs.lineapy.org/latest/concepts/artifact/
[Tutorials]: https://github.com/LineaLabs/lineapy/tree/main/examples/tutorials
[Use Cases]: https://github.com/LineaLabs/lineapy/tree/main/examples/use_cases
[API Reference]: https://docs.lineapy.org/latest/reference/lineapy/
[Contribute]: https://docs.lineapy.org/latest/guides/contributing/process/
[Slack]: https://join.slack.com/t/lineacommunity/shared_invite/zt-18kizfn3b-1Qu_HDT3ahGudnAwoFAw9Q
