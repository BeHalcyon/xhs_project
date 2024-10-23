# 小红书最新加密算法已逆向完成，下列所有接口都可用

# 对熟悉爬虫想做副业的可以联系作者，作者有大量的爬虫副业

## Table of content

- [简介](#%E7%AE%80%E4%BB%8B)
- [性能](#%E6%80%A7%E8%83%BD)
- [changelog](#changelog)
- [how to run demo](#how-to-run-demo)
- [常见Q&A](#%E5%B8%B8%E8%A7%81qa)
- [作者提供的服务](#%E4%BD%9C%E8%80%85%E6%8F%90%E4%BE%9B%E7%9A%84%E6%9C%8D%E5%8A%A1)
    - [提供web单个api的源码服务](#6%E5%88%9B%E5%BB%BA%E5%B0%8F%E7%BA%A2%E4%B9%A6%E8%B4%A6%E5%8F%B7%E6%8C%87%E5%8D%97)
    - [创建小红书账号指南](#7%E6%8F%90%E4%BE%9B%E9%80%86%E5%90%91%E5%8D%95%E4%B8%AAapi%E7%9A%84%E6%BA%90%E7%A0%81%E6%9C%8D%E5%8A%A1)
- [作者联系方式、寻求帮助、合作](#%E4%BD%9C%E8%80%85%E8%81%94%E7%B3%BB%E6%96%B9%E5%BC%8F--%E5%AF%BB%E6%B1%82%E5%B8%AE%E5%8A%A9--%E5%90%88%E4%BD%9C)
- [Star History](#star-history)

![Static Badge](https://img.shields.io/badge/author-submato-gree)
![Static Badge](https://img.shields.io/badge/GitHub-blue?logo=GitHub&labelColor=black)
![Static Badge](https://img.shields.io/badge/author-3.7%2F3.8-blue?logo=Python&label=python&labelColor=black)
![Static Badge](https://img.shields.io/badge/Node.js-v18.16.1-blue?logo=Node.js&labelColor=black)
![Static Badge](https://img.shields.io/badge/java-1.8-blue?logo=java&labelColor=black)


## 感谢下列Sponsors对本仓库赞助

---
[system-design-pro](https://github.com/submato/system-design-pro)
> 针对中高级开发，**高质量**系统设计面试题及解答


*[成为赞助者，展示你的产品在这里](https://github.com/submato/xhscrawl/blob/main/service/service_index/ad.md)*

---

## 声明

**作者声明：没有在任何平台进行代码售卖，请谨慎鉴别，上当受骗作者一律不负责**

**本项目仅供学习交流，严禁用于任何商业和非法用途，非本人使用而产生的纠纷与一切后果均与本人无关。**

## 简介

本项项目是针对web端。小红书web的api都有加密，主要就是x-s。本项目是用python逆向小红书x-s。

## 性能
1. 本项目采用js计算，不使用playwright/selenium调用浏览器内核的方式。因为起浏览器太耗资源了，如果有高并发、多账号需求的生产环境很难容忍。
2. 整个请求(包括本地计算xs、发起请求、小红书处理请求、返回数据)，10次平均耗时在800ms左右，速度十分可观

<img width="75" heigth="75" alt="image" src="https://github.com/submato/xhscrawl/assets/55040284/4845e6e9-a8b1-42cd-9822-6a1a5658ef8e">


## changelog

[changelog](https://github.com/submato/xhscrawl/blob/main/changelog.md) 


## how to run demo

找到[demo/xhs.py](https://github.com/submato/xhscrawl/blob/main/demo/xhs.py) ,将自己需要的参数、cookie进行手动替换运行即可

- python环境
  - execjs包(可能编辑器会找不到这个包，真正名字叫PyExecJS)
  - 等其他import依赖
- java环境
- node js环境，需要支持ES13的 node js版本，也就是node js版本要晚于June 2022


## 常见Q&A

[常见Q&A](https://github.com/submato/xhscrawl/blob/main/service/service_index/feature_notice.md) 

## 作者提供的服务


### 创建小红书账号指南

[创建小红书账号指南](https://github.com/submato/xhscrawl/blob/main/service/service_index/account_manual.md)   


### 提供逆向单个api的源码

- **以下api均为web端api**
- 代码以最简单朴素的方式编写。
- 有详细的运行文档，接口文档，每一个参数都有说明。
- 作者会一直跟到在本地跑起来为止，因为代码原因跑不起来直接退款，都是做技术的，不玩那些虚。
- 量大有优惠，但这里不是菜市场，讨价还价的不用来

| 名称(里面有返回参数及价格)    | 
| ------------------------------------ |
|[发送评论](https://github.com/submato/xhscrawl/blob/main/service/service_index/comment.md)                   |
| [获取笔记详情](https://github.com/submato/xhscrawl/blob/main/service/service_index/note_detail.md)    |
| [笔记搜索](https://github.com/submato/xhscrawl/blob/main/service/service_index/search.md)                  |
| [用户搜索](https://github.com/submato/xhscrawl/blob/main/service/service_index/usersearch.md)                  |
| [获取笔记评论](https://github.com/submato/xhscrawl/blob/main/service/service_index/get_comment.md)                  |
| [收藏笔记](https://github.com/submato/xhscrawl/blob/main/service/service_index/collect_note.md)                |
| [给笔记点赞](https://github.com/submato/xhscrawl/blob/main/service/service_index/like_note.md)  
| [获取用户所有笔记](https://github.com/submato/xhscrawl/blob/main/service/service_index/user_notes.md)  |
| [获取用户详情](https://github.com/submato/xhscrawl/blob/main/service/service_index/user_info.md)  |
| [获取关键词搜索推荐信息](https://github.com/submato/xhscrawl/blob/main/service/service_index/search_keyword_recommend.md)  |
| [homefeed首页推荐](https://github.com/submato/xhscrawl/blob/main/service/service_index/homefeed.md)  |
| [自动发布笔记](https://github.com/submato/xhscrawl/blob/main/service/service_index/creat_note.md) |
| [消息-评论和@列表](https://github.com/submato/xhscrawl/blob/main/service/service_index/mentions.md)  |
| [消息-赞和收藏](https://github.com/submato/xhscrawl/blob/main/service/service_index/likes.md)  |
| [消息-新增关注列表](https://github.com/submato/xhscrawl/blob/main/service/service_index/connections.md)  |
| [未读通知数](https://github.com/submato/xhscrawl/blob/main/service/service_index/unread.md)  |
| [关注用户](https://github.com/submato/xhscrawl/blob/main/service/service_index/follow.md)  |
| [专业号-发送私信](https://github.com/submato/xhscrawl/blob/main/service/service_index/pro_chat_sent_msg.md)  |
| [专业号-私信列表](https://github.com/submato/xhscrawl/blob/main/service/service_index/pro_msg_list.md)  |
| [专业号-与某用户历史聊天消息](https://github.com/submato/xhscrawl/blob/main/service/service_index/pro_chat_history.md)  |
| [创作中心-笔记列表](https://github.com/submato/xhscrawl/blob/main/service/service_index/creator_note_list.md)  |
| [二维码登录获取cookie](https://github.com/submato/xhscrawl/blob/main/service/service_index/login_qrcode.md)  |
| [创作中心-话题推荐接口](https://github.com/submato/xhscrawl/blob/main/service/service_index/topic_recommend.md)  |
| [话题下笔记列表](https://github.com/submato/xhscrawl/blob/main/service/service_index/topic_notes.md)  |
| [本账号用户信息](https://github.com/submato/xhscrawl/blob/main/service/service_index/user_me.md)  |

| 若没有你需要的接口,联系作者有偿开发，[提需前必看](https://github.com/submato/xhscrawl/blob/main/service/service_index/feature_notice.md)    |


## 作者联系方式 || 寻求帮助 || 合作
联系作者前请务必查阅[常见Q&A](https://github.com/submato/xhscrawl/blob/main/service/service_index/feature_notice.md)
。能回答你90%的问题，节省自己、作者的宝贵时间。

由于出售的是源码，无法在线测试。介意勿扰

wx: <img width="200" alt="image" src="https://github.com/submato/xhscrawl/assets/55040284/d63ef610-527f-4d3c-af9b-9244b172faf5">

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=submato/xhscrawl&type=Date)](https://star-history.com/#submato/xhscrawl&Date)
