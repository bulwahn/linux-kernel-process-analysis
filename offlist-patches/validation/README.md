
We use pasta to identify off-list patches. Pasta returns a set of commits, for
which the tool concludes that they are off-list patches. Then, we manually
assess the result returned by pasta. The motivation for our manual assessment
is to:
  
  - understand the quality of the Linux kernel development process,
  - evaluate and improve the quality of pasta's matching algorithm, and
  - create a complete data collection of all public emails around the Linux
    kernel development for further process analysis

With this assessment, we determine:

  - if the identified commits are actually off-list patches, that pasta has
    correctly identified, or
  - if the identified commits are not matched due to the matching algorithm,
  - if the identified commits are not matched due to missing data sources or
    insufficient data collection

In this directory here, we store our manual assessment in the following
directory structure and file format.

Each manual assessment of a single git commit reported by pasta is put
into a single file:

  _`<git range>/<git sha>`_


where _`<git range>`_ is the range of the two closest tags for that commit,
e.g., for a commit that was included with v5.0-rc2, the range is
v5.0-rc1..v5.0-rc2,
and `<git sha>` is the 40-character hex sha of the commit in torvalds' tree.

The files are simple loosely structured text files and the following format:

```
<git sha> <commit message header>
ASSESSMENT: (OFF-LIST PATCH | NOT MATCHED | NOT IN DATASET | REVERT | INLINE PATCH | RELEASE COMMIT | UNCLEAR)
MESSAGE-ID: [optional, reasonable when NOT MATCHED or NOT IN DATASET]
DETAILS:
CONFIDENCE: [optional]
TODO:
  - (CONFIRMATION MAIL | PASTA | PATCH INVESTIGATION | OTHER):
```

In these files, commits are referred to in this format:

  `Git commit Hash ("git commit message header")`

and messages are referred to in this format:

  `<Message-ID> ("Email Subject Line")`
