# 最小限のアプリを作る
Flaskはユーザーインターフェイスを持つアプリを実装するためのデザインパターンとして、**MVTモデル**(Model, View, Template)を採用している。

| インターフェイス | 責務                                      |
| ---------------- | ----------------------------------------- |
| Model            | ビジネスロジックを担当する                |
| View             | 入力を受け取り、ModelとTemplateを制御する |
| Template         | 入出力を担当する                          |

一般的にはMVCモデルが有名だが、MVTのViewはMVCのC(Controller)、MVTのTemplateはMVCのViewに相当する。

![mvc](../images/24406d24f9caae203df789bb7b6202e9023ed17b38bec5f8d6aac091247e47aa.png)  

