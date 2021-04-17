# -*- coding: utf-8 -*-

import argparse
import glob
import math
import os

import pandas as pd


# log(当日の終値,前日の終値(底))として対数表示したもの
# 一番最初のセルは計算できないので0を入力しておく
def add_log(dataframe):
    if 'Close' in dataframe.columns:
        for row_index in range(1, len(dataframe)):
            dataframe.at[row_index, 'LogClose'] = math.log(float(dataframe['Close'][row_index]), float(dataframe['Close'][row_index - 1]))
        dataframe.at[0, 'LogClose'] = 0
        return dataframe
    return None


if __name__ == '__main__':
    # コマンドラインで使うための設定
    parser = argparse.ArgumentParser(description = 'YahooファイナンスからDLしたCSVに前日終値と当日終値から対数を計算した列を追加')
    parser.add_argument('-d', '--dir', required = True, help = 'ダウンロードしたcsvファイルが含まれるディレクトリ')
    parser.add_argument('-dn', '--dirname', default = '対数追加済み', help = '編集後のCSVを入れるフォルダ名')
    args = parser.parse_args()

    # 保存先のパス
    export_dir = os.path.join(args.dir, args.dirname)

    # 選択したディレクトリからCSVファイルだけを検索
    for file_path in glob.glob(os.path.join(args.dir, '*.csv')):
        # 対数計算をする
        stock_csv = add_log(pd.read_csv(file_path))
        if stock_csv is None:
            continue
        if not os.path.exists(export_dir):
            os.makedirs(export_dir)
        # CSVの書き出し
        stock_csv.to_csv(os.path.join(export_dir, os.path.basename(file_path)))
