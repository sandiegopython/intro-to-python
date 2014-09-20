def cupcake_tally(guests):
    """ Given number of party guests,
        returns how many cupcakes are needed. """
    return 2 * guests + 13

cupcakes = cupcake_tally(30) + cupcake_tally(1)
print("You need {} cupcakes".format(cupcakes))