# Kendall Tau Point Facet Generator for TSP
import sys
import itertools

n = 3

# generates distinct hamiltonian paths
def paths():
    # list of permutation tuples 
    ham_paths = []
    paths = {}
    for x in itertools.permutations(tuple(range(2,n+1))):
        paths[x] = True
        if x[::-1] not in paths:
            ham_paths.append((1,) + x)
    return ham_paths

# converts hamiltonian paths to binary representation
def ham_paths_to_bins(perms):
    # maps subscript to index location in list 
    subscript_index = {}
    count = 0
    # subscripts 
    for x in itertools.permutations(tuple(range(1,n+1)),2):
        subscript_index[x] = count
        count += 1
    # stores the binary representation lists 
    bin_reps = []
    for perm in perms:
        bin_representation = [0] * len(subscript_index)
        for i in range(len(perm)-1):
            curr_subscript = (perm[i],perm[i+1])
            bin_representation[subscript_index[curr_subscript]] = 1
        bin_representation[subscript_index[(perm[-1],perm[0])]] = 1
        bin_reps.append(bin_representation)
    # print(subscript_index)
    return bin_reps

# convertes binary reperesentation into points 
def gen_points(bin_rep):
    points = []
    z_lst = list(itertools.product([0, 1], repeat=n*(n-1)))
    for x in bin_rep:
        for y in bin_rep:
            for z in z_lst:
                test = True
                for i in range(len(x)):
                    test = test and (x[i]+y[i]-z[i]<=1)
                if test:
                    points.append(x + y + list(z))
    return points

def main():
    ham_paths = paths()
    bin = ham_paths_to_bins(ham_paths)
    points = gen_points(bin)
    # write points to file
    f = open("kt_points%d.poly"%n,"w+")
    f.write("POINTS\n")
    for p in points:
        f.write("1")
        for k in p:
            f.write(" %d"%k)
        f.write("\n")

if __name__ == '__main__':
    main()





# def perm_to_bin(perm):
#     x = []
#     for i in range(len(perm)):
#         for j in range(len(perm)):
#             if(i!=j):
#                 if(perm[i]<perm[j]):
#                     x.append(1)
#                 else:
#                     x.append(0)
#     return x
# # main function
# def main(argv):
#     # size of problem
#     n = int(argv[0])
#     # type of problem
#     t = argv[1]
#     # create points
#     if(t=="p"):
#         # all possible permutations
#         perm = []
#         for x in itertools.permutations(list(range(n))):
#             perm.append(list(x))
#         # all possible 0-1 combos
#         z_lst = list(itertools.product([0, 1], repeat=n*(n-1)))
#         # build all feasible KT points
#         points = []
#         for i in range(len(perm)):
#             x = perm_to_bin(perm[i])
#             for j in range(len(perm)):
#                 y = perm_to_bin(perm[j])
#                 for k in range(len(z_lst)):
#                     z = z_lst[k]
#                     test = True
#                     for l in range(len(z)):
#                         test = test and (x[l]+y[l]-z[l]<=1)
#                     if(test):
#                         row = deepcopy(x)
#                         row.extend(y)
#                         row.extend(z)
#                         points.append(row)
#         print("number of points: %d"%len(points))
#         # write points to file
#         f = open("kt_points%d.poly"%n,"w+")
#         f.write("POINTS\n")
#         for p in points:
#             f.write("1")
#             for k in p:
#                 f.write(" %d"%k)
#             f.write("\n")
#     # create facets
#     elif(t=="f"):
#         print("this is where the facet file writer would go.")
#     # warning
#     else:
#         print("main method is expecting two arguments: n and t, where n is the size of the problem and t is the type of problem: p (points) or f (facets).")
# if __name__ == '__main__':
#     main(sys.argv[1:])