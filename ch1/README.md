# 最小限のアプリを作る
## MVTモデル
Flaskはユーザーインターフェイスを持つアプリを実装するためのデザインパターンとして、**MVTモデル**(Model, View, Template)を採用している。

| インターフェイス | 責務                                      |
| ---------------- | ----------------------------------------- |
| Model            | ビジネスロジックを担当する                |
| View             | 入力を受け取り、ModelとTemplateを制御する |
| Template         | 入出力を担当する                          |

一般的にはMVCモデルが有名だが、MVTのViewはMVCのC(Controller)、MVTのTemplateはMVCのViewに相当する。

![mvt](https://github.com/TakutoHashimoto/flask_book/assets/125980270/21cd58c8-afe3-48de-bd35-32ba9ccdd16d) 


## 最小限のアプリを作成する
最小限の機能を持つアプリ `minimalapp` を作成する。