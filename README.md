# mendel.py: A basic genetics package
mendel.py is a simple system to play with the genetics of inheritance in a very simple and user-friendly manner.

It is written with a functional approach to genetics, with a creature definition being "compiled" to a bunch of functions that operate on "genomes", which are simple strings.

## How to use
`self_test.py` showsa simple example of a creature template, and the 3 functions the `compile_creature()` returns.

In principle, all tests start with a template. The template defines certain traits, that are identified with a allese letter, that is capital for dominant and small for resessive. Support for co-domiance is not added yet.

Templates are dictionaries:
```python3
template = {
    "trait A" : {
        "type": "mendel",
        "letter": "A",
        "dom": "A expresses"
        "res": "A not express"
    }
}
```

The above template tracks a trait A, which has 2 alleles, `A` and `a`.

For a genotype `"Aa"`, the trait expresses will be `"A expresses"`

The `compile_creature` function returns 3 functions:
1) A `express` function: returns a list of expressed traits for a given genotype
2) A `check` fucntion: Checks to see of genotype is valid
3) A `cross` function: Returns all offspring of a cross between 2 genotypes

