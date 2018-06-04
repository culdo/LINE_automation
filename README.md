# LINE_automation
一個讓Line大部份操作自動化的腳本
## 寫在前頭
* 首先有[Ruby環境](https://rubyinstaller.org/downloads/)
* 安裝瀏覽器自動化套件
```shell
gem install watir
```
* 再來你只要`git clone http://github.com/culdo/LINE_automation`
## 使用
在你的ruby腳本內require
```ruby
#!/env/bin/ruby
require 'Line.rb'

send_msg("你的訊息")
```
