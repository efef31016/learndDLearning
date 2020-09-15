# !練習!內文無數學!心得整理!
# Movie_comment(datasets from keras)  cat_dog_classification with Pytorch(datasets from Kaggle)

心得
-------


深度學習對我來說非常深澳，儘管接觸了一年依舊對它沒什麼感覺，我就開始思考是不是
因為缺乏一些實戰經驗導致我如此迷茫。但自己沒有方向，但非常幸運地遇到一位教授，
願意花時間給我一些方向並督促我在這方面的進度，於是剛開始，我就從一場AIDEA舉辦的
比賽開始著手。
    真正在做的時候，發現資料的處理其實是非常重要的，所以我之後想學習有關於處理資料
的概念與一些技巧。在這次我把資料丟進模型裡跑，不知道是程式碼的問題還是我電腦硬體的
關係，跑了10個小時還沒跑出來，在最後也以失敗告終(因為太久)，這也是我第一次丟數據到模
型裡跑，感覺終於有點感覺了，但是還是有點空虛，畢竟那模型不是自己建的，資料也不是自己
抓的。
    所以在之後的練習中，我的目標是學會抓一些簡單的資料並做處理，並了解一些模型的基本
架構。

學到的一些
-------


1. 利用 for 迴圈讀取資料夾內的檔案(os)
2. 讓數據相關性可視化(heatmap)
3. LSTM、RNN 模型的基本架構


7月
-------
用 lstm+pytorch 做 IMDB 電影評論(原本是要用 rnn ，但網路上的 lstm+pytorch 寫比較詳細))。

是跟著以下網址做的:
https://zhuanlan.zhihu.com/p/140075236?fbclid=IwAR2ph8ex0XtLpdm229eu5TjbgbjzikHNgAUFjTVSJRciBR4FLCfGNQxIIAg
下載數據集:
kaggle:https://www.kaggle.com/mnk812/movie-comment/data?select=wiki_word2vec_50.bin

學到的一些
-------


1. 發現 python 可以用來解壓縮，所以可以把整個 IMDB 數據集的訓練直接用成一個模型，這樣方便調整路徑位置。
2. 成功繁體轉換無誤。
3. 發現理解一些概念真的需要熟悉並加強 class 的概念，所以就練習了class。寫個簡單的小互動遊戲當作練習，放在 practice文件中。

8月
-------
環境:
virtualenv
python3.8
torch.cuda.is_available == False( so i just do simple test)

跟著以下網址跑貓狗辨別:
https://reurl.cc/A8yraY

調整參數並觀察結果
-------
首先在簡單實做並測試(只有比較的跑的次數不同後的結果)
儲存第一個 model，訓練結果非常不樂觀，想必是硬體太差。

以下是訓練第一變與第十變的結果(每一遍的 epoch 為 6)
![image](https://github.com/efef31016/learndDLearning/blob/master/0.png)
![image](https://github.com/efef31016/learndDLearning/blob/master/9.png)
我取的資料集分常單純，與 https://reurl.cc/j5qzL2 一樣，所以覺得先不用在這一次
做真正的"改變參數"的動作，但是有一點值得觀察的是，跑到第四次出現了的非常巨大改變。

9月
-------
正式拿 Kaggle 的 25000 筆資料(訓練集)與 25000 資料(測試集)調整參數訓練並觀察結果。
以下為跑神經網路的相關硬體及參數資訊(溫馨提醒:別用文書電腦跑神經網路...):

訓練主要硬體:
CPU:intel(R) Pentium(R) CPU G3220 @ 3.00Hz (2 CPUs), ~3.0GHz

(model_1總共跑了13小時左右)
(model_2總共跑了30小時左右)
(model_3總共跑了15小時左右)

datasets train:70%   validate:30%
CNN
batch_size=8
n_epoch=16

model1: criterior=CEL(CrossEntropyLoss)
	opt=Adam
	learning_rate=0.0001
	
model2: criterior=CEL
	opt=SGD (momentum=0.9)
	learning_rate=0.0001

model3:criterior=CEL
	opt=SGD(no momentum)
	learning_rate=0.001(bigger than other two models)

以下為各自跑出的訓練集和驗證集和測試集準確率:
![image](https://github.com/efef31016/learndDLearning/blob/master/ok_1.png)
![image](https://github.com/efef31016/learndDLearning/blob/master/ok_2.png)
![image](https://github.com/efef31016/learndDLearning/blob/master/ok_3.png)
以下為更各個模型精確的準確率(最後一次):
![image](https://github.com/efef31016/learndDLearning/blob/master/result_comparison.png)
以下附上我的程式碼大剛:
![image](https://github.com/efef31016/learndDLearning/blob/master/key_steps.png)
