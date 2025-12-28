# artifinder 📚: a `rachis` (formerly Q2F) Research Data Management tool

`artifinder` is designed to help you find and identify `[rachis](https://news.rachis.org/en/latest/2025-10-23-q2f-transition.html)` (formerly Q2F) [`Results`](https://use.qiime2.org/en/latest/back-matter/glossary.html#term-result) that are relevant to your analysis from a directory that might contain a mix of relevant and irrelevant `Result` files.
This can be useful when:
 1. you're getting to the end of a complex analysis and need to compile relevant [`Artifacts`](https://use.qiime2.org/en/latest/back-matter/glossary.html#term-artifact) for archival; or
 2. you're picking up an analysis that someone left off on, and you're struggling to make sense of which files were used for what; or
 3. you're picking up an analysis that you left off on a while ago, and you're can't remember what is what.

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

After installing, you can use `artifinder` as follows:

```shell
$ artifinder <target-result> <search-directory>
```

As an example, imagine you downloaded the full ["gut-to-soil" dataset](https://doi.org/10.1093/ismeco/ycaf089) from [its artifact repository on Zenodo](https://zenodo.org/records/15390940).
You've been looking at [the top-level unweighted UniFrac Emperor plot](https://view.qiime2.org/visualization/?src=https://zenodo.org/api/records/13887457/files/unweighted_unifrac.qzv/content), and would like to build a variation on it.
For example, maybe you want to exclude some samples from the unifrac distance matrix that it is derived from, and then recompute PCoA to generate a new plot.
To do this, you want to know exactly which unweighted UniFrac distance matrix it was created from, so you're certain that you're starting with the right file.

If you want to follow along, you can download the data and do so - but be aware that **this is a 15GB file, so you may just want to read** and then try it out on your own data.

```shell
wget -O gut-to-soil-qiime2.zip \
 https://zenodo.org/records/15390940/files/gut-to-soil-qiime2.zip?download=1
```

```shell
artifinder top-level-qzvs/unweighted_unifrac.qzv combined/

Target `Result` UUID(s):
 * 553580f7-0fb8-4101-a4a1-b93781ec4658 (/Users/jgcap/temp/g2s-download/gut-to-soil-qiime2/top-level-qzvs/unweighted_unifrac.qzv)

Predecessor `Results`:
 * 553580f7-0fb8-4101-a4a1-b93781ec4658
  * Visualization
  * /Users/jgcap/temp/g2s-download/gut-to-soil-qiime2/combined/rarefaction-based-diversity/emperor-plots/unweighted_unifrac.qzv
 * 1cf47da5-1538-4151-bc3a-f7c1af0cf424
  * EMPPairedEndSequences
  * Result not found in search path.
 * 2db99c5c-4899-46e5-b19a-ddce6ac40c3e
  * EMPPairedEndSequences
  * Result not found in search path.
 * 4afd1f08-72e8-4bbf-a73a-8c2bccb0b69f
  * FeatureData[Sequence]
  * Result not found in search path.
 * 8162ad56-eb06-43d7-a52c-a96997d3098e
  * FeatureData[Sequence]
  * Result not found in search path.
 * 419d5c8a-253a-4cd5-83e8-61e1b276afc8
  * TaxonomicClassifier
  * Result not found in search path.
 * da396632-c2d8-4c1e-9237-e46f1a2f0c30
  * SampleData[PairedEndSequencesWithQuality]
  * Result not found in search path.
 * e2bcbaf0-7c5c-4aa1-924e-53163d844265
  * FeatureTable[Frequency]
  * Result not found in search path.
 * 6764be53-7936-431e-8cbc-5c293ad1f102
  * FeatureData[Sequence]
  * Result not found in search path.
 * 74a9e284-768c-4b0c-b2a1-d524885584bf
  * FeatureData[Sequence]
  * Result not found in search path.
 * 91a354b4-a7b0-43ca-9ad6-96857ae631e3
  * FeatureTable[Frequency]
  * Result not found in search path.
 * e327c08d-faed-4c0b-bd97-07fdbea3d438
  * PCoAResults
  * /Users/jgcap/temp/g2s-download/gut-to-soil-qiime2/combined/rarefaction-based-diversity/pcoa-matrices/unweighted_unifrac.qza
 * f971ac95-9756-4e6f-b9b4-4a90740ad59a
  * FeatureTable[Frequency]
  * Result not found in search path.
 * 7fb9bcf8-8dab-4d36-879b-45cbe4f1b8ca
  * FeatureData[Sequence]
  * Result not found in search path.
 * 85d9d87e-361f-4a92-87da-a43845da2c14
  * EMPPairedEndSequences
  * Result not found in search path.
 * e80b5598-5432-4ac5-ba85-e46360065d64
  * SampleData[PairedEndSequencesWithQuality]
  * Result not found in search path.
 * 3df45781-511d-4722-9773-cb1b546b59cc
  * SampleData[PairedEndSequencesWithQuality]
  * Result not found in search path.
 * f8c447e0-75e1-4fc1-b984-637fcb726a57
  * SampleData[PairedEndSequencesWithQuality]
  * Result not found in search path.
 * d775572a-79be-461f-95c1-586d5b1b6b13
  * FeatureData[Sequence]
  * Result not found in search path.
 * b92a2676-3786-494c-9661-5edbf0934f42
  * FeatureData[Sequence]
  * Result not found in search path.
 * 745163cf-18b1-42e3-8a55-5a3acf569b5a
  * FeatureData[Sequence]
  * Result not found in search path.
 * dcd66f24-4f16-49a3-a679-cfe02ae81afd
  * FeatureTable[Frequency]
  * Result not found in search path.
 * 47094f5d-fdb7-4b1e-9e71-233531c95deb
  * EMPPairedEndSequences
  * Result not found in search path.
 * 9884b8bc-a061-42a3-a476-0646f17edf00
  * FeatureTable[Frequency]
  * Result not found in search path.
 * 313811fe-08ad-4689-9117-971199f3ddef
  * SampleData[PairedEndSequencesWithQuality]
  * Result not found in search path.
 * 3bfdf3fb-a031-4089-8be6-304c75c2b461
  * FeatureData[Sequence]
  * Result not found in search path.
 * f3bbdad4-6274-431f-a56a-bfcbc8330a8b
  * FeatureData[Sequence]
  * Result not found in search path.
 * 19fd8247-6c24-4e82-9753-c27ffcd7fb4d
  * FeatureData[Taxonomy]
  * Result not found in search path.
 * d90937f7-edaa-423d-858a-58c88cac53f9
  * FeatureTable[Frequency]
  * Result not found in search path.
 * 4437b72f-b113-4809-b521-e9a1e0bc478a
  * FeatureTable[Frequency]
  * Result not found in search path.
 * dfdf1cf7-20b3-465d-aa91-ca0613ca7729
  * FeatureData[Taxonomy]
  * /Users/jgcap/temp/g2s-download/gut-to-soil-qiime2/combined/taxonomic-annotations/gtdb-r214.1-weighted-stool-taxonomy.qza
 * 62e9def0-3461-436a-a101-c0fefba658a8
  * FeatureData[Sequence]
  * Result not found in search path.
 * b997d6da-ea6d-4d8f-b766-d5098534555e
  * FeatureTable[Frequency]
  * Result not found in search path.
 * 5b90b946-9ddb-4315-9c8f-83623cbda0b2
  * EMPPairedEndSequences
  * Result not found in search path.
 * cd182b04-46a0-4467-9974-84f7784060e1
  * FeatureTable[Frequency]
  * Result not found in search path.
 * abd3b941-3c43-4107-8b20-128845f18a07
  * FeatureTable[Frequency]
  * Result not found in search path.
 * 35009e42-86ca-4b92-926b-f3f561d1249f
  * EMPPairedEndSequences
  * Result not found in search path.
 * efa37f5b-0dfb-4939-bbd4-8be3b38c3eeb
  * SampleData[PairedEndSequencesWithQuality]
  * Result not found in search path.
 * f6ee7ac9-99b1-4dc5-a710-0a34171a9c27
  * FeatureTable[RelativeFrequency]
  * Result not found in search path.
 * e07cd30e-a83c-4520-9092-02ab199a59ef
  * FeatureTable[Frequency]
  * Result not found in search path.
 * 89e06f0b-3471-454c-9ba6-7f56c0841bbd
  * FeatureTable[Frequency]
  * Result not found in search path.
 * 43514fc4-48e9-40b4-a5f3-4e530a4aaddb
  * SampleData[PairedEndSequencesWithQuality]
  * Result not found in search path.
 * 03133bb2-10a3-42ab-b6db-5421e26f10a3
  * FeatureTable[Frequency]
  * Result not found in search path.
 * 595d26ab-f0f0-44a0-a74e-94a88f7f858e
  * FeatureData[Sequence]
  * /Users/jgcap/temp/g2s-download/gut-to-soil-qiime2/combined/asv-seqs.qza
 * ecb63807-e5b7-41bd-9f3d-f0bbbd5d4572
  * Phylogeny[Rooted]
  * /Users/jgcap/temp/g2s-download/gut-to-soil-qiime2/combined/rooted-tree.qza
 * dc57a837-7658-4f13-8edf-eb2f8063497a
  * FeatureTable[Frequency]
  * Result not found in search path.
 * fd7dd96b-c401-4b17-95e5-8dcf34f1573f
  * FeatureData[Sequence]
  * Result not found in search path.
 * 00d23d5b-20a1-4170-8619-89e5d3a679b4
  * FeatureTable[Frequency]
  * Result not found in search path.
 * 4bc12a54-a6db-480d-97bc-ed00face3c63
  * SampleData[PairedEndSequencesWithQuality]
  * Result not found in search path.
 * 2b5b1192-8817-4ef2-9c81-292a6c58fe72
  * SampleData[PairedEndSequencesWithQuality]
  * Result not found in search path.
 * f3a548a2-0c95-44b0-b5e2-1ad3c29d55ef
  * FeatureTable[Frequency]
  * /Users/jgcap/temp/g2s-download/gut-to-soil-qiime2/combined/asv-table.qza
 * 0ecd2151-a54b-4e2c-96b2-226e41a2a50b
  * FeatureData[Sequence]
  * Result not found in search path.
 * 7fca1ee9-b6f3-43e8-9ca0-2f78c8bfc248
  * FeatureData[Sequence]
  * Result not found in search path.
 * 08f3a02c-e2ff-4651-bf53-eda40beab872
  * FeatureTable[Frequency]
  * Result not found in search path.
 * 548ec3f4-3d90-4eb7-810e-2ee8d6eb52bf
  * EMPPairedEndSequences
  * Result not found in search path.
 * 9cbcb60d-bac5-487a-8f48-56a79ee82851
  * FeatureTable[Frequency]
  * Result not found in search path.
 * 44f0f4ff-c425-474f-ad60-681693687044
  * FeatureTable[Frequency]
  * Result not found in search path.
 * f522eb7d-412f-4dc7-a6ad-d267f7e308a4
  * FeatureTable[Frequency]
  * Result not found in search path.
 * 301a6791-eaac-41e5-ab38-ba257b91ef5f
  * SampleData[PairedEndSequencesWithQuality]
  * Result not found in search path.
 * 716fb24d-0077-435d-a3d1-f349f6d98312
  * FeatureData[Sequence]
  * Result not found in search path.
 * 7a4309ce-f8ce-4f25-8b42-84d0294524c7
  * FeatureTable[Frequency]
  * Result not found in search path.
 * 1bb2e87f-9fba-4f0e-acd1-11e12d66b1cc
  * FeatureData[Taxonomy]
  * Result not found in search path.
 * 1ae3f1ba-6106-4063-a482-563183b079ee
  * SampleData[PairedEndSequencesWithQuality]
  * Result not found in search path.
 * c2e1f374-fa37-4ca4-9a7b-29bca6e6a359
  * FeatureTable[Frequency]
  * Result not found in search path.
 * 84fcf26d-3259-4886-bf0f-9718c393dff7
  * FeatureTable[Frequency]
  * Result not found in search path.
 * 771f54ec-fca4-45f0-b5f5-ad1cc0b03599
  * TaxonomicClassifier
  * Result not found in search path.

---
Run with `artifinder` version: 0.0.1+3.g4829966
```

Have fun! 😎

## About

`artifinder` is developed by [Greg Caporaso](https://cap-lab.us). 📚
The `artifinder` Python package was [created from a template](https://develop.qiime2.org/en/stable/plugins/tutorials/create-from-template.html).
Learning resources and more at https://library.qiime2.org.
