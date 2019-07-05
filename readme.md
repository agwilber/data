# take home project

this project has been designed to see how you think about working with data.

data sources:
1. file `addresses.csv` contains addresses, each associated to a number, called "x".
2. file `properties.json` also contains addresses, each associated with some data, called "y".
3. ["County Business Patterns: 2016"](https://census.gov/data/datasets/2016/econ/cbp/2016-cbp.html) provides some data about zipcodes and states, for instance employment payrolls.

could you create a program which does the following (in no particular order):

1. loads in `addresses.csv`, `properties.json`, and at least one state and one zipcode dataset from ["County Business Patterns: 2016"](https://census.gov/data/datasets/2016/econ/cbp/2016-cbp.html). so, a total of four (4) or more datasets.
2. create a file `results.json` or `results.csv` which contains all the provided addresses, and their associated data. in other words, each address may have a number "x" associated to it, some data "y" associated to it, and also some state- or zip-associated data.

addresses generally contain typographical errors, so matching them may
be a challenge. ideally, but not necessarily, the program you create
could be run by somebody else, or in other words, your result file
`results.json` is created automatically. the minimum completion of
this project is production of `results.json` or `results.csv`, with extra credit being
complete automation, meaning someone else can run your program which
generates the results from scratch.