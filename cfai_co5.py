def bayes(
        prior,
        likelihood,
        evidence):

    return (
        prior *
        likelihood
    ) / evidence

prior = 0.5

likelihood = 0.8

evidence = 1

probability = bayes(
    prior,
    likelihood,
    evidence
)

print(
    "Overload Probability =",
    round(probability, 2)
)