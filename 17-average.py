import statistics

print("Average is ",statistics.mean([100,95]))

print("median of 100,95,90 is ", statistics.median([100,95,90]))

print("mode of 100,95,90,95 is ", statistics.mode([100,95,90,95]))

print("standard deviation of 100,95,90 is ", statistics.stdev([100,95,90]))

print("variance of 100,95,90 is ", statistics.variance([100,95,90]))

print("harmonic mean of 100,95,90 is ", statistics.harmonic_mean([100,95,90]))

print("geometric mean of 100,95,90 is ", statistics.geometric_mean([100,95,90]))

print("multimode of 100,95,90,95,90 is ", statistics.multimode([100,95,90,95,90]))

print("quantiles of 100,95,90 is ", statistics.quantiles([100,95,90], n=4))

print("pstdev of 100,95,90 is ", statistics.pstdev([100,95,90]))

print("pvariance of 100,95,90 is ", statistics.pvariance([100,95,90]))

print("fmean of 100,95,90 is ", statistics.fmean([100,95,90]))

print("geometric mean of 100,95,90 is ", statistics.geometric_mean([100,95,90]))

print("median low of 100,95,90 is ", statistics.median_low([100,95,90]))

print("median high of 100,95,90 is ", statistics.median_high([100,95,90]))

print("median grouped of 100,95,90 is ", statistics.median_grouped([100,95,90], interval=10))

print("quantiles of 100,95,90 is ", statistics.quantiles([100,95,90], n=4, method='inclusive'))

print("quantiles of 100,95,90 is ", statistics.quantiles([100,95,90], n=4, method='exclusive'))