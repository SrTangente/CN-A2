import matplotlib.pyplot as plt
from networkx.algorithms import *
import collections
import numpy as np
from sklearn.linear_model import LinearRegression

def degree_distributions(graph, apply_log):
    G = graph

    degree_sequence = sorted([d for n, d in G.degree()])  # degree sequence
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())

    total_count = np.sum(cnt)

    kmin = np.min(deg)
    kmax = np.max(deg)

    log_k = np.log10(deg)

    log_kmin = np.log10(kmin)
    log_kmax = np.log10(kmax)

    #print('log_kmin ', log_kmin)
    #print('log_kmax ', log_kmax)

    x_bins = np.arange(log_kmin, np.log10(kmax+1), 0.1*(np.log10(kmax+1)-log_kmin))

    bins = np.zeros([10])

    for v in range(len(x_bins)-1):
        for l in range(len(log_k)):
            if log_k[l] >= x_bins[v] and log_k[l] < x_bins[v+1]:
                bins[v] += cnt[l]

    fig, ax = plt.subplots(1, 2)

    #print(bins)
    #print(x_bins)
    div_bins = bins / total_count

    # PDF
    if apply_log:
        ax[0].bar(x_bins, div_bins, color="b", width=0.1*(np.log10(kmax+1)-log_kmin))
        ax[0].set_ylabel("log(P(k))")
        ax[0].set_xlabel("log(k)")
    else:
        ax[0].bar(deg, cnt / total_count, color="b")
        ax[0].set_ylabel("P(k)")
        ax[0].set_xlabel("k")
    ax[0].set_title("PDF")


    # CCDF
    accumulated_bins = [np.sum(div_bins[i: len(bins)]) for i in range(0, len(bins))]
    accumulated_cnt = [np.sum(cnt[i: len(cnt)]) for i in range(0, len(cnt))]

    ax[1].set_title("CCDF")
    if apply_log:
        ax[1].set_ylabel("log(P(K>=k))")
        ax[1].set_xlabel("log(k)")
        ax[1].bar(x_bins, accumulated_bins, color="b", width=0.1*(np.log10(kmax+1)-log_kmin))
    else:
        ax[1].set_ylabel("P(K>=k)")
        ax[1].set_xlabel("k")
        ax[1].bar(deg, accumulated_cnt / total_count, color="b")


    #estimation of the exponent
    x = x_bins
    y = np.asarray(div_bins)
    x = x[y!=0]
    y = np.log(y[y!=0])

    reg = LinearRegression().fit(x.reshape(-1,1),y)
    print("Estimation exponent: "+ str(-reg.coef_+1))
    plt.show()


def PDF(graph, apply_log):
    G = graph

    degree_sequence = sorted([d for n, d in G.degree()])  # degree sequence
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())

    total_count = np.sum(cnt)

    kmin = np.min(deg)
    kmax = np.max(deg)

    log_k = np.log10(deg)

    log_kmin = np.log10(kmin)
    log_kmax = np.log10(kmax)

    print('log_kmin ', log_kmin)
    print('log_kmax ', log_kmax)

    x_bins = np.arange(log_kmin, np.log10(kmax+1), 0.1*(np.log10(kmax+1)-log_kmin))

    bins = np.zeros([10])

    for v in range(len(x_bins)-1):
        for l in range(len(log_k)):
            if log_k[l] >= x_bins[v] and log_k[l] < x_bins[v+1]:
                bins[v] += cnt[l]

    fig, ax = plt.subplots(1, 2)

    print(bins)
    print(x_bins)
    div_bins = bins / total_count

    # PDF
    if apply_log:
        ax[0].bar(x_bins, div_bins, color="b", width=0.1*(np.log10(kmax+1)-log_kmin))
        ax[0].set_ylabel("log(P(k))")
        ax[0].set_xlabel("log(k)")
    else:
        ax[0].bar(deg, cnt / total_count, color="b")
        ax[0].set_ylabel("P(k)")
        ax[0].set_xlabel("k")
    ax[0].set_title("PDF")

def CCDF(graph, apply_log):
    G = graph

    degree_sequence = sorted([d for n, d in G.degree()])  # degree sequence
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())

    total_count = np.sum(cnt)

    kmin = np.min(deg)
    kmax = np.max(deg)

    log_k = np.log10(deg)

    log_kmin = np.log10(kmin)
    log_kmax = np.log10(kmax)

    print('log_kmin ', log_kmin)
    print('log_kmax ', log_kmax)

    x_bins = np.arange(log_kmin, np.log10(kmax+1), 0.1*(np.log10(kmax+1)-log_kmin))

    bins = np.zeros([10])

    for v in range(len(x_bins)-1):
        for l in range(len(log_k)):
            if log_k[l] >= x_bins[v] and log_k[l] < x_bins[v+1]:
                bins[v] += cnt[l]

    fig, ax = plt.subplots(1, 2)

    print(bins)
    print(x_bins)
    div_bins = bins / total_count


    # CCDF
    accumulated_bins = [np.sum(div_bins[i: len(bins)]) for i in range(0, len(bins))]
    accumulated_cnt = [np.sum(cnt[i: len(cnt)]) for i in range(0, len(cnt))]

    ax[1].set_title("CCDF")
    if apply_log:
        ax[1].set_ylabel("log(P(K>=k))")
        ax[1].set_xlabel("log(k)")
        ax[1].bar(x_bins, accumulated_bins, color="b", width=0.1*(np.log10(kmax+1)-log_kmin))
    else:
        ax[1].set_ylabel("P(K>=k)")
        ax[1].set_xlabel("k")
        ax[1].bar(deg, accumulated_cnt / total_count, color="b")

    plt.show()