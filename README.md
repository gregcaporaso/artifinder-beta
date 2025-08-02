# artifinder

A [QIIME 2 Framework (Q2F)](https://qiime2.org) Research Data Management (RDM) tool [developed](https://develop.qiime2.org) by Greg Caporaso (greg.caporaso@nau.edu). 📚

`artifinder` is designed to help you identify [Q2F `Results`](https://use.qiime2.org/en/latest/back-matter/glossary.html#term-result) that are relevant to your analysis from a directory that might contain a mix of relevant and irrelevant `Result` files.
This can be useful when:
 1. you're getting to the end of a complex analysis and need to compile relevant [QIIME 2 `Artifacts`](https://use.qiime2.org/en/latest/back-matter/glossary.html#term-artifact) for inclusion with a manuscript;
 2. you're picking up an analysis that someone left off on, and your struggling to make sense of which files were used for what (and which files have a date with the compost bin);
 3. and probably other applications.

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
[Let me know](https://github.com/gregcaporaso/artifinder/issues) if it's not working for you or if you think have ideas for new functionality.

## Installation instructions

**The following instructions are intended to be a starting point** and should be replaced when `artifinder` is ready to share with others.
They will enable you to install the most recent *development* version of `artifinder`.
Remember that *release* versions should be used for all "real" work (i.e., where you're not testing or prototyping) - if there aren't instructions for installing a release version of this plugin, it is probably not yet intended for use in practice.

1. Get conda installed.
 Lately I've been using [Miniforge](https://github.com/conda-forge/miniforge) for this.

2. [Install a QIIME 2 distribution of your choice](https://library.qiime2.org/quickstart).
 If you're just using artfinder, the `tiny` distro will work great.
 It should work in most [plugin environments](https://library.qiime2.org/plugins) too.
 Activate that environment.

3. Install the dev branch of the repository with the following command:

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

The `artifinder` Python package was [created from a template](https://develop.qiime2.org/en/latest/plugins/tutorials/create-from-template.html).
To learn how to use QIIME 2, refer to the [QIIME 2 User Documentation](https://use.qiime2.org).
To learn QIIME 2 development, refer to [*Developing with QIIME 2*](https://develop.qiime2.org).
