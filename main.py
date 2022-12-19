import pandas as pd
import numpy as np
from scipy.stats import spearmanr

if __name__ == '__main__':
    # 名前はいらないので読み混むときに飛ばす
    data  = pd.read_csv("data.tsv", delimiter="\t",
                        header=0,
                        names=["A", "B", "C", "D", "E", "F", "G", "Total"])
    data.index = range(10)
    print(data)
    print()

    # 合計点でソートする
    data_rank = data["Total"].to_numpy()
    rank = np.argsort(-data_rank) + 1
    print(f"全体順位: {rank}")
    print()
 
    # 個人の投票 ("A" ~ "F")
    list_judges = ["A", "B", "C", "D", "E", "F", "G"]
    for judge in list_judges:
        data_rank_judge = data[judge].to_numpy()
        rank_judge = np.argsort(-data_rank_judge) + 1
        
        # 順位相関係数とp値
        corr, pv = spearmanr(rank, rank_judge)
        print(f"ジャッジ{judge}: {corr:>.3f} (p-value {pv:>.7f})")
        print(rank_judge)
        print()
    print()

    # ある個人以外の合計点でランキングを求めた場合
    for judge in list_judges:
        rem_judges = [j for j in list_judges if j != judge]
        data_rem = data[rem_judges]
        scores_rem = data_rem.sum(axis=1).to_numpy()
        rank_rem = np.argsort(-scores_rem) + 1

        # 順位相関係数とp値
        corr, pv = spearmanr(rank, rank_rem)
        print(f"ジャッジ{judge}以外: {corr:>.3f} (p-value {pv:>.7f})")
        print(rank_rem)
        print()
    print()