# coding:utf-8
# @Author:xb
# @Time: 2024/2/26 20:39
# @File:re库.py
import re




import requests


def request_dangdang(url):
    try:
        respose=requests.get(url)
        if respose.status_code == 200 :
            print("url 解析完成")
            return respose.text

    except requests.RequestException:
        return None


def pares_result(html):
    pattern=re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><spansclass="price_n">&yen;(.*?)</span>.*?</li>',re.S)
    print("分析页面代码")
    items = re.findall(pattern,html)

    for item in items :
        yield {
            'range': item[0],
            'iamge': item[1],
            'title': item[2],
            'recommend': item[3],
            'author': item[4],
            'times': item[5],
            'price': item[6]
        }
    for item in items:
        print(item)
def main(page):
    # url='http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-'+str(page)
    # html=request_dangdang(url)
    html=("""

    <li>
    <div class="list_num red">1.</div>   
    <div class="pic"><a href="http://product.dangdang.com/29600416.html" target="_blank"><img src="http://img3m6.ddimg.cn/10/9/29600416-1_l_1702884607.jpg" alt="爆品创新：新时代爆品打造法"  title="爆品创新：新时代爆品打造法"/></a></div>    
    <div class="name"><a href="http://product.dangdang.com/29600416.html" target="_blank" title="爆品创新：新时代爆品打造法">爆品创新：新时代爆品打造法</a></div>    
    <div class="star"><span class="level"><span style="width: 100%;"></span></span><a href="http://product.dangdang.com/29600416.html?point=comment_point" target="_blank">6069条评论</a><span class="tuijian">100%推荐</span></div>    
    <div class="publisher_info"><a href="http://search.dangdang.com/?key=姚萍" title="姚萍;雷虹;萨米尔" target="_blank">姚萍</a>;<a href="http://search.dangdang.com/?key=雷虹" title="姚萍;雷虹;萨米尔" target="_blank">雷虹</a>;<a href="http://search.dangdang.com/?key=萨米尔" title="姚萍;雷虹;萨米尔" target="_blank">萨米尔</a></div>    
    <div class="publisher_info"><span>2023-07-03</span>&nbsp;<a href="http://search.dangdang.com/?key=中国铁道出版社" target="_blank">中国铁道出版社</a></div>    

            <div class="biaosheng">五星评分：<span>6060次</span></div>
                      
    
    <div class="price">        
        <p><span class="price_n">&yen;32.50</span>
                        <span class="price_r">&yen;59.00</span>(<span class="price_s">5.5折</span>)
                    </p>
                    <p class="price_e"></p>
                <div class="buy_button">
                          <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29600416');" class="listbtn_buy">加入购物车</a>
                        
                        <a ddname="加入收藏" id="addto_favorlist_29600416" name="" href="javascript:showMsgBox('addto_favorlist_29600416',encodeURIComponent('29600416&platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
     
        </div>

    </div>
  
    </li>    
    
        
    
   """)
    items = pares_result(html)
    # for item in items:
    #     write_item_to_file(item)
    print(items[1])

if __name__ == "__main__":
    main(1)
# content = 'Xiaoshuair hms m101l ban1002nanas'
# res = re.match('Xi.*?m(.*?)l.*', content)
# if res is not None:
#     num = res.group(1)
#     print(num)  # Output: 100
# else:
#     print('No match found.')

