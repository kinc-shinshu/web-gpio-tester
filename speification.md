## 前提条件
GPIOを簡単にテストしたい

## 目的
高速にGPIOをテストできること
ため息が出るほど画面が美しいこと
GPIOでできることを全て網羅できること
 - 出力、入力全て取れること

## 要件
pipでインストールできるようにしたい
コマンド一つで立ち上がって、利用できるようにしたい

## 仕様
 - ルーティング
   - ポート番号：４９８９
   - API
      - `POST /gpio/:port_number/out`
        - `:port_number`ピンに指定値`{0, 1}`のデジタル出力を設定する。
      - `POST /gpio/:port_number/in`
        - `:port_number`ピンを入力モードに設定する。
      - `GET /gpio/:post_number/read`
        - `:port_number`ピンの入力値を取得する。
      - `POST /gpio/:post_number/pwm`
        - `:port_number`ピンに指定周波数`{int}`のアナログモードに設定する。
      - `POST /gpio/:post_number/pwm/start`
        - `:port_number`ピンでアナログ出力を開始する。
      - `POST /gpio/:post_number/pwm/stop`
        - `:port_number`ピンでアナログ出力を停止する。

   - View
     - /
