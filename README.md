# artifinder 📚: a `rachis` (formerly Q2F) Research Data Management tool

`artifinder` is designed to help you find and identify `[rachis](https://news.rachis.org/en/latest/2025-10-23-q2f-transition.html)` (formerly Q2F) [`Results`](https://use.qiime2.org/en/latest/back-matter/glossary.html#term-result) that are relevant to your analysis from a directory that might contain a mix of relevant and irrelevant `Result` files.
This can be useful when:
 1. you're getting to the end of a complex analysis and need to compile relevant [`Artifacts`](https://use.qiime2.org/en/latest/back-matter/glossary.html#term-artifact) for inclusion with a manuscript; or
 2. you're picking up an analysis that someone left off on, and you're struggling to make sense of which files were used for what (and which files have a date with the compost bin).

For example, given a **target** `Result` (`ss-usage/Serial/hits-table.qzv` in the example that follows) and a search directory (`ss-usage`), `artifinder` provides you with absolute file paths to all of the QIIME 2 `Artifacts` that were used in the creation of the target.
If an `Artifact` that was used is not found in the search path, that information is reported.

```shell
$ artifinder ss-usage/Serial/hits-table.qzv ss-usage

Target `Result` UUID(s):
 * 4e5df73c-a24e-4f02-b0a3-6ad1995fe5a7

Predecessor `Results`:
 * 4e5df73c-a24e-4f02-b0a3-6ad1995fe5a7
  * Visualization
  * /Users/jgc/temp/uq2/ss-usage/Serial/hits-table.qzv
 * 3d410727-d6cc-4d97-bbbf-473954a25e4f
  * FeatureData[Sequence]
  * /Users/jgc/temp/uq2/ss-usage/Serial/query-seqs.qza
 * 572a62ce-8ae4-442e-bfbf-e1e177ea767a
  * FeatureData[Sequence]
  * Result not found in search path.
```

`artifinder` is mostly untested at this point, aside from applications to some local data - it's just a simple utility script, after all.
[Let me know](https://github.com/gregcaporaso/artifinder/issues) if it's not working for you or if you have ideas for new functionality.

## Installation instructions

1. Get conda installed.
 I've most recently been using [Miniforge](https://github.com/conda-forge/miniforge) for this.

2. Activate a 2025.10 or later `[rachis](https://news.rachis.org/en/latest/2025-10-23-q2f-transition.html)` (formerly Q2F) environment of your choice, such as:
 a. an existing Q2F deployment, such as a qiime2 (formerly amplicon) or MOSPHIT installation;
 b. a new deployment you create (e.g., a fresh install of the `tiny` distro following the *quickstart* steps on the [QIIME 2 Library](https://library.qiime2.org/quickstart/tiny) will work great); or
 c. a [plugin environment](https://library.qiime2.org/plugins), such as a [`q2-fmt` installation](https://library.qiime2.org/plugins/qiime2/q2-fmt).

3. Install the dev branch of `artifinder` with the following command:

 ```shell
 pip install https://github.com/gregcaporaso/artifinder/archive/refs/heads/dev.zip
 ```

## Usage

You should then be able to use `artifinder` as follows:

```shell
$ artifinder <target-result> <search-directory>
```

For example:

```shell
$ artifinder hits-table.qzv ss-usage
```

Have fun! 😎

## About

`artifinder` is developed by [Greg Caporaso](https://cap-lab.us). 📚
The `artifinder` Python package was [created from a template](https://develop.qiime2.org/en/stable/plugins/tutorials/create-from-template.html).
Learning resources and more at https://library.qiime2.org.