# ("""<li>
#     <div class="list_num red">2.</div>
#     <div class="pic"><a href="http://product.dangdang.com/29678466.html" target="_blank"><img src="http://img3m6.ddimg.cn/48/26/29678466-1_l_1705386838.jpg" alt="国货崛起：传统品牌如何突围"  title="国货崛起：传统品牌如何突围"/></a></div>
#     <div class="name"><a href="http://product.dangdang.com/29678466.html" target="_blank" title="国货崛起：传统品牌如何突围">国货崛起：传统品牌如何突围</a></div>
#     <div class="star"><span class="level"><span style="width: 100%;"></span></span><a href="http://product.dangdang.com/29678466.html?point=comment_point" target="_blank">3049条评论</a><span class="tuijian">100%推荐</span></div>
#     <div class="publisher_info"><a href="http://search.dangdang.com/?key=吕秀兰" title="吕秀兰" target="_blank">吕秀兰</a></div>
#     <div class="publisher_info"><span>2024-01-01</span>&nbsp;<a href="http://search.dangdang.com/?key=电子工业出版社" target="_blank">电子工业出版社</a></div>
#
#             <div class="biaosheng">五星评分：<span>3046次</span></div>
#
#
#     <div class="price">
#         <p><span class="price_n">&yen;39.00</span>
#                         <span class="price_r">&yen;78.00</span>(<span class="price_s">5.0折</span>)
#                     </p>
#                     <p class="price_e">电子书：<span class="price_n">&yen;46.80</span></p>
#                 <div class="buy_button">
#                           <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29678466');" class="listbtn_buy">加入购物车</a>
#
#                         <a name="" href="http://product.dangdang.com/1901342505.html" class="listbtn_buydz" target="_blank">购买电子书</a>
#                         <a ddname="加入收藏" id="addto_favorlist_29678466" name="" href="javascript:showMsgBox('addto_favorlist_29678466',encodeURIComponent('29678466&platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
#
#         </div>
#
#     </div>
#
#     </li>
#
#     <li>
#     <div class="list_num red">3.</div>
#     <div class="pic"><a href="http://product.dangdang.com/29669700.html" target="_blank"><img src="http://img3m0.ddimg.cn/93/29/29669700-1_l_1703147538.jpg" alt="管理者20法则：看清领导力的底层逻辑"  title="管理者20法则：看清领导力的底层逻辑"/></a></div>
#     <div class="name"><a href="http://product.dangdang.com/29669700.html" target="_blank" title="管理者20法则：看清领导力的底层逻辑">管理者20法则：看清领导力的底层逻辑</a></div>
#     <div class="star"><span class="level"><span style="width: 100%;"></span></span><a href="http://product.dangdang.com/29669700.html?point=comment_point" target="_blank">2517条评论</a><span class="tuijian">100%推荐</span></div>
#     <div class="publisher_info">[美]<a href="http://search.dangdang.com/?key=丽莎·汉娜伯格" title="[美]丽莎·汉娜伯格 著，酷威文化 出品" target="_blank">丽莎·汉娜伯格</a> 著，<a href="http://search.dangdang.com/?key=酷威文化" title="[美]丽莎·汉娜伯格 著，酷威文化 出品" target="_blank">酷威文化</a> 出品</div>
#     <div class="publisher_info"><span>2024-01-01</span>&nbsp;<a href="http://search.dangdang.com/?key=四川文艺出版社" target="_blank">四川文艺出版社</a></div>
#
#             <div class="biaosheng">五星评分：<span>2041次</span></div>
#
#
#     <div class="price">
#         <p><span class="price_n">&yen;19.10</span>
#                         <span class="price_r">&yen;39.80</span>(<span class="price_s">4.8折</span>)
#                     </p>
#                     <p class="price_e">电子书：<span class="price_n">&yen;9.99</span></p>
#                 <div class="buy_button">
#                           <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29669700');" class="listbtn_buy">加入购物车</a>
#
#                         <a name="" href="http://product.dangdang.com/1901340076.html" class="listbtn_buydz" target="_blank">购买电子书</a>
#                         <a ddname="加入收藏" id="addto_favorlist_29669700" name="" href="javascript:showMsgBox('addto_favorlist_29669700',encodeURIComponent('29669700&platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
#
#         </div>
#
#     </div>
#
#     </li>
#
#     <li>
#     <div class="list_num ">4.</div>
#     <div class="pic"><a href="http://product.dangdang.com/29663601.html" target="_blank"><img src="http://img3m1.ddimg.cn/33/35/29663601-1_l_1701930256.jpg" alt="财富的底层逻辑"  title="财富的底层逻辑"/></a></div>
#     <div class="name"><a href="http://product.dangdang.com/29663601.html" target="_blank" title="财富的底层逻辑">财富的底层逻辑</a></div>
#     <div class="star"><span class="level"><span style="width: 100%;"></span></span><a href="http://product.dangdang.com/29663601.html?point=comment_point" target="_blank">2259条评论</a><span class="tuijian">100%推荐</span></div>
#     <div class="publisher_info"><a href="http://search.dangdang.com/?key=周路平" title="周路平  著，酷威文化 出品" target="_blank">周路平</a>  著，<a href="http://search.dangdang.com/?key=酷威文化" title="周路平  著，酷威文化 出品" target="_blank">酷威文化</a> 出品</div>
#     <div class="publisher_info"><span>2024-01-01</span>&nbsp;<a href="http://search.dangdang.com/?key=四川文艺出版社" target="_blank">四川文艺出版社</a></div>
#
#             <div class="biaosheng">五星评分：<span>2055次</span></div>
#
#
#     <div class="price">
#         <p><span class="price_n">&yen;20.20</span>
#                         <span class="price_r">&yen;42.00</span>(<span class="price_s">4.8折</span>)
#                     </p>
#                     <p class="price_e">电子书：<span class="price_n">&yen;8.99</span></p>
#                 <div class="buy_button">
#                           <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29663601');" class="listbtn_buy">加入购物车</a>
#
#                         <a name="" href="http://product.dangdang.com/1901340969.html" class="listbtn_buydz" target="_blank">购买电子书</a>
#                         <a ddname="加入收藏" id="addto_favorlist_29663601" name="" href="javascript:showMsgBox('addto_favorlist_29663601',encodeURIComponent('29663601&platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
#
#         </div>
#
#     </div>
#
#     </li>
#
#     <li>
#     <div class="list_num ">5.</div>
#     <div class="pic"><a href="http://product.dangdang.com/29517917.html" target="_blank"><img src="http://img3m7.ddimg.cn/77/20/29517917-1_l_1.jpg" alt="天工开物（中国17世纪的工艺百科全书）全注全译版"  title="天工开物（中国17世纪的工艺百科全书）全注全译版"/></a></div>
#     <div class="name"><a href="http://product.dangdang.com/29517917.html" target="_blank" title="天工开物（中国17世纪的工艺百科全书）全注全译版">天工开物（中国17世纪的工艺百科全书）全注全译版</a></div>
#     <div class="star"><span class="level"><span style="width: 100%;"></span></span><a href="http://product.dangdang.com/29517917.html?point=comment_point" target="_blank">8345条评论</a><span class="tuijian">100%推荐</span></div>
#     <div class="publisher_info">[明]<a href="http://search.dangdang.com/?key=宋应星" title="[明]宋应星 著，酷威文化 出品" target="_blank">宋应星</a> 著，<a href="http://search.dangdang.com/?key=酷威文化" title="[明]宋应星 著，酷威文化 出品" target="_blank">酷威文化</a> 出品</div>
#     <div class="publisher_info"><span>2023-03-01</span>&nbsp;<a href="http://search.dangdang.com/?key=北方文艺出版社" target="_blank">北方文艺出版社</a></div>
#
#             <div class="biaosheng">五星评分：<span>6013次</span></div>
#
#
#     <div class="price">
#         <p><span class="price_n">&yen;19.90</span>
#                         <span class="price_r">&yen;39.80</span>(<span class="price_s">5.0折</span>)
#                     </p>
#                     <p class="price_e">电子书：<span class="price_n">&yen;4.99</span></p>
#                 <div class="buy_button">
#                           <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29517917');" class="listbtn_buy">加入购物车</a>
#
#                         <a name="" href="http://product.dangdang.com/1901321819.html" class="listbtn_buydz" target="_blank">购买电子书</a>
#                         <a ddname="加入收藏" id="addto_favorlist_29517917" name="" href="javascript:showMsgBox('addto_favorlist_29517917',encodeURIComponent('29517917&platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
#
#         </div>
#
#     </div>
#
#     </li>
#
#     <li>
#     <div class="list_num ">6.</div>
#     <div class="pic"><a href="http://product.dangdang.com/29561416.html" target="_blank"><img src="http://img3m6.ddimg.cn/16/7/29561416-1_l_1690517797.jpg" alt="历史的镜子（中国史学大家吴晗经典作品）"  title="历史的镜子（中国史学大家吴晗经典作品）"/></a></div>
#     <div class="name"><a href="http://product.dangdang.com/29561416.html" target="_blank" title="历史的镜子（中国史学大家吴晗经典作品）">历史的镜子（中国史学大家吴晗经典作品）</a></div>
#     <div class="star"><span class="level"><span style="width: 100%;"></span></span><a href="http://product.dangdang.com/29561416.html?point=comment_point" target="_blank">6689条评论</a><span class="tuijian">100%推荐</span></div>
#     <div class="publisher_info"><a href="http://search.dangdang.com/?key=吴晗" title="吴晗" target="_blank">吴晗</a></div>
#     <div class="publisher_info"><span>2023-05-01</span>&nbsp;<a href="http://search.dangdang.com/?key=四川文艺出版社" target="_blank">四川文艺出版社</a></div>
#
#             <div class="biaosheng">五星评分：<span>4361次</span></div>
#
#
#     <div class="price">
#         <p><span class="price_n">&yen;33.80</span>
#                         <span class="price_r">&yen;39.80</span>(<span class="price_s">8.5折</span>)
#                     </p>
#                     <p class="price_e">电子书：<span class="price_n">&yen;4.99</span></p>
#                 <div class="buy_button">
#                           <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29561416');" class="listbtn_buy">加入购物车</a>
#
#                         <a name="" href="http://product.dangdang.com/1901327905.html" class="listbtn_buydz" target="_blank">购买电子书</a>
#                         <a ddname="加入收藏" id="addto_favorlist_29561416" name="" href="javascript:showMsgBox('addto_favorlist_29561416',encodeURIComponent('29561416&platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
#
#         </div>
#
#     </div>
#
#     </li>
#
#     <li>
#     <div class="list_num ">7.</div>
#     <div class="pic"><a href="http://product.dangdang.com/29675989.html" target="_blank"><img src="http://img3m9.ddimg.cn/46/28/29675989-1_l_1704448075.jpg" alt="鲁滨逊漂流记（经典全译本）"  title="鲁滨逊漂流记（经典全译本）"/></a></div>
#     <div class="name"><a href="http://product.dangdang.com/29675989.html" target="_blank" title="鲁滨逊漂流记（经典全译本）">鲁滨逊漂流记（经典全译本）</a></div>
#     <div class="star"><span class="level"><span style="width: 100%;"></span></span><a href="http://product.dangdang.com/29675989.html?point=comment_point" target="_blank">1052条评论</a><span class="tuijian">100%推荐</span></div>
#     <div class="publisher_info">[英]<a href="http://search.dangdang.com/?key=丹尼尔·笛福" title="[英]丹尼尔·笛福  著，酷威文化 出品" target="_blank">丹尼尔·笛福</a>  著，<a href="http://search.dangdang.com/?key=酷威文化" title="[英]丹尼尔·笛福  著，酷威文化 出品" target="_blank">酷威文化</a> 出品</div>
#     <div class="publisher_info"><span>2024-01-01</span>&nbsp;<a href="http://search.dangdang.com/?key=江苏凤凰文艺出版社" target="_blank">江苏凤凰文艺出版社</a></div>
#
#             <div class="biaosheng">五星评分：<span>1039次</span></div>
#
#
#     <div class="price">
#         <p><span class="price_n">&yen;12.00</span>
#                         <span class="price_r">&yen;48.00</span>(<span class="price_s">2.5折</span>)
#                     </p>
#                     <p class="price_e">电子书：<span class="price_n">&yen;5.99</span></p>
#                 <div class="buy_button">
#                           <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29675989');" class="listbtn_buy">加入购物车</a>
#
#                         <a name="" href="http://product.dangdang.com/1901341254.html" class="listbtn_buydz" target="_blank">购买电子书</a>
#                         <a ddname="加入收藏" id="addto_favorlist_29675989" name="" href="javascript:showMsgBox('addto_favorlist_29675989',encodeURIComponent('29675989&platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
#
#         </div>
#
#     </div>
#
#     </li>
#
#     <li>
#     <div class="list_num ">8.</div>
#     <div class="pic"><a href="http://product.dangdang.com/29660702.html" target="_blank"><img src="http://img3m2.ddimg.cn/5/22/29660702-1_l_1701412335.jpg" alt="聊斋志异（全注释文白对照版）蒲松龄中国古代志怪小说经典"  title="聊斋志异（全注释文白对照版）蒲松龄中国古代志怪小说经典"/></a></div>
#     <div class="name"><a href="http://product.dangdang.com/29660702.html" target="_blank" title="聊斋志异（全注释文白对照版）蒲松龄中国古代志怪小说经典">聊斋志异（全注释文白对照版）蒲松龄中国古代志怪小说经典</a></div>
#     <div class="star"><span class="level"><span style="width: 100%;"></span></span><a href="http://product.dangdang.com/29660702.html?point=comment_point" target="_blank">2229条评论</a><span class="tuijian">100%推荐</span></div>
#     <div class="publisher_info">[清]<a href="http://search.dangdang.com/?key=蒲松龄" title="[清]蒲松龄 著，酷威文化 出品" target="_blank">蒲松龄</a> 著，<a href="http://search.dangdang.com/?key=酷威文化" title="[清]蒲松龄 著，酷威文化 出品" target="_blank">酷威文化</a> 出品</div>
#     <div class="publisher_info"><span>2024-01-01</span>&nbsp;<a href="http://search.dangdang.com/?key=江苏凤凰文艺出版社" target="_blank">江苏凤凰文艺出版社</a></div>
#
#             <div class="biaosheng">五星评分：<span>2053次</span></div>
#
#
#     <div class="price">
#         <p><span class="price_n">&yen;15.50</span>
#                         <span class="price_r">&yen;39.80</span>(<span class="price_s">3.9折</span>)
#                     </p>
#                     <p class="price_e">电子书：<span class="price_n">&yen;4.99</span></p>
#                 <div class="buy_button">
#                           <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29660702');" class="listbtn_buy">加入购物车</a>
#
#                         <a name="" href="http://product.dangdang.com/1901339340.html" class="listbtn_buydz" target="_blank">购买电子书</a>
#                         <a ddname="加入收藏" id="addto_favorlist_29660702" name="" href="javascript:showMsgBox('addto_favorlist_29660702',encodeURIComponent('29660702&platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
#
#         </div>
#
#     </div>
#
#     </li>
#
#     <li>
#     <div class="list_num ">9.</div>
#     <div class="pic"><a href="http://product.dangdang.com/29647742.html" target="_blank"><img src="http://img3m2.ddimg.cn/14/12/29647742-1_l_1699331084.jpg" alt="水浒传（全3册）中国古典文学四大名著 原著无删足回正版"  title="水浒传（全3册）中国古典文学四大名著 原著无删足回正版"/></a></div>
#     <div class="name"><a href="http://product.dangdang.com/29647742.html" target="_blank" title="水浒传（全3册）中国古典文学四大名著 原著无删足回正版">水浒传（全3册）中国古典文学四大名著 原著无删足回正版</a></div>
#     <div class="star"><span class="level"><span style="width: 100%;"></span></span><a href="http://product.dangdang.com/29647742.html?point=comment_point" target="_blank">2159条评论</a><span class="tuijian">100%推荐</span></div>
#     <div class="publisher_info">[明]<a href="http://search.dangdang.com/?key=施耐庵" title="[明]施耐庵 [明]罗贯中 著，酷威文化 出品" target="_blank">施耐庵</a> [明]<a href="http://search.dangdang.com/?key=罗贯中" title="[明]施耐庵 [明]罗贯中 著，酷威文化 出品" target="_blank">罗贯中</a> 著，<a href="http://search.dangdang.com/?key=酷威文化" title="[明]施耐庵 [明]罗贯中 著，酷威文化 出品" target="_blank">酷威文化</a> 出品</div>
#     <div class="publisher_info"><span>2023-11-01</span>&nbsp;<a href="http://search.dangdang.com/?key=江苏凤凰文艺出版社" target="_blank">江苏凤凰文艺出版社</a></div>
#
#             <div class="biaosheng">五星评分：<span>2110次</span></div>
#
#
#     <div class="price">
#         <p><span class="price_n">&yen;24.00</span>
#                         <span class="price_r">&yen;96.00</span>(<span class="price_s">2.5折</span>)
#                     </p>
#                     <p class="price_e">电子书：<span class="price_n">&yen;8.99</span></p>
#                 <div class="buy_button">
#                           <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29647742');" class="listbtn_buy">加入购物车</a>
#
#                         <a name="" href="http://product.dangdang.com/1901339147.html" class="listbtn_buydz" target="_blank">购买电子书</a>
#                         <a ddname="加入收藏" id="addto_favorlist_29647742" name="" href="javascript:showMsgBox('addto_favorlist_29647742',encodeURIComponent('29647742&platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
#
#         </div>
#
#     </div>
#
#     </li>""")


# content = 'The quick brown fox jumps over the lazy dog. Today is 06/12/2022.'
# res = re.match('.*(\d{2}/\d{2}/\d{4}).*', content)
# if res is not None:
#     date = res.group(1)
#     print(date)  # Output: 06/12/2022
# else:
#     print('No match found.')
#
#
#
# content = 'Xiaoshuaib has 100 bananas'
# res = re.search('\d+', content)
# if res is not None:
#     num = res.group(0)
#     print(num)
# else:
#     print('No match found.')
# #
content = """Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;"""
res = re.findall('Xi.*?(\d+).*?',content,re.S)
print(res)
#
#
# content = 'Xiaoshuaib has 100 bananas'
# res = re.search('100', content)
# if res is not None:
#     text = res.group(0)
#     print(text)
# else:
#     print('No match found.')
#
#
#
# content = 'Xiaoshuaib has 100 bananas'
# res = re.search('\d+', content)
# if res is not None:
#     num = res.group(0)
#     print(num)  # Output: 100
# else:
#     print('No match found.')
#
