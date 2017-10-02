import random
#import sys
#from answer import is_answer, get_mean_score
#from encoding import create_chromosome
#from tools import selection, crossover, mutation

def answer():
    return "merunda17&"

def is_answer(x):
    return x == answer()

def get_gene():
    genes = "abcdefghijklnmopqrstuvwxyz0123456789ABCDEFGHIJKLNMOPQRSTUVWXYZ&!*"
    return random.choice(genes)

def create_chromosome(chrom_size):
    return "".join([get_gene() for x in range(chrom_size)])

def create_population(pop_size, chrom_size):
    population = []
    for i in range(pop_size):
        chrom = create_chromosome(chrom_size)
        population.append(chrom)

    return population

def fit(chrom):
    size = len(chrom)
    score = 0
    for i in range(size):
        if chrom[i] == answer()[i]:
            score += 1

    return score / size

def selection(population):
    BEST = 0.3
    LAZY = 0.2
    size = len(population)

    best_count = int(size * BEST)
    lazy_count = int(size * LAZY)

    population.sort(key= lambda c: fit(c))
    print(population[0])
    best_ones = population[-best_count:]
    lazy_ones = population[:-best_count]

    return best_ones + random.sample(lazy_ones, lazy_count)

def crossover(parent1, parent2):
    half = int(len(parent1)/2)
    return parent1[:half] + parent2[half:]

def mutation(chrom):
    # -1 to avoid index out error if mutating last position
    mutation_index = random.randint(0, len(chrom)-1)
    return chrom[:mutation_index] + get_gene() + chrom[1+mutation_index:]

def generation(population):
    # selection
    select = selection(population)

    # reproduction
    # As long as we need individuals in the new population, fill it with children
    children = []
    while len(children) < len(select):
        ## crossover
        parent1 = random.choice(select)
        parent2 = random.choice(select)
        child = crossover(parent1, parent2)

        ## mutation
        child = mutation(child)
        children.append(child)

    # return the new generation
    return select + children

def algorithm():
    # chrom_size = int(input())
    chrom_size = len(answer())
    population_size = chrom_size * 10

    # create the base population
    generations = 1
    population = create_population(population_size, chrom_size)

    answers = []
    while not answers:
        ## create the next generation
        generations += 1
        population = generation(population)

        ## check if a solution has been found
        for chrom in population:
            if is_answer(chrom):
                answers.append(chrom)

    print("Your password is", answers[0], "after", generations, "generations")

if __name__ == "__main__":
    algorithm()
