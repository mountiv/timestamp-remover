# Timestamp remover

This Python script is made to remove timestamps from YouTube transcript.

### Running

To run this script, Python must be installed in your PC.
Copy transcript file in the folder where located main.py and change its name as 'input.txt'.

Open terminal and run this command.

```
python main.py
```

### How it works?

Input:

```
1:39:53
これインターナショナルシッピングって 送料無料って言うんですけど送料無料で
1:39:59
出品されてる人が多いですけどたまに こんな感じで送料別で書いてる人もいるん
1:40:05
です よその送料も 読み取って最初には見てほしいですだから
1:40:11
例えば これであれば500 20ドルプラス2000円だったら最安値
1:40:20
じゃないんだけど 並び替えで言ったら一番上に来るんですよ
1:40:25
送料を含めない金額で表示されるんで
```

Output:

```
これインターナショナルシッピングって 送料無料って言うんですけど送料無料で
出品されてる人が多いですけどたまに こんな感じで送料別で書いてる人もいるん
です よその送料も 読み取って最初には見てほしいですだから
例えば これであれば500 20ドルプラス2000円だったら最安値
じゃないんだけど 並び替えで言ったら一番上に来るんですよ
送料を含めない金額で表示されるんで
```

Is it useful?