for one_multiplier in range(1, 11):
    for two_multiplier in range(1, 11):
        print(f"{one_multiplier}{"x"}{two_multiplier}{"="}{one_multiplier*two_multiplier}", end="\t")
    print()