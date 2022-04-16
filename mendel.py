import typing

# mendel.py: a basic genetics package, with 
# very fucntional-first principles

def get_gametes(genotype: str) -> list:
    '''
        Return all possible gametes of a givin genotype. 
        Independant of all variations in genotype size.
        Reurns a list
    '''
    genes = [genotype[i:i+2] for i in range(0, len(genotype), 2)]

    gametes = []

    for i in range(0, len(genes)**2):
        gam = ""
        for j in range(0, len(genes)):
            gene = genes[j]
            gam += gene[(2**j & i) >> j]    
        gametes.append(gam)
    
    return gametes


def cross_gametes(m_gamete: str, f_gamete: str) -> str:
    '''
    a FUNCTION THAT TAKES in 2 gamete strings, and returns cross.
    Example: "xYz" cross "XYz" => "xXYYzz"
    '''
    cross = ""

    for m, f in zip(m_gamete, f_gamete):
        cross += m+f

    return cross
         

def compile_creature(template: dict) -> tuple:
    '''
        Takes a ccrature template, and return a few functions

        1) express() - Finds the phenotype given a genotype.
        2) check() - Checks to see is a given genotype is valid [WIP]
        3) cross() - Return all cross offspring of a given pair

    '''
    # Extract keys from template, creating a list of traits    
    traits = list(template.keys())
    alleles = []
    for trait in traits:
        if(template[trait]["type"] == "mendel"):
            alleles.append(template[trait]["letter"])
    # We now have a list "alleles", that holds the matching letters
    # for each trait

    # This function expects a string containig the genotype, in letter form
    # it uses this to find the phenotype traits, based of Dominace and resessive
    
    def express(genotype: str) -> list:
        # Extracts allele pairs from string, each pair is a "gene", 
        # For example, "Hh", or "YY" 
        genes = [genotype[i:i+2] for i in range(0, len(genotype), 2)] 
        if(len(genes) > len(alleles)):
            return -1
        else:
            phenotype = []
            for gene, i in zip(genes, range(0, len(genes))):
                if(True in [c.isupper() for c in gene]): # Chcks if ANY letter in gene is capital
                    phenotype.append(template[traits[i]]["dom"])
                else:
                    phenotype.append(template[traits[i]]["res"])
            return phenotype
    
    
    # This function checks if the given genotype is a valid
    # for the creature
    def check(genotype):
        # Extracts genes
        valid = True
        for l in genotype:
            if l not in alleles:
                valid = False
        return valid

    def cross(mother, father):
        m_gamtes = get_gametes(mother)
        f_gametes = get_gametes(father)
        offspring = []
        for m, f in zip(m_gamtes, f_gametes):
            offspring.append(cross_gametes(m, f))
        return offspring

    return express ,check, cross
                   

        


if __name__ == "__main__":
    print("mendel.py loaded!")
