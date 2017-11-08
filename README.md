# 网格策略（半）自动下单
自动获取股票收盘价，依据网格策略，自动下单。



## 网格策略
网格表数据来源即来自网格策略来自公众号：[股市药丸](http://weixin.sogou.com/weixin?type=1&s_from=input&query=%E8%82%A1%E5%B8%82%E8%8D%AF%E4%B8%B8&ie=utf8&_sug_=y&_sug_type_=&w=01019900&sut=11768&sst0=1506520645458&lkt=7%2C1506520634975%2C1506520645356)，关注公众号回复关键字“**网格**”，可查看策略。

根据股市药丸的网格表数据，结合我自己计划投入的资金量，我做了适用自己的[网格模型](https://github.com/luyh/test_easytrade/blob/master/%E7%BD%91%E6%A0%BC%E6%A8%A1%E5%9E%8B.numbers)。

我资金量不大，每天要盯数据手工下单显得特别费劲，正好最近在研究API/量化交易，找到[github-easytrader](https://github.com/shidenggui/easytrader)适来A股交易的接口（我用的银河证券），于是开干。

目前实现三个网格策略（华宝油气162411，证券ETF512880，及创业板ETF159915）（半）自动下委托单。

所谓半自动，是还需要人工处理少许错误或核对下单结果，确保无误。

##Dependence:

- [easytrader](https://github.com/shidenggui/easytrader)：
在windows下安装银河客户端，配置帐号，实现自动化交易
- [easyquotation](https://github.com/shidenggui/easyquotation)：获取行情数据


## 开发思路
其实就是模拟人用网格策略下单的思路，每天用程序挂委托单：
1. 获取（录入）网格表
2. 设置交易量
2. 利用easyquotation获取行情，获取收盘价
3. 查找所在网格位置
4. 获取网格交易价
5. 调用easytrader实现下单

## 效果截图
![](https://ooo.0o0.ooo/2017/11/08/5a03240a8e514.png)

![](https://i.loli.net/2017/11/08/5a0324426d557.png)



## 遇到的问题
当然，在测试过程中我发现能录单，但不能确认订单（得手工确认），然后我找下用代码实现两次回车，模拟人工的确认订单。

还有个问题是：客户端打开时，需将交易面版还原。不然程序不会执行下单。

## 进一步完善
- 修复手工确认订单两次回车的问题，这样可返回交易单号。群友已给出解决方案，我还未测试验证。
- 如果能每天帮打新债就好了
- 这个只是个人的小工作，更合规的可能要用些交易框架，比如[easyquant](https://github.com/shidenggui/easyquant)
